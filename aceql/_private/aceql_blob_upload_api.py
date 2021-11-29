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

import sys
from typing import List, TYPE_CHECKING

import requests
from requests import Request
from requests_toolbelt.multipart import encoder

if TYPE_CHECKING:
    from aceql._private.aceql_http_api import AceQLHttpApi


class AceQLBlobUploadApi(object):
    """ AceQL HTTP wrapper for Blob upload API. Takes care of all
    HTTP calls and operations."""
    __debug = False

    def __init__(self, aceQLHttpApi: 'AceQLHttpApi'):
        if aceQLHttpApi is None:
            raise TypeError("aceQLHttpApi is null!")
        self.__aceQLHttpApi = aceQLHttpApi
        self.__url = aceQLHttpApi.get_url()

        self.__temp_length = 0
        self.__total_length = 0

    def blob_upload(self, blob_id: str, fd, total_length: int):
        """ Upload the BLOB and use a callback function for progress indicator. """

        self.__total_length = total_length

        # fields={'field0': 'value', 'field1': 'value',
        # 'field2': ('filename', open('file.py', 'rb'), 'text/plain')}

        the_fields: dict = dict()
        the_fields["blob_id"] = blob_id
        the_fields["file"] = ("filename", fd, "application/octet-stream")

        e = encoder.MultipartEncoder(fields=the_fields)
        m = encoder.MultipartEncoderMonitor(e, self.my_callback)

        the_headers = dict(self.__aceQLHttpApi.get_headers())  # or orig.copy()
        the_headers["Content-Type"] = m.content_type

        the_url = self.__url + "blob_upload"
        # requests.post(the_url, data=m, headers={'Content-Type': m.content_type}, proxies=self.__proxies,
        #              auth=self.__auth)

        # requests.post(the_url, data=m, headers=the_headers, proxies=self.__proxies,
        #               auth=self.__auth)
        requests.post(the_url, data=m, headers=the_headers, proxies=self.__aceQLHttpApi.get_proxies(),
                      auth=self.__aceQLHttpApi.get_auth())

    def my_callback(self, monitor):
        """ The callback function when uploading a BLOB """
        try:
            if self.__total_length == 0 or self.__aceQLHttpApi.get_progress_indicator() is None:
                return

            the_read = monitor.bytes_read

            self.__temp_length += the_read
            if self.__temp_length >= self.__total_length / 100:
                self.__temp_length = 0
                self.__aceQLHttpApi.get_progress_indicator() ._increment()

        except Exception as e:
            print(str(e))