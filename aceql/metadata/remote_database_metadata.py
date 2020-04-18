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

from aceql import HolderJdbcDatabaseMetaData


class RemoteDatabaseMetaData(object):
    """Allows to retrieve metadata info of the remote SQL database."""

    def __init__(self, connection):
        self.__connection = connection
        self.__aceql_http_api = self.__connection._get_aceql_http_api

    def db_schema_download(self, file, file_format = None, table_name= None):
        """
        Downloads the schema extract for a table name in the specified HTML or Text format.

        Parameters
        ----------
        file : str
            The filename to store the output schema in
        file_format
            the format of the output "html" or "text". Defaults to "html"
        table_name
            if specified, output will be done only for the table
        """

        if file is None:
            raise TypeError("file is null!")

        if file_format is None:
            file_format = "html"

        if file_format != "html" and file_format != "text":
            raise TypeError("Invalid format value. Must be \"file\" or \"text\". Is: " + file_format)

        response = self.__aceql_http_api.db_schema_download(file_format, table_name)

        with open(file, 'wb') as fd:
            for chunk in response.iter_content(chunk_size=2048):
                fd.write(chunk)

    def get_jdbc_database_meta_data(self):
        """
        Returns the basic meta data values of the remote database, as sent by the the remote JDBC Driver of the remote database.
        :return:
        the basic meta data values sent by the the remote JDBC Driver of the remote database.
        """
        jdbc_database_meta_data_holder : HolderJdbcDatabaseMetaData = self.__aceql_http_api.get_db_metadata()
        return jdbc_database_meta_data_holder.jdbcDatabaseMetaData
