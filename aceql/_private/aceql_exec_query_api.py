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
import os
from typing import TYPE_CHECKING

import requests
from requests import Request

from aceql._private.aceql_debug_parms import AceQLDebugParms
from aceql._private.cursor_util import CursorUtil
from aceql._private.file_util import FileUtil
from aceql._private.result_set_info import ResultSetInfo
from aceql._private.row_counter import RowCounter
from aceql._private.stream_result_analyzer import StreamResultAnalyzer
from aceql.error import Error
from aceql._private.aceql_debug import AceQLDebug
from aceql._private.aceql_execution_util import AceQLExecutionUtil

if TYPE_CHECKING:
    from aceql._private.aceql_http_api import AceQLHttpApi


class AceQLExecQueryApi(object):
    """ AceQL HTTP wrapper for /execute_update API. Takes care of all
    HTTP calls and operations."""
    __debug = False

    def __init__(self, aceQLHttpApi: 'AceQLHttpApi'):
        if aceQLHttpApi is None:
            raise TypeError("aceQLHttpApi is null!")
        self.__aceQLHttpApi = aceQLHttpApi
        self.__url = aceQLHttpApi.get_url()

    # *
    # * Calls /execute_query API
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
    # * @return the input stream containing either an error, or the result set in
    # * JSON format.  See user documentation.
    # * @
    # * if any Exception occurs

    def execute_query(self, sql: str, is_prepared_statement: bool, statement_parameters: dict):
        """Calls /execute_query API"""
        try:

            action = "execute_query"
            AceQLExecutionUtil.check_values(is_prepared_statement, sql)
            dict_params = {"sql": sql}
            AceQLExecutionUtil.set_is_prepared_statement(dict_params, is_prepared_statement)

            url_withaction = self.__url + action

            AceQLDebug.debug("url_withaction: " + url_withaction)
            AceQLDebug.debug("dictParams 1: " + str(dict_params))

            if statement_parameters is not None:
                if not isinstance(statement_parameters, dict):
                    raise TypeError("statementParameters is not a dictionary!")

                dict_params.update(statement_parameters)

            self.update_dict_params(dict_params)

            AceQLDebug.debug("dictParams 2: " + str(dict_params))

            # r = requests.post('http://httpbin.org/post', data = {'key':'value'})

            if self.__aceQLHttpApi.get_timeout() is None:
                AceQLDebug.debug("QUERY HERE 1")
                response: Request = requests.post(url_withaction,
                                                  headers=self.__aceQLHttpApi.get_headers(),
                                                  data=dict_params,
                                                  proxies=self.__aceQLHttpApi.get_proxies(),
                                                  auth=self.__aceQLHttpApi.get_auth())
            else:
                AceQLDebug.debug("QUERY HERE 2")
                response: Request = requests.post(url_withaction,
                                                  headers=self.__aceQLHttpApi.get_headers(),
                                                  data=dict_params,
                                                  proxies=self.__aceQLHttpApi.get_proxies(),
                                                  auth=self.__aceQLHttpApi.get_auth(),
                                                  timeout=self.__aceQLHttpApi.get_timeout())
            AceQLDebug.debug("DONE!")
            self.__aceQLHttpApi.set_http_status_code(response.status_code)

            filename = FileUtil.build_result_set_file()
            AceQLDebug.debug("filename1: " + filename)

            # We dump the JSon stream into user.home/.kawansoft/tmp
            with open(filename, 'wb') as fd:
                for chunk in response.iter_content(chunk_size=2048):
                    fd.write(chunk)

            AceQLDebug.debug("after open filename")
            result_set_info = self.treat_result(filename)
            return result_set_info

        except Exception as e:
            if isinstance(e, Error):
                raise
            else:
                raise Error(str(e), 0, e, None, self.__aceQLHttpApi.get_http_status_code())

    def treat_result(self, filename: str):
        file_out = None
        if self.__aceQLHttpApi.is_gzip_result():
            file_out = filename[0: len(filename) - 4] + ".ungzipped.txt"
            FileUtil.decompress(filename, file_out)
            if AceQLDebugParms.DELETE_FILES:
                CursorUtil.remove_file_safe(filename)
        else:
            file_out = filename
        AceQLDebug.debug("Before StreamResultAnalyzer")
        result_analyzer = StreamResultAnalyzer(file_out, self.__aceQLHttpApi.get_http_status_code())
        if not result_analyzer.is_status_ok():
            if AceQLDebugParms.DELETE_FILES:
                CursorUtil.remove_file_safe(filename)
            raise Error(result_analyzer.get_error_message(),
                        result_analyzer.get_error_type(), None, None, self.__aceQLHttpApi.get_http_status_code())
        row_counter = RowCounter(file_out)
        row_count = row_counter.count()
        result_set_info = ResultSetInfo(file_out, row_count)
        AceQLDebug.debug("Before resultSetInfo")
        return result_set_info

    def update_dict_params(self, dict_params: dict):
        if self.__aceQLHttpApi.is_gzip_result() :
            dict_params["gzip_result"] = "true"
        if self.__aceQLHttpApi.is_pretty_printing():
            dict_params["pretty_printing"] = "true"
        # Force pretty printing to True because parser needs it
        dict_params["pretty_printing"] = "true"
        # We need the types
        dict_params["column_types"] = "true"
