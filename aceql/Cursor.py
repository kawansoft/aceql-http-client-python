#
# This file is part of AceQL Python Client SDK.
# AceQL Python Client SDK: Remote SQL access over HTTP with AceQL HTTP.
# Copyright (C) 2017,  KawanSoft SAS
# (http://www.kawansoft.com). All rights reserved.                                
#                                                                               
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License. 
##

from aceql._private.CursorUtil import *
from aceql._private.RowParser import *
from aceql._private.AceQLHttpApi import *


class Cursor(object):
    """Cursor class."""

    def __init__(self, aceqlConnection, aceQLHttpApi):
        self.__connection = aceqlConnection
        self.__aceQLHttpApi = aceQLHttpApi
        self.__is_closed = False

        self.__rowcount = -1
        self.__description = []

        self.__filelist = []
        self.arraysize = 1

    @property
    def description(self):
        """Describes the name and SLQ type of each column.

        (5 other elements are not set in this version)"""

        return self.__description

    @property
    def rowcount(self):
        """This read-only attribute specifies the number of rows that the last .execute*()
        produced (for DQL statements like SELECT)
        or affected (for DML statements like UPDATE or INSERT)"""
        return self.__rowcount

    def execute(self, sql, params=()):
        """Executes the given operation

        Executes the given operation substituting any markers with
        the given parameters.

        For example, getting all rows where id is 5:
          cursor.execute("SELECT * FROM t1 WHERE id = ?", (5,))
        """

        if sql is None:
            raise TypeError("sql is null!")

        sql = sql.strip()

        if sql.lower().startswith("select"):
            return self.__execute_query(sql, params)
        else:
            return self.__execute_update(sql, params)

    def executemany(self):
        """Execute the given operation multiple times.

        Not implemented in this version.
        """
        raise NotImplementedError("executemany is not implemented in this AceQL SDK version.")

    def __execute_update(self, sql, params=()):
        """Executes and update operation on remote database"""

        blob_streams = []

        try:
            cursor_util = CursorUtil()
            parms_dict = cursor_util.get_http_parameters_dict(params)

            blob_ids = cursor_util.blob_ids
            blob_streams = cursor_util.blob_streams
            blob_lengths = cursor_util.blob_lengths

            cpt = 0
            for blob_id in blob_ids:
                self.__aceQLHttpApi.blob_upload(blob_id, blob_streams[cpt], blob_lengths[cpt])
                cpt += 1

            AceQLDebug.debug("parms_dict: " + str(parms_dict))

            isPreparedStatement = False
            if len(parms_dict) > 0:
                isPreparedStatement = True

            rows = self.__aceQLHttpApi.execute_update(sql, isPreparedStatement, parms_dict)
            self.__rowcount = rows
            return rows
        finally:
            for blob_stream in blob_streams:
                blob_stream.close()

    def __execute_query(self, sql, params=()):
        """Executes a SELECT on remote database"""
        self.row_count = 0
        self.__description = []

        cursor_util = CursorUtil()
        parms_dict = cursor_util.get_http_parameters_dict(params)

        isPreparedStatement = False
        if len(parms_dict) > 0:
            isPreparedStatement = True

        self.__result_set_info = self.__aceQLHttpApi.execute_query(sql, isPreparedStatement, parms_dict)

        # Appends the files to delete
        self.__filelist.append(self.__result_set_info.get_filename())

        self.__rowcount = self.__result_set_info.get_row_count()

        AceQLDebug.debug("self.rowcount: " + str(self.__rowcount))
        AceQLDebug.debug("filename    : " + self.__result_set_info.get_filename())

        # first buil the description for Curose.description
        self.__build_description()

        self.__row_parser = RowParser(self.__result_set_info.get_filename(), self.__result_set_info.get_row_count())

    def __iter__(self):
        """
        Iteration over the result set which calls self.fetchone()
        and returns the next row.
        """
        return iter(self.fetchone, None)

    def fetchone(self):
        """ Fetch the next row of a query result set, returning a single sequence,
        or None when no more data is available"""
        row_available = self.__row_parser.buildNextRow()

        if not row_available:
            return None

        values_per_column_index = self.__row_parser.get_values_per_col_index()
        types_per_column_index = self.__row_parser.get_types_per_col_index()

        the_list = []
        index = 0
        for k, v in values_per_column_index.items():
            # print(k, v)
            # detect Epoch timestamp and convert them to date for DATE and datetime for
            # TIMESTAMP
            if types_per_column_index[index] == "TIMESTAMP":
                the_list.append(DateTimeUtil.get_datetime_from_timestamp(v))
            elif types_per_column_index[index] == "DATE":
                the_list.append(DateTimeUtil.get_date_from_timestamp(v))
            else:
                the_list.append(v)

            index += 1

        the_tup = tuple(the_list)
        return the_tup

    def fetchmany(self, size=-1):
        """Fetch the next set of rows of a query result, returning a sequence of sequences

        (e.g. a list of tuples). An empty sequence is returned when no more rows are available.

        The number of rows to fetch per call is specified by the parameter.
        If it is not given, the cursor's arraysize determines the number of rows to be fetched."""

        sizeToUse = size
        if sizeToUse <= 1:
            sizeToUse = self.arraysize

        list_tuples = []
        cpt = 0
        while (True):
            theTup = self.fetchone()
            cpt += 1
            if (theTup is None):
                break
            list_tuples.append(theTup)
            if cpt >= sizeToUse:
                return list_tuples

        return list_tuples

    def fetchall(self):
        """Fetches all (remaining) rows of a query result, returning a list.

            Note that the cursors arraysize attribute can affect the performance
            of this operation. An empty list is returned when no rows are available.
        """

        list_tuples = []
        while (True):
            theTup = self.fetchone()
            if (theTup is None):
                break
            list_tuples.append(theTup)

        return list_tuples

    def setinputsizes(self, sizes):
        """ Does nothing. Implemented to respect PEP 249."""
        pass

    def setoutputsize(self, sizes, column=None):
        """ Does nothing. Implemented to respect PEP 249."""
        pass

    def close(self):
        """ Closes the cursor and releases underlying file resource (result set). """
        self.__is_closed = True
        self.__row_parser.close()  # very important

        if Parms.DELETE_FILES:
            for filename in self.__filelist:
                os.remove(filename)

    def __build_description(self):
        """ Builds the .description property"""

        if self.__rowcount < 1:
            return

        row_parser = None

        try:
            row_parser = RowParser(self.__result_set_info.get_filename(), self.__rowcount)
            row_parser.buildNextRow()  # read first row to get the column names, only way to do it...

            aceql_types = row_parser.get_types_per_col_index()
            aceql_names = row_parser.column_names_per_index()

            AceQLDebug.debug("aceql_types : " + str(aceql_types))
            AceQLDebug.debug("aceql_names: " + str(aceql_names))

            index = 0
            while index < len(aceql_types):
                name_and_type = []
                name_and_type.append(aceql_names[index])
                name_and_type.append(aceql_types[index])

                # Append 5 non set values
                name_and_type.append(None)
                name_and_type.append(None)
                name_and_type.append(None)
                name_and_type.append(None)
                name_and_type.append(None)

                theTup = tuple(name_and_type)
                self.__description.append(theTup)
                index += 1

        finally:
            if row_parser is not None:
                row_parser.close()

    # def blob_download(self, blob_id, filename, total_length=0,
    # progress_holder=None):
    # 	""" Allows to download a blob corresponding to a blob_id into a filename
    #
    # 		total_length & and a ProgressHolder instance may be passed for progress
    # 		indication.
    # 	"""
    #
    # 	if blob_id is None:
    # 		raise TypeError("blob_id is null!")
    #
    # 	if filename is None:
    # 		raise TypeError("filename is null!")
    #
    # 	self.__aceQLHttpApi.blob_download(blob_id, filename, total_length,
    # 	progress_holder)

    def get_blob_length(self, column_index):
        """ Gets the remote BLOB length  on a column in the current row

        To be used if progress indicator needed.

        """
        if column_index is None:
            raise TypeError("column_index is null!")

        values_per_column_index = self.__row_parser.get_values_per_col_index()

        AceQLDebug.debug("values_per_column_index: " + str(values_per_column_index))

        if values_per_column_index is None:
            raise Error("Not positioned on a row. (No fetchone call done.)",
                        0, None, None, self.__http_status_code)

        blob_id = values_per_column_index[column_index]

        print("blob_id: " + str(blob_id))

        if blob_id is None:
            raise Error("No value found for column_index " + str(column_index),
                        0, None, None, self.__http_status_code)

        if not blob_id.endswith(".blob"):
            raise Error("Fetched value does not correspond to a BLOB Id: " + str(blob_id),
                        0, None, None, self.__http_status_code)

        blob_length = self.__aceQLHttpApi.get_blob_length(blob_id)
        return blob_length

    def get_blob_stream(self, column_index):
        """ Allows to get a BLOB stream on a column in the current row.

            The column index starts at 0.
        """
        if column_index is None:
            raise TypeError("column_index is null!")

        values_per_column_index = self.__row_parser.get_values_per_col_index()

        if values_per_column_index is None:
            raise Error("Not positioned on a row. (Seems no fetchone() call done.)",
                        0, None, None, self.__http_status_code)

        blob_id = values_per_column_index[column_index]

        if blob_id is None:
            raise Error("No value found for column_index " + str(column_index),
                        0, None, None, self.__http_status_code)

        if not blob_id.endswith(".blob"):
            raise Error("Fetched value does not correspond to a BLOB Id: " + str(blob_id),
                        0, None, None, self.__http_status_code)

        # OK!  we have a valid BLOB Id:
        response = self.__aceQLHttpApi.get_blob_stream(blob_id)
        return response
