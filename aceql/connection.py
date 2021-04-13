#
# This file is part of AceQL Python Client SDK.
# AceQL Python Client SDK: Remote SQL access over HTTP with AceQL HTTP.
# Copyright (C) 2020,  KawanSoft SAS
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
from aceql._private.aceql_http_api import AceQLHttpApi
from aceql.cursor import Cursor
from aceql.connection_options import ConnectionOptions
from aceql.proxy_auth import ProxyAuth
from aceql.progress_indicator import ProgressIndicator


class Connection(object):
    """Allows to create a database connection to a remote server."""

    def __init__(self, *, url: str, username: str, password: str, database: str,
                 connection_options: ConnectionOptions = None):
        """
        Creates a database connection to the remote AceQL HTTP server.

        Parameters
        ----------
        url : str
            The URL of the AceQL server. Example: https://www.acme.com:9443/aceql.
        username : str
            The authentication username.
        password : str
            the authentication password.
        database : str
            The remote database name.
        connection_options : ConnectionOptions
            the  supplemental Connection Options.

        Returns
        -------
        Connection
            A connection to the remote database.
        """

        if url is None:
            raise TypeError("url is null!")
        if username is None:
            raise TypeError("username is null!")
        if password is None:
            raise TypeError("password is null!")
        if database is None:
            raise TypeError("database is null!")

        self.__aceQLHttpApi = AceQLHttpApi(url, username, password, database, connection_options)
        self.__connection_options = connection_options

    @property
    def _get_aceql_http_api(self) -> AceQLHttpApi:
        return self.__aceQLHttpApi

    def getConnectionsOptions(self) -> ConnectionOptions:
        return self.____connection_options

    def cursor(self) -> Cursor:
        """Instantiates and returns a cursor."""
        cursor = Cursor(self, self.__aceQLHttpApi)
        return cursor

    def add_request_headers(self, headers: dict):
        """Allows to pass a dictionary of headers to each request."""
        self.__aceQLHttpApi.add_request_headers(headers)

    def reset_request_headers(self):
        """Resets the request headers. The previously added headers with add_request_headers will be suppressed."""
        self.__aceQLHttpApi.reset_request_headers()

    def set_progress_indicator(self, progress_indicator: ProgressIndicator):
        """ Allows to set a progress indicator."""
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
        """Gets the SDK version."""
        return AceQLHttpApi.get_client_version()

    @staticmethod
    def get_client_version_full() -> str:
        """Gets the SDK version with the Python version."""
        return AceQLHttpApi.get_client_version_full()
