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
from typing import List, TYPE_CHECKING

import marshmallow_dataclass
import requests
from requests import Request

from aceql._private.batch.update_counts_array_dto import UpdateCountsArrayDto
from aceql._private.aceql_debug import AceQLDebug
from aceql._private.result_analyzer import ResultAnalyzer
from aceql.error import Error

if TYPE_CHECKING:
    from aceql._private.aceql_http_api import AceQLHttpApi


class AceQLBatchApi(object):
    """ AceQL HTTP wrapper for metadata apis. Takes care of all
    HTTP calls and operations."""
    __debug = False

    def __init__(self, aceQLHttpApi: 'AceQLHttpApi'):
        if aceQLHttpApi is None:
            raise TypeError("aceQLHttpApi is null!")
        self.__aceQLHttpApi = aceQLHttpApi
        self.__url = aceQLHttpApi.get_url()

    def execute_batch(self, sql: str, batch_file_parameters: str):

        try:
            action = "prepared_statement_execute_batch"
            AceQLBatchApi.check_values(True, sql)
            url_withaction = self.__url + action

            AceQLDebug.debug("url_withaction: " + url_withaction)

            blob_id: str = os.path.basename(batch_file_parameters)
            length: int = os.path.getsize(batch_file_parameters)

            with open(batch_file_parameters, "rb") as fd:
                self.__aceQLHttpApi.blob_upload(blob_id, fd, length)

            dict_params: dict = {"sql": sql, "blob_id": blob_id}
            AceQLDebug.debug("dict_params: " + str(dict_params))

            # r = requests.post('http://httpbin.org/post', data = {'key':'value'})
            # print("Before update request")

            # if self.__timeout is None:
            #     response: Request = requests.post(url_withaction, headers=self.__headers, data=dict_params,
            #                                       proxies=self.__proxies, auth=self.__auth)
            # else:
            #     response: Request = requests.post(url_withaction, headers=self.__headers, data=dict_params,
            #                                       proxies=self.__proxies, auth=self.__auth,
            #                                       timeout=self.__timeout)

            if self.__aceQLHttpApi.get_timeout() is None:
                response: Request = requests.post(url_withaction, headers=self.__aceQLHttpApi.get_headers(), data=dict_params,
                                                  proxies=self.__aceQLHttpApi.get_proxies(),
                                                  auth=self.__aceQLHttpApi.get_auth())
            else:
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

            update_counts_array_dto_schema = marshmallow_dataclass.class_schema(UpdateCountsArrayDto)
            update_counts_array_dto_back: UpdateCountsArrayDto = update_counts_array_dto_schema().loads(
                result)

            update_counts_array: List[int] = update_counts_array_dto_back.updateCountsArray
            return update_counts_array
        except Exception as e:
            if isinstance(e, Error):
                raise
            else:
                raise Error(str(e), 0, e, None, self.__aceQLHttpApi.get_http_status_code())

    @staticmethod
    def check_values(is_prepared_statement: bool, sql: str):
        if sql is None:
            raise TypeError("sql is null!")
        if is_prepared_statement is None:
            raise TypeError("isPreparedStatement is null!")