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
from typing import List

from aceql import Connection
from aceql._private.table_names_dto import TableNamesDto
from aceql._private.jdbc_database_meta_data_dto import JdbcDatabaseMetaDataDto
from aceql._private.table_dto import TableDto
from aceql.metadata.table import Table
from aceql.metadata.jdbc_database_meta_data import JdbcDatabaseMetaData


class RemoteDatabaseMetaData(object):

    """Allows to retrieve metadata info from the remote SQL database."""

    def __init__(self, connection: Connection):
        self.__connection = connection
        self.__aceql_http_api = self.__connection._get_aceql_http_api

    def db_schema_download(self, file: str, file_format: str = None, table_name: str = None):
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

    def get_jdbc_database_meta_data(self) -> JdbcDatabaseMetaData:
        """
        Returns the basic meta data values of the remote database, as sent by the the remote JDBC Driver of the remote database.
        :return:
        the basic meta data values sent by the the remote JDBC Driver of the remote database.
        """
        jdbc_database_meta_data_holder : JdbcDatabaseMetaDataDto = self.__aceql_http_api.get_db_metadata()
        return jdbc_database_meta_data_holder.jdbcDatabaseMetaData

    def get_table_names(self, table_type: str =None) -> List[str]:
        """
        Returns The list of tables
        :param table_type:
        the table type. Possible values: "table","view", etc. Defaults to all types if null.

        :return:
        The list of tables
        """
        table_names_dto : TableNamesDto = self.__aceql_http_api.get_table_names(table_type)
        table_names: List[str] = table_names_dto.tableNames
        return table_names

    def get_table(self, name: str) -> Table:
        """
        Returns the Table details
        :param name:
        The name table to get without any prefix/dot

        :return:
        The Table details
        """
        if name is None:
            raise TypeError("table name is null!")

        table_dto: TableDto = self.__aceql_http_api.get_table(name)
        table: Table = table_dto.table
        return table
