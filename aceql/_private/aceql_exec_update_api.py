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
from typing import TYPE_CHECKING

import requests
from requests import Request

from aceql._private.aceql_debug import AceQLDebug
from aceql._private.aceql_execution_util import AceQLExecutionUtil
from aceql._private.result_analyzer import ResultAnalyzer
from aceql.error import Error

if TYPE_CHECKING:
    from aceql._private.aceql_http_api import AceQLHttpApi


class AceQLExecUpdateApi(object):
    """ AceQL HTTP wrapper for /execute_update API. Takes care of all
    HTTP calls and operations."""
    __debug = False

    def __init__(self, aceQLHttpApi: 'AceQLHttpApi'):
        if aceQLHttpApi is None:
            raise TypeError("aceQLHttpApi is null!")
        self.__aceQLHttpApi = aceQLHttpApi
        self.__url = aceQLHttpApi.get_url()

    # *
    # * Calls /execute_update API
    # *
    # * @param sql
    # * an SQL <code>INSERT</code>, <code>UPDATE</code> or
    # * <code>DELETE</code> statement or an SQL statement that returns
    # * nothing
    # * @param isPreparedStatement
    # * if true, the server will generate a prepared statement, else a
    # * simple statement
    # * @param statementParameters
    # * the statement parameters in JSON format.  Maybe null for simple
    # * statement call.
    # * @return either the row count for <code>INSERT</code>, <code>UPDATE</code>
    # * or <code>DELETE</code> statements, or <code>0</code> for SQL
    # * statements that return nothing
    # * @
    # * if any Exception occurs
    #
    def execute_update(self, sql: str, is_prepared_statement: bool, statement_parameters: dict):
        """Calls /execute_update API"""

        try:
            action = "execute_update"
            AceQLExecutionUtil.check_values(is_prepared_statement, sql)
            dict_params: dict = {"sql": sql}

            AceQLExecutionUtil.set_is_prepared_statement(dict_params, is_prepared_statement)
            url_withaction = self.__url + action

            AceQLDebug.debug("url_withaction: " + url_withaction)
            AceQLDebug.debug("dict_params 1: " + str(dict_params))

            if statement_parameters is not None:
                if not isinstance(statement_parameters, dict):
                    raise TypeError("statement_parameters is not a dictionary!")

                dict_params.update(statement_parameters)

            AceQLDebug.debug("dictParams 2: " + str(dict_params))

            # r = requests.post('http://httpbin.org/post', data = {'key':'value'})
            # print("Before update request")

            if self.__aceQLHttpApi.get_timeout() is None:
                AceQLDebug.debug("UPDATE HERE 1")
                response: Request = requests.post(url_withaction, headers=self.__aceQLHttpApi.get_headers(), data=dict_params,
                                                  proxies=self.__aceQLHttpApi.get_proxies(),
                                                  auth=self.__aceQLHttpApi.get_auth())
            else:
                AceQLDebug.debug("UPDATE HERE 2")
                response: Request = requests.post(url_withaction, headers=self.__aceQLHttpApi.get_headers(), data=dict_params,
                                                  proxies=self.__aceQLHttpApi.get_proxies(),
                                                  auth=self.__aceQLHttpApi.get_auth(),
                                                  timeout=self.__aceQLHttpApi.get_timeout())

            self.__aceQLHttpApi.set_http_status_code(response.status_code)
            result = response.text

            # print("self.__http_status_code: " + str(self.__http_status_code ))
            # print("result                 : " + str(result))
            AceQLDebug.debug("result: " + result)

            result_analyzer = ResultAnalyzer(result, self.__aceQLHttpApi.get_http_status_code())
            if not result_analyzer.is_status_ok():
                raise Error(result_analyzer.get_error_message(),
                            result_analyzer.get_error_type(), None, None, self.__aceQLHttpApi.get_http_status_code())

            row_count = result_analyzer.get_int_value("row_count")
            return row_count

        except Exception as e:
            if isinstance(e, Error):
                raise
            else:
                raise Error(str(e), 0, e, None, self.__aceQLHttpApi.get_http_status_code())

