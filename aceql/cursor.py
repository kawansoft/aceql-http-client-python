#
# This file is part of AceQL Python Client SDK.
# AceQL Python Client SDK: Remote SQL access over HTTP with AceQL HTTP.
# Copyright (C) 2020,  KawanSoft SAS
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

from aceql._private.row_parser import *
from aceql._private.aceql_http_api import *


class Cursor(object):
    """Cursor class."""

    def __init__(self, connection, aceql_http_api):
        self.__connection = connection
        self.__aceql_http_api = aceql_http_api
        self.__is_closed = False

        self.__rowcount = -1
        self.__description = []

        self.__filelist = []
        self.arraysize = 1

        self.__row_parser = None

    @property
    def description(self):
        """Describes the name and SLQ type of each column.

        (5 other elements are not set in this version)"""

        self.__raise_error_if_closed()
        return self.__description

    @property
    def rowcount(self):
        """This read-only attribute specifies the number of rows that the last .execute*()
        produced (for DQL statements like SELECT)
        or affected (for DML statements like UPDATE or INSERT)"""
        self.__raise_error_if_closed()
        return self.__rowcount

    def execute(self, sql, params=()):
        """Executes the given operation

        Executes the given operation substituting any markers with
        the given parameters.

        For example, getting all rows where id is 5:
          cursor.execute("SELECT * FROM t1 WHERE id = ?", (5,))
        """
        self.__raise_error_if_closed()

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
        self.__raise_error_if_closed()
        raise NotImplementedError("executemany is not implemented in this AceQL SDK version.")

    def __execute_update(self, sql, params=()):
        """Executes and update operation on remote database"""

        blob_streams = []

        try:
            the_cursor_util = CursorUtil()
            parms_dict = the_cursor_util.get_http_parameters_dict(params)

            blob_ids = the_cursor_util.blob_ids
            blob_streams = the_cursor_util.blob_streams
            blob_lengths = the_cursor_util.blob_lengths

            cpt = 0
            for blob_id in blob_ids:
                self.__aceql_http_api.blob_upload(blob_id, blob_streams[cpt], blob_lengths[cpt])
                cpt += 1

            AceQLDebug.debug("parms_dict: " + str(parms_dict))

            is_prepared_statement = False
            if len(parms_dict) > 0:
                is_prepared_statement = True

            rows = self.__aceql_http_api.execute_update(sql, is_prepared_statement, parms_dict)
            self.__rowcount = rows
            return rows
        finally:
            for blob_stream in blob_streams:
                blob_stream.close()

    def __execute_query(self, sql, params=()):
        """Executes a SELECT on remote database"""
        self.__raise_error_if_closed()

        self.row_count = 0
        self.__description = []

        the_cursor_util = CursorUtil()
        parms_dict = the_cursor_util.get_http_parameters_dict(params)

        is_prepared_statement = False
        if len(parms_dict) > 0:
            is_prepared_statement = True

        self.__result_set_info = self.__aceql_http_api.execute_query(sql, is_prepared_statement, parms_dict)

        # Appends the files to delete
        self.__filelist.append(self.__result_set_info.get_filename())

        self.__rowcount = self.__result_set_info.get_row_count()

        AceQLDebug.debug("self.rowcount: " + str(self.__rowcount))
        AceQLDebug.debug("filename    : " + self.__result_set_info.get_filename())

        # first build the description for Cursor.description
        self.__build_description()

        self.__row_parser = RowParser(self.__result_set_info.get_filename(), self.__result_set_info.get_row_count())

    def fetchone(self):
        """ Fetch the next row of a query result set, returning a single sequence,
        or None when no more data is available"""

        self.__raise_error_if_closed()
        row_available = self.__row_parser.build_next_row()

        if not row_available:
            return None

        values_per_column_index = self.__row_parser.get_values_per_col_index()
        types_per_column_index = self.__row_parser.get_types_per_col_index()

        if Parms.DEBUG_ON:
            print("values_per_column_index: " + str(values_per_column_index))
            print("types_per_column_index : " + str(types_per_column_index))

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
            elif types_per_column_index[index] == "TIME":
                the_list.append(DateTimeUtil.get_time_from_timestamp(v))
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

        self.__raise_error_if_closed()
        size_to_use = size
        if size_to_use <= 1:
            size_to_use = self.arraysize

        list_tuples = []
        cpt = 0
        while True:
            the_tup = self.fetchone()
            cpt += 1
            if the_tup is None:
                break
            list_tuples.append(the_tup)
            if cpt >= size_to_use:
                return list_tuples

        return list_tuples

    def fetchall(self):
        """Fetches all (remaining) rows of a query result, returning a list.

            Note that the cursors arraysize attribute can affect the performance
            of this operation. An empty list is returned when no rows are available.
        """
        self.__raise_error_if_closed()

        list_tuples = []
        while True:
            the_tup = self.fetchone()
            if the_tup is None:
                break
            list_tuples.append(the_tup)

        return list_tuples

    def setinputsizes(self, sizes):
        """ Does nothing. Implemented for respect to PEP 249."""
        pass

    def setoutputsize(self, sizes, column=None):
        """ Does nothing. Implemented for respect to PEP 249."""
        pass

    def __build_description(self):
        """ Builds the .description property"""

        self.__raise_error_if_closed()
        self.__description = []

        if self.__rowcount < 1:
            return

        row_parser = None

        try:
            row_parser = RowParser(self.__result_set_info.get_filename(), self.__rowcount)
            row_parser.build_next_row()  # read first row to get the column names, only way to do it...

            aceql_types = row_parser.get_types_per_col_index()
            aceql_names = row_parser.column_names_per_index()

            AceQLDebug.debug("aceql_types : " + str(aceql_types))
            AceQLDebug.debug("aceql_names: " + str(aceql_names))

            index = 0

            while index < len(aceql_types):
                name_and_type = list()

                #name_and_type.append(aceql_names[index])
                #name_and_type.append(aceql_types[index])

                aceql_name = aceql_names.get(index)
                if aceql_name is not None:
                    name_and_type.append(aceql_name)

                name_and_type.append(aceql_types.get(index))

                # Append 5 non set values
                name_and_type.append(None)
                name_and_type.append(None)
                name_and_type.append(None)
                name_and_type.append(None)
                name_and_type.append(None)

                the_tup = tuple(name_and_type)
                self.__description.append(the_tup)
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
    # 	self.__aceql_http_api.blob_download(blob_id, filename, total_length,
    # 	progress_holder)

    def get_blob_length(self, column_index):
        """ Gets the remote BLOB length  on a column in the current row

        To be used if progress indicator needed.

        """
        self.__raise_error_if_closed()

        if column_index is None:
            raise TypeError("column_index is null!")

        values_per_column_index = self.__row_parser.get_values_per_col_index()

        AceQLDebug.debug("values_per_column_index: " + str(values_per_column_index))

        if values_per_column_index is None:
            raise Error("Not positioned on a row. (No fetchone call done.)",
                        0, None, None, 200)

        blob_id = values_per_column_index[column_index]

        print("blob_id: " + str(blob_id))

        if blob_id is None:
            raise Error("No value found for column_index " + str(column_index),
                        0, None, None, 200)

        if not blob_id.endswith(".blob"):
            raise Error("Fetched value does not correspond to a BLOB Id: " + str(blob_id),
                        0, None, None, 200)

        blob_length = self.__aceql_http_api.get_blob_length(blob_id)
        return blob_length

    def get_blob_stream(self, column_index):
        """ Returns a BLOB stream on a column in the current row.

            The column index starts at 0.
        """

        self.__raise_error_if_closed()

        if column_index is None:
            raise TypeError("column_index is null!")

        values_per_column_index = self.__row_parser.get_values_per_col_index()

        if values_per_column_index is None:
            raise Error("Not positioned on a row. (Seems no fetchone() call done.)",
                        0, None, None, 200)

        blob_id = values_per_column_index[column_index]

        if blob_id is None:
            raise Error("No value found for column_index " + str(column_index),
                        0, None, None, 200)

        if not blob_id.endswith(".blob"):
            raise Error("Fetched value does not correspond to a BLOB Id: " + str(blob_id),
                        0, None, None, 200)

        # OK!  we have a valid BLOB Id:
        response = self.__aceql_http_api.get_blob_stream(blob_id)
        return response

    def close(self):
        """ Closes the cursor and releases underlying stream & file resource (result set). """

        if self.__is_closed:
            return

        self.__is_closed = True

        if self.__row_parser is not None:
            self.__row_parser.close()  # very important

        if Parms.DELETE_FILES:
            for filename in self.__filelist:
                os.remove(filename)

    def __raise_error_if_closed(self):
        if self.__is_closed:
            raise Error("Invalid call: Cursor is closed.", 0, None, None, 200)