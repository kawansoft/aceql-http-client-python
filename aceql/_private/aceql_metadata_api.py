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

import aceql._private.aceql_http_api
import marshmallow_dataclass

from aceql._private.dto.database_info_dto import DatabaseInfoDto
from aceql._private.result_analyzer import ResultAnalyzer
from aceql.error import Error

if TYPE_CHECKING:
    from aceql._private.aceql_http_api import AceQLHttpApi


class AceQLMetadataApi(object):
    """ AceQL HTTP wrapper for metadata apis. Takes care of all
    HTTP calls and operations."""
    __debug = False

    def __init__(self, aceQLHttpApi: 'AceQLHttpApi'):
        if aceQLHttpApi is None:
            raise TypeError("aceQLHttpApi is null!")
        self.__aceQLHttpApi = aceQLHttpApi
        self.__url = aceQLHttpApi.get_url()

    def get_database_info(self) -> DatabaseInfoDto:

        try:
            url_withaction = self.__url + "get_database_info"
            result = self.__aceQLHttpApi.call_with_get_url(url_withaction)

            result_analyzer = ResultAnalyzer(result, self.__aceQLHttpApi.get_http_status_code())
            if not result_analyzer.is_status_ok():
                raise Error(result_analyzer.get_error_message(),
                            result_analyzer.get_error_type(), None, None, self.__aceQLHttpApi.get_http_status_code())

            if AceQLMetadataApi.__debug:
                print(result)

            holder_database_info_dto_schema = marshmallow_dataclass.class_schema(DatabaseInfoDto)
            database_info_dto: DatabaseInfoDto = holder_database_info_dto_schema().loads(
                result)

            if AceQLMetadataApi.__debug:
                print(database_info_dto)

            print(database_info_dto)
            return database_info_dto;

        except Exception as e:
            if isinstance(e, Error):
                raise
            else:
                raise Error(str(e), 0, e, None, self.__aceQLHttpApi.get_http_status_code())