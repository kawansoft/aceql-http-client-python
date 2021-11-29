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
from aceql._private.result_analyzer import ResultAnalyzer
from aceql.error import Error

if TYPE_CHECKING:
    from aceql._private.aceql_http_api import AceQLHttpApi


class AceQLBlobApi(object):
    """ AceQL HTTP wrapper for Blob download APIs. Takes care of all
    HTTP calls and operations."""
    __debug = False

    def __init__(self, aceQLHttpApi: 'AceQLHttpApi'):
        if aceQLHttpApi is None:
            raise TypeError("aceQLHttpApi is null!")
        self.__aceQLHttpApi = aceQLHttpApi
        self.__url = aceQLHttpApi.get_url()

    def get_blob_stream(self, blob_id: str) -> Request:
        """ returns a BLOB stream as a Requests response """
        try:

            if blob_id is None:
                raise TypeError("blob_id is null!")

            the_url = self.__url + "/blob_download?blob_id=" + blob_id

            if self.__aceQLHttpApi.get_timeout() is None:
                response: Request = requests.get(the_url, headers=self.__aceQLHttpApi.get_headers(),
                                                 proxies=self.__aceQLHttpApi.get_proxies(),
                                                 auth=self.__aceQLHttpApi.get_auth())
            else:
                response: Request = requests.get(the_url,  headers=self.__aceQLHttpApi.get_headers(),
                                                 proxies=self.__aceQLHttpApi.get_proxies(),
                                                 auth=self.__aceQLHttpApi.get_auth(),
                                                 timeout=self.__aceQLHttpApi.get_timeout())

            self.__aceQLHttpApi.set_http_status_code(response.status_code)
            return response

        except Exception as e:
            if isinstance(e, Error):
                raise
            else:
                raise Error(str(e), 0, e, None, self.__aceQLHttpApi.get_http_status_code())

    def get_blob_length(self, blob_id: str) -> int:
        """ Gets the blob length. """
        try:

            if blob_id is None:
                raise TypeError("blob_id is null!")

            action = "get_blob_length"

            dict_params: dict = {"blob_id": blob_id}

            url_withaction = self.__url + action

            AceQLDebug.debug("urlWithaction: " + url_withaction)
            AceQLDebug.debug("dictParams   : " + str(dict_params))

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

            AceQLDebug.debug("result: " + result)

            result_analyzer = ResultAnalyzer(result, self.__aceQLHttpApi.get_http_status_code())
            if not result_analyzer.is_status_ok():
                raise Error(result_analyzer.get_error_message(),
                            result_analyzer.get_error_type(), None, None, self.__aceQLHttpApi.get_http_status_code())

            length_str = result_analyzer.get_value("length")
            AceQLDebug.debug("result: " + length_str + ":")
            return int(length_str)

        except Exception as e:
            if isinstance(e, Error):
                raise
            else:
                raise Error(str(e), 0, e, None, self.__aceQLHttpApi.get_http_status_code())