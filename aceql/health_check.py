#
# This file is part of AceQL Python Client SDK.
# AceQL Python Client SDK: Remote SQL access over HTTP with AceQL HTTP.
# Copyright (C) 2021,  KawanSoft SAS
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
import time
from typing import List

import requests
from requests import Request

from aceql import Connection, Error
from aceql._private.aceql_debug import AceQLDebug
from aceql._private.aceql_execution_util import AceQLExecutionUtil
from aceql._private.dto.table_names_dto import TableNamesDto
from aceql._private.dto.jdbc_database_meta_data_dto import JdbcDatabaseMetaDataDto
from aceql._private.dto.table_dto import TableDto
from aceql._private.file_util import FileUtil
from aceql._private.result_analyzer import ResultAnalyzer
from aceql.metadata.table import Table
from aceql.metadata.jdbc_database_meta_data import JdbcDatabaseMetaData


class HealthCheck(object):

    """Allows checking the remote server's availability & response time. It will be enhanced in future versions."""

    def __init__(self, connection: Connection):
        self.__connection = connection
        self.__aceql_http_api = self.__connection._get_aceql_http_api
        self.__error = None

    def ping(self) -> bool:
        """Allows to ping the AceQL server main servlet. Returns True if the server is pingable."""
        try:
            url: str = self.__connection.get_url();
            result = self.__aceql_http_api.call_with_get_url(url)

            result_analyzer = ResultAnalyzer(result, self.__http_status_code)
            if not result_analyzer.is_status_ok():
                raise Error(result_analyzer.get_error_message(),
                            result_analyzer.get_error_type(), None, None, self.__http_status_code)

            return True

        except Exception as e:
            # if isinstance(e, Error):
            #     raise
            # else:
            #     raise Error(str(e), 0, e, None, self.__http_status_code)
            self.__error = Error(str(e), 0, e, None, self.__http_status_code)
            return False

    def get_error(self) -> Error:
        """Returns the Error raised if the AceQL server servlet is not pingable."""
        return self.__error

    def get_response_time(self, sql: str) -> int:
        """Gets the response time of a SQL statement called on the remote database defined by the underlying
        Connection. """
        statement_parameters = {}
        begin = int(round(time.time() * 1000))
        self.__aceql_http_api.execute_query(sql, False, statement_parameters)
        end = int(round(time.time() * 1000))
        return end - begin

    def get_response_time_select_1(self, sql: str) -> int:
        """Gets the response time of a "select 1" called on the remote database defined by the underlying
        Connection. """
        return self.get_response_time("select 1");