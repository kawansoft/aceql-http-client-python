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

import marshmallow_dataclass
import requests
from requests import Request

from aceql._private.dto.database_info_dto import DatabaseInfoDto
from aceql._private.dto.jdbc_database_meta_data_dto import JdbcDatabaseMetaDataDto
from aceql._private.dto.limits_info_dto import LimitsInfoDto
from aceql._private.dto.table_dto import TableDto
from aceql._private.dto.table_names_dto import TableNamesDto
from aceql._private.http_client_with_retry import HTTPClientWithRetry
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

    def db_schema_download(self, file_format: str, table_name: str):
        """ returns a schema stream as a Requests response """
        try:
            if file_format is None:
                raise TypeError("format is null!")

            the_url = self.__url + "/metadata_query/db_schema_download"

            dict_params = {"format": file_format}

            if table_name is not None:
                table_name = table_name.lower()
                dict_params["table_name"] = table_name

            if self.__aceQLHttpApi.get_timeout() is None:
                response: Request = HTTPClientWithRetry.post(the_url, headers=self.__aceQLHttpApi.get_headers(), data=dict_params,
                                                  proxies=self.__aceQLHttpApi.get_proxies(),
                                                  auth=self.__aceQLHttpApi.get_auth())
            else:
                response: Request = HTTPClientWithRetry.post(the_url, headers=self.__aceQLHttpApi.get_headers(), data=dict_params,
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

    def get_table_names(self, table_type: str) -> TableNamesDto:
        try:
            url_withaction = self.__url + "metadata_query/get_table_names"

            if table_type is not None:
                url_withaction += "?table_type=" + table_type

            result = self.__aceQLHttpApi.call_with_get_url(url_withaction)

            result_analyzer = ResultAnalyzer(result, self.__aceQLHttpApi.get_http_status_code())
            if not result_analyzer.is_status_ok():
                raise Error(result_analyzer.get_error_message(),
                            result_analyzer.get_error_type(), None, None, self.__aceQLHttpApi.get_http_status_code())

            if AceQLMetadataApi.__debug:
                print(result)

            table_names_dto_schema = marshmallow_dataclass.class_schema(TableNamesDto)
            table_names_dto: TableNamesDto = table_names_dto_schema().loads(result)

            if AceQLMetadataApi.__debug:
                print(table_names_dto)

            return table_names_dto

        except Exception as e:
            if isinstance(e, Error):
                raise
            else:
                raise Error(str(e), 0, e, None, self.__aceQLHttpApi.get_http_status_code())

    def get_table(self, name: str) -> TableDto:
        try:
            url_withaction = self.__url + "metadata_query/get_table"

            if name is None:
                raise TypeError("name is null!")
            url_withaction += "?table_name=" + name

            result = self.__aceQLHttpApi.call_with_get_url(url_withaction)

            if AceQLMetadataApi.__debug:
                print(result)

            result_analyzer = ResultAnalyzer(result, self.__aceQLHttpApi.get_http_status_code())
            if not result_analyzer.is_status_ok():
                raise Error(result_analyzer.get_error_message(),
                            result_analyzer.get_error_type(), None, None, self.__aceQLHttpApi.get_http_status_code())

            table_dto_schema = marshmallow_dataclass.class_schema(TableDto)
            table_dto: TableDto = table_dto_schema().loads(result)

            if AceQLMetadataApi.__debug:
                print(table_dto)

            return table_dto

        except Exception as e:
            if isinstance(e, Error):
                raise
            else:
                raise Error(str(e), 0, e, None, self.__aceQLHttpApi.get_http_status_code())

    def get_db_metadata(self) -> JdbcDatabaseMetaDataDto:
        try:
            url_withaction = self.__url + "metadata_query/get_db_metadata"
            result = self.__aceQLHttpApi.call_with_get_url(url_withaction)

            result_analyzer = ResultAnalyzer(result, self.__aceQLHttpApi.get_http_status_code())
            if not result_analyzer.is_status_ok():
                raise Error(result_analyzer.get_error_message(),
                            result_analyzer.get_error_type(), None, None, self.__aceQLHttpApi.get_http_status_code())

            if AceQLMetadataApi.__debug:
                print(result)

            holder_jdbc_database_meta_data_schema = marshmallow_dataclass.class_schema(JdbcDatabaseMetaDataDto)
            jdbc_database_meta_data_holder: JdbcDatabaseMetaDataDto = holder_jdbc_database_meta_data_schema().loads(
                result)

            if AceQLMetadataApi.__debug:
                print(jdbc_database_meta_data_holder)

            return jdbc_database_meta_data_holder

        except Exception as e:
            if isinstance(e, Error):
                raise
            else:
                raise Error(str(e), 0, e, None, self.__aceQLHttpApi.get_http_status_code())

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

            return database_info_dto;

        except Exception as e:
            if isinstance(e, Error):
                raise
            else:
                raise Error(str(e), 0, e, None, self.__aceQLHttpApi.get_http_status_code())

    def get_limits_info(self) -> LimitsInfoDto:

        try:
            url_withaction = self.__url + "get_limits_info"
            result = self.__aceQLHttpApi.call_with_get_url(url_withaction)

            result_analyzer = ResultAnalyzer(result, self.__aceQLHttpApi.get_http_status_code())
            if not result_analyzer.is_status_ok():
                raise Error(result_analyzer.get_error_message(),
                            result_analyzer.get_error_type(), None, None, self.__aceQLHttpApi.get_http_status_code())

            if AceQLMetadataApi.__debug:
                print(result)

            holder_limits_info_dto_schema = marshmallow_dataclass.class_schema(LimitsInfoDto)
            limits_info_dto: LimitsInfoDto = holder_limits_info_dto_schema().loads(
                result)

            if AceQLMetadataApi.__debug:
                print(limits_info_dto)

            return limits_info_dto;

        except Exception as e:
            if isinstance(e, Error):
                raise
            else:
                raise Error(str(e), 0, e, None, self.__aceQLHttpApi.get_http_status_code())