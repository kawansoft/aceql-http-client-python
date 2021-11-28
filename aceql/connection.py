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
from datetime import datetime
from aceql._private.aceql_http_api import AceQLHttpApi
from aceql._private.connection_util import ConnectionUtil
from aceql.cursor import Cursor
from aceql.connection_options import ConnectionOptions
from aceql.progress_indicator import ProgressIndicator
from aceql.login_url_decoder import LoginUrlDecoder

from aceql._private.dto.database_info_dto import DatabaseInfoDto
from aceql.database_info import DatabaseInfo


class Connection(object):
    """Allows to create a database connection to a remote server."""

    def __init__(self, *, url: str, username: str= None, password: str = None, database: str = None,
                 connection_options: ConnectionOptions = None):
        """
        Creates a database connection to the remote AceQL HTTP server.

        Parameters
        ----------
        url : str
            The URL of the AceQL server. Example: https://www.acme.com:9443/aceql.
            The URL may includes all parameters:
            https://www.acme.com:9443/acel?username=my_name&password=my_passwd&database=my_db
        username : str
            The authentication username.
        password : str
            the authentication password.
        database : str
            The remote database name.
            the  supplemental Connection Options (Container that allows define some options: proxies,
            timeout, request headers, etc.)

        Returns
        -------
        Connection
            A connection to the remote database.
        """

        if url is None:
            raise TypeError("url is null!")

        url_connection = LoginUrlDecoder(url)
        if "?" in url:
            url = url_connection.server_url
            if url_connection.username is not None:
                username = url_connection.username
            if url_connection.password is not None:
                password = url_connection.password
            if url_connection.database is not None:
                database = url_connection.database

        if username is None:
            raise TypeError("username is null!")
        if password is None:
            if connection_options is None:
                raise TypeError("password and connection_options cannot be both null!")
            if connection_options.session_id is None:
                raise TypeError("password and connection_options.session_id cannot be both null!")
        if database is None:
            raise TypeError("database is null!")

        self.__url = url
        self.__username = username
        self.__database = database

        self.__aceQLHttpApi = AceQLHttpApi(url=url, username=username, password=password, database=database,
                                           connection_options=connection_options)
        self.__connection_options = connection_options
        self.__creation_datetime = datetime.now()

    @property
    def _get_aceql_http_api(self) -> AceQLHttpApi:
        return self.__aceQLHttpApi

    def get_url(self) -> str :
        """Gets the Serverl URL for this Connection."""
        return self.__url

    def get_username(self) -> str :
        """Gets the username for this Connection."""
        return self.__username

    def get_database(self) -> str :
        """Gets the database for this Connection."""
        return self.__database

    def get_creation_datetime(self) -> datetime :
        """Gets the creation date and time for this Connection."""
        return self.__creation_datetime

    def get_connections_options(self) -> ConnectionOptions:
        """Gets the Connections options."""
        return self.__connection_options

    def cursor(self) -> Cursor:
        """Instantiates and returns a cursor."""
        cursor = Cursor(self, self.__aceQLHttpApi)
        return cursor

    def set_progress_indicator(self, progress_indicator: ProgressIndicator):
        """Allows to set a progress indicator."""
        self.__aceQLHttpApi.set_progress_indicator(progress_indicator)

    def get_progress_indicator(self) -> ProgressIndicator:
        """Returns the progress indicator in use."""
        return self.__aceQLHttpApi.get_progress_indicator()

    def set_auto_commit(self, auto_commit: bool):
        """Sets this connection's auto-commit mode to the given state."""
        self.__aceQLHttpApi.set_auto_commit(auto_commit)

    def get_auto_commit(self):
        """Retrieves the current auto-commit mode."""
        return self.__aceQLHttpApi.get_auto_commit()

    def commit(self):
        """Commit current transaction."""
        self.__aceQLHttpApi.commit()

    def rollback(self):
        """Rollback current transaction."""
        self.__aceQLHttpApi.rollback()

    def _trace(self):
        """Print empty line on trace."""
        self.__aceQLHttpApi.trace("")

    def trace(self, s: str):
        """Prints the string on trace."""
        self.__aceQLHttpApi.trace(s)

    @staticmethod
    def _is_trace_on() -> bool:
        """Says if trace is on."""
        return AceQLHttpApi.is_trace_on()

    @staticmethod
    def _set_trace_on(trace_on: bool):
        """Sets the trace on/off."""
        AceQLHttpApi.set_trace_on(trace_on)

    def get_server_version(self) -> str:
        """Gets the server version of AceQL HTTP."""
        return self.__aceQLHttpApi.get_server_version()

    def get_database_info(self) -> DatabaseInfo:
        """Get the the remote database and remote JDBC Driver basic info"""

        if not ConnectionUtil.is_get_database_info_supported(self):
            raise Exception("AceQL Server version must be >= " + ConnectionUtil.GET_DATABASE_INFO_MIN_SERVER_VERSION
                + " in order to call get_database_info.")

        database_info_dto: DatabaseInfoDto = self.__aceQLHttpApi.get_database_info()
        databaseInfo: DatabaseInfo = DatabaseInfo(database_info_dto)
        return databaseInfo

    def close(self):
        """Closes the connection to the remote database but keeps the HTTP session."""
        self.__aceQLHttpApi.close()

    def logout(self):
        """Closes all the connection to the remote database and closes the HTTP session."""
        self.__aceQLHttpApi.logout()

    def get_transaction_isolation(self) -> str:
        """Returns the current transaction isolation level."

           Will be one of the following constants:
                transaction_read_uncommitted,
                transaction_read_committed,
                transaction_repeatable_read,
                transaction_serializable, or
                transaction_none.
        """
        return self.__aceQLHttpApi.get_transaction_isolation()

    def set_transaction_isolation(self, level: str):
        """Sets the transaction isolation level."""
        self.__aceQLHttpApi.set_transaction_isolation(level)

    def get_holdability(self) -> str:
        """Returns the holdability.
         One of hold_cursors_over_commit or close_cursors_at_commit.
        """
        return self.__aceQLHttpApi.get_holdability()

    def set_holdability(self, holdability: str):
        """Sets the holdability."""
        self.__aceQLHttpApi.set_holdability(holdability)

    def is_read_only(self) -> bool:
        """Says if Connection is read-only."""
        return self.__aceQLHttpApi.is_read_only()

    def set_read_only(self, read_only: bool):
        """Allows to put Connection read-only mode."""
        self.__aceQLHttpApi.set_read_only(read_only)

    @staticmethod
    def get_client_version() -> str:
        """Gets the AceQL Cient SDK version."""
        return AceQLHttpApi.get_client_version()

    @staticmethod
    def get_client_version_full() -> str:
        """Gets the AceQL Cient SDK version with the Python version."""
        return AceQLHttpApi.get_client_version_full()
