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
from typing import List

import requests
from requests import Request

import aceql._private.aceql_batch_api
import aceql._private.aceql_blob_api
import aceql._private.aceql_blob_upload_api
import aceql._private.aceql_exec_query_api
import aceql._private.aceql_exec_update_api
import aceql._private.aceql_metadata_api
from aceql._private.dto.database_info_dto import DatabaseInfoDto
from aceql._private.dto.jdbc_database_meta_data_dto import JdbcDatabaseMetaDataDto
from aceql._private.dto.table_dto import TableDto
from aceql._private.dto.table_names_dto import TableNamesDto
from aceql._private.result_analyzer import ResultAnalyzer
from aceql._private.user_login_store import UserLoginStore
from aceql._private.version_values import VersionValues
from aceql.connection_options import ConnectionOptions
from aceql.error import Error
from aceql.progress_indicator import ProgressIndicator
from aceql.proxy_auth import ProxyAuth


class AceQLHttpApi(object):
    """ AceQL HTTP wrapper for all apis. Takes care of all
    HTTP calls and operations."""

    __trace_on = False
    __debug = False

    def __init__(self, *, url: str, username: str, password: str, database: str,
                 connection_options: ConnectionOptions = None):

        if url is None:
            raise TypeError("url is null!")
        if database is None:
            raise TypeError("database is null!")
        if username is None:
            raise TypeError("username is null!")

        session_id: str = None
        proxies: dict = None
        auth: ProxyAuth = None
        gzip_result: bool = True
        timeout = None
        request_headers: dict = {}

        if connection_options is not None:
            if connection_options.session_id is not None:
                session_id = connection_options.session_id
                password = None
            proxies = connection_options.proxies
            auth = connection_options.auth
            gzip_result = connection_options.gzip_result
            timeout = connection_options.timeout
            request_headers = connection_options.request_headers

        self.__url = url
        self.__database = database
        self.__username = username
        self.__password = password
        self.__proxies = proxies
        self.__auth = auth
        self.__gzip_result = gzip_result
        self.__timeout = timeout
        self.__headers = request_headers
        self.__http_status_code = requests.codes.ok

        # Other self for other methods
        self.__pretty_printing = True
        #self.__temp_length = 0  ==> Done in AceQLBlobUploadApi
        #self.__total_length = 0 ==> ==> Done in AceQLBlobUploadApi
        self.__progress_indicator = None

        # url = c + "/database/" + database + "/username/" \
        #       + username + "/connect" + "?password=" \
        #       + password
        user_login_store = UserLoginStore(url, username, database)

        if session_id is not None:
            user_login_store.set_session_id(session_id);

        try:
            if user_login_store.is_already_logged():
                session_id = user_login_store.get_session_id()
                the_url = url + "/session/" + session_id + "/get_connection";

                result = self.call_with_get_url(the_url)

                result_analyzer = ResultAnalyzer(result, self.__http_status_code)
                if not result_analyzer.is_status_ok():
                    raise Error(result_analyzer.get_error_message(),
                                result_analyzer.get_error_type(), None, None, self.__http_status_code)

                connection_id = result_analyzer.get_value("connection_id");
                self.__url = url + "/session/" + session_id + "/connection/" + connection_id + "/";

            else:
                url = url + "/database/" + database + "/username/" \
                      + username + "/login"

                dict_params = {"password": password, "client_version": str(VersionValues.VERSION)}

                result = self.call_with_post_url(url, dict_params)

                result_analyzer = ResultAnalyzer(result, self.__http_status_code)
                if not result_analyzer.is_status_ok():
                    raise Error(result_analyzer.get_error_message(),
                                result_analyzer.get_error_type(), None, None, self.__http_status_code)

                session_id = result_analyzer.get_value("session_id")
                connection_id = result_analyzer.get_value("connection_id");
                self.__url = url + "/session/" + session_id + "/connection/" + connection_id + "/"

                user_login_store.set_session_id(session_id);
        except Exception as e:
            if isinstance(e, Error):
                raise
            else:
                raise Error(str(e), 0, e, None, self.__http_status_code)

    def set_progress_indicator(self, progress_indicator: ProgressIndicator):
        self.__progress_indicator = progress_indicator

    def get_progress_indicator(self) -> ProgressIndicator:
        return self.__progress_indicator

    def call_with_get_url(self, url: str) -> str:
        if self.__timeout is None:
            response: Request = requests.get(url, headers=self.__headers, proxies=self.__proxies, auth=self.__auth)
        else:
            response: Request = requests.get(url, headers=self.__headers, proxies=self.__proxies, auth=self.__auth,
                                             timeout=self.__timeout)

        self.__http_status_code = response.status_code
        return response.text

    def call_with_post_url(self, url: str, dict_params: dict) -> str:

        if self.__timeout is None:
            response: Request = requests.post(url, headers=self.__headers, data=dict_params, proxies=self.__proxies,
                                              auth=self.__auth)
        else:
            response: Request = requests.post(url, headers=self.__headers, data=dict_params, proxies=self.__proxies,
                                              auth=self.__auth,
                                              timeout=self.__timeout)

        self.__http_status_code = response.status_code

        return response.text

    def call_with_get_action(self, action: str, action_parameter: dict) -> str:
        url_withaction = self.__url + action

        if AceQLHttpApi.__debug:
            print("url_withaction: " + url_withaction)

        if action_parameter is not None and len(action_parameter) > 1:
            url_withaction += "/" + action_parameter

        return self.call_with_get_url(url_withaction)

    def call_api_with_result(self, command_name: str, command_option: str):
        if command_name is None:
            raise TypeError("command_name is null!")

        try:
            result = self.call_with_get_action(command_name, command_option)

            result_analyzer = ResultAnalyzer(result, self.__http_status_code)
            if not result_analyzer.is_status_ok():
                raise Error(result_analyzer.get_error_message(),
                            result_analyzer.get_error_type(), None, None, self.__http_status_code)

            return result_analyzer.get_result_default()

        except Exception as e:
            if isinstance(e, Error):
                raise
            else:
                raise Error(str(e), 0, e, None, self.__http_status_code)

    def call_api_no_result(self, command_name: str, command_option: str):
        if command_name is None:
            raise TypeError("command_name is null!")

        try:
            result = self.call_with_get_action(command_name, command_option)

            result_analyzer = ResultAnalyzer(result, self.__http_status_code)
            if not result_analyzer.is_status_ok():
                raise Error(result_analyzer.get_error_message(),
                            result_analyzer.get_error_type(), None, None, self.__http_status_code)

        except Exception as e:
            if isinstance(e, Error):
                raise
            else:
                raise Error(str(e), 0, e, None, self.__http_status_code)

    def set_auto_commit(self, auto_commit: bool):
        auto_commit_str = str(auto_commit)

        if auto_commit_str == "True":
            auto_commit_str = "true"
        else:
            auto_commit_str = "false"

        self.call_api_no_result("set_auto_commit", auto_commit_str)

    def get_auto_commit(self) -> bool:
        is_auto_commit_str = self.call_api_with_result("get_auto_commit", None)
        if is_auto_commit_str == "true":
            return True
        else:
            return False

    def commit(self):
        self.call_api_no_result("commit", None)

    def rollback(self):
        self.call_api_no_result("rollback", None)

    @staticmethod
    def trace(s: str):
        if AceQLHttpApi.__trace_on:
            print(s)

    @staticmethod
    def is_trace_on() -> bool:
        """Says if trace is on"""
        return AceQLHttpApi.__trace_on

    @staticmethod
    def set_trace_on(trace_on: bool):
        """Sets the trace on/off"""
        AceQLHttpApi.__trace_on = trace_on

    def is_gzip_result(self) -> bool:
        """Says the query result is returned compressed with the GZIP file format."""
        return self.__gzip_result

    def set_gzip_result(self, gzip_result: bool):
        """Define if result sets are compressed before download.  Defaults to true."""
        if str(gzip_result) == 'True':
            self.__gzip_result = True
        else:
            self.__gzip_result = False

    def get_server_version(self) -> str:
        """Calls /get_version API"""
        the_version = self.call_api_with_result("get_version", None)
        return the_version

    @staticmethod
    def get_client_version() -> str:
        """Gets the SDK version"""
        return VersionValues.NAME + " - " + VersionValues.VERSION + " - " + VersionValues.DATE

    @staticmethod
    def get_client_version_full() -> str:
        """Gets the SDK version + Python version"""
        return AceQLHttpApi.get_client_version() + " - " + sys.version

    def close(self):
        """Calls /close API"""
        self.call_api_no_result("close", None)

    def logout(self):
        """Calls /logout API"""
        user_login_store = UserLoginStore(self.__url, self.__username, self.__database)
        user_login_store.remove_store()
        self.call_api_no_result("logout", None)

    def get_transaction_isolation(self) -> str:
        """Calls /get_transaction_isolation_level API"""
        transaction_isolation = self.call_api_with_result("get_transaction_isolation_level", None)
        return transaction_isolation

    def set_transaction_isolation(self, level: str):
        """Calls /set_transaction_isolation_level API"""
        self.call_api_no_result("set_transaction_isolation_level", level)

    def get_holdability(self) -> str:
        """Calls /get_holdability API"""
        holdability = self.call_api_with_result("get_holdability", None)
        return holdability

    def set_holdability(self, holdability: str):
        """Calls /set_holdability API"""
        self.call_api_no_result("set_holdability", holdability)

    def is_read_only(self) -> bool:
        """Calls /get_auto_commit API"""
        is_read_only_str = self.call_api_with_result("is_read_only", None)
        if is_read_only_str == "true":
            return True
        else:
            return False

    def set_read_only(self, read_only: bool):
        """Calls /set_read_only API"""
        if read_only is None:
            raise TypeError("read_only is null!")

        read_only_str = "false"

        if str(read_only) == "True":
            read_only_str = "true"

        self.call_api_no_result("set_read_only", read_only_str)

    def is_pretty_printing(self):
        return self.__pretty_printing

    def get_url(self) -> int:
        """returns the httpStatus"""
        return self.__url

    def get_headers(self):
        """returns the headers"""
        return self.__headers

    def get_proxies(self):
        """returns the proxies"""
        return self.__proxies

    def get_auth(self):
        """returns the auth"""
        return self.__auth

    def get_timeout(self):
        """returns the timeout"""
        return self.__timeout

    def get_http_status_code(self) -> int:
        """returns the httpStatus"""
        return self.__http_status_code

    def set_http_status_code(self, status_code):
        self.__http_status_code = status_code

    def get_http_status_message(self) -> str:
        """returns the httpStatusMessage"""
        status_messages = requests.status_codes.codes[self.__http_status_code]
        return status_messages[0]

    def add_request_headers(self, headers: dict):
        self.__headers = headers

    def reset_request_headers(self):
        self.__headers = {}

    def execute_server_query(self, server_query_executor_class_name: str, parameters: List):
        """Calls /execute_server_query API"""
        aceql_exec_query_api:  aceql.AceQLExecQueryApi = aceql._private.aceql_exec_query_api.AceQLExecQueryApi(self)
        return aceql_exec_query_api.execute_server_query(server_query_executor_class_name, parameters)

    def execute_query(self, sql: str, is_prepared_statement: bool, statement_parameters: dict):
        """Calls /execute_query API"""
        aceql_exec_query_api:  aceql.AceQLExecQueryApi = aceql._private.aceql_exec_query_api.AceQLExecQueryApi(self)
        return aceql_exec_query_api.execute_query(sql, is_prepared_statement, statement_parameters)

    def execute_update(self, sql: str, is_prepared_statement: bool, statement_parameters: dict):
        """Calls /execute_update API"""
        aceql_exec_update_api: aceql.AceQLExecUpdateApi = aceql._private.aceql_exec_update_api.AceQLExecUpdateApi(self)
        return aceql_exec_update_api.execute_update(sql, is_prepared_statement, statement_parameters)

    def blob_upload(self, blob_id: str, fd, total_length: int):
        """ Upload the BLOB and use a callback function for progress indicator."""
        aceql_blob_upload_api: aceql.AceQLBlobUploadApi = aceql._private.aceql_blob_upload_api.AceQLBlobUploadApi(self)
        aceql_blob_upload_api.blob_upload(blob_id, fd, total_length)

    def execute_batch(self, sql: str, batch_file_parameters: str):
        """Executes batch and return affected rows"""
        aceql_batch_api: aceql.AceQLBatchApi = aceql._private.aceql_batch_api.AceQLBatchApi(self)
        return aceql_batch_api.execute_batch(sql, batch_file_parameters)

    def get_blob_stream(self, blob_id: str) -> Request:
        """ returns a BLOB stream as a Requests response """
        aceql_blob_api: aceql.AceQLBlobApi = aceql._private.aceql_blob_api.AceQLBlobApi(self)
        return aceql_blob_api.get_blob_stream(blob_id)

    def get_blob_length(self, blob_id: str):
        """ returns a BLOB stream as a Requests response """
        aceql_blob_api: aceql.AceQLBlobApi = aceql._private.aceql_blob_api.AceQLBlobApi(self)
        aceql_blob_api.get_blob_length(blob_id)

    def db_schema_download(self, file_format: str, table_name: str):
        ace_ql_metadata_api: aceql.AceQLMetadataApi = aceql._private.aceql_metadata_api.AceQLMetadataApi(self)
        return ace_ql_metadata_api.db_schema_download(file_format, table_name)

    def get_table_names(self, table_type: str) -> TableNamesDto:
        ace_ql_metadata_api: aceql.AceQLMetadataApi = aceql._private.aceql_metadata_api.AceQLMetadataApi(self)
        return ace_ql_metadata_api.get_table_names(table_type)

    def get_table(self, name: str) -> TableDto:
        ace_ql_metadata_api: aceql.AceQLMetadataApi = aceql._private.aceql_metadata_api.AceQLMetadataApi(self)
        return ace_ql_metadata_api.get_table(name)

    def get_db_metadata(self) -> JdbcDatabaseMetaDataDto:
        ace_ql_metadata_api: aceql.AceQLMetadataApi = aceql._private.aceql_metadata_api.AceQLMetadataApi(self)
        return ace_ql_metadata_api.get_db_metadata()

    def get_database_info(self) -> DatabaseInfoDto:
        ace_ql_metadata_api: aceql.AceQLMetadataApi = aceql._private.aceql_metadata_api.AceQLMetadataApi(self)
        return ace_ql_metadata_api.get_database_info()
