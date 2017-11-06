#
# This file is part of AceQL Python Client SDK.
# AceQL Python Client SDK: Remote SQL access over HTTP with AceQL HTTP.
# Copyright (C) 2017,  KawanSoft SAS
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

from aceql.ProgressIndicator import *
from aceql.Cursor import *


class Connection(object):
    """ Allows to create a database connection to a remote server."""

    def __init__(self, server_url, database, username, password, proxies=None):
        """Creates a database connection to the remote server.

        Parameters
        ----------
        server_url: str
                   the URL of the AceQL server. Example: https://www.acme.com:9443/aceql
        database: str
                  the remote database name
        username: str
                  the authentication username
        password: str
                  the authentication password
        proxies: proxies
                 the proxy to use, can  be an authenticatesd proxy.
                 See Requests doc (http://docs.python-requests.org)
        """

        if server_url is None:
            raise TypeError("serverUrl is null!")
        if database is None:
            raise TypeError("database is null!")
        if username is None:
            raise TypeError("username is null!")
        if password is None:
            raise TypeError("password is null!")

        self.__aceQLHttpApi = AceQLHttpApi(server_url, database, username, password, proxies=None)

    def cursor(self):
        """Instantiates and returns a cursor."""
        cursor = Cursor(self, self.__aceQLHttpApi)
        return cursor

    def is_stateless():
        """ Says if session is stateless."""
        return AceQLHttpApi.__stateless

    is_stateless = staticmethod(is_stateless)

    def set_stateless(stateless):
        """ Sets the session mode. if true, the session will be stateless, else stateful."""
        if stateless is None:
            raise TypeError("stateless is null!")
        if str(stateless) == "True":
            AceQLHttpApi.__stateless = True
        else:
            AceQLHttpApi.__stateless = False

    set_stateless = staticmethod(set_stateless)

    def set_timeout(timeout):
        """ Sets the HTTP connection timeout in seconds.
        0 means not timeout is used (default value)."""

        if timeout is None:
            raise TypeError("timeout is null!")

        if isinstance(timeout, int):
            AceQLHttpApi.__timeout = timeout
        else:
            raise Exception("timeout is not numeric!")

    set_timeout = staticmethod(set_timeout)

    def set_progress_indicator(self, progress_indicator):
        """ Allows to set a progress indicator."""
        self.__aceQLHttpApi.setProgressIndicator(progress_indicator)

    def get_progress_indicator(self):
        """Returns the progress indicator in use."""
        return self.__aceQLHttpApi.getProgressIndicator()

    def set_auto_commit(self, auto_commit):
        """Sets this connection's auto-commit mode to the given state."""
        self.__aceQLHttpApi.setAutoCommit(auto_commit)

    def get_auto_commit(self):
        """Retrieves the current auto-commit mode."""
        return self.__aceQLHttpApi.getAutoCommit()

    def commit(self):
        """Commit current transaction."""
        self.__aceQLHttpApi.commit()

    def rollback(self):
        """Rollback current transaction."""
        self.__aceQLHttpApi.rollback()

    def _trace(self):
        """Print empty line on trace."""
        self.__aceQLHttpApi.trace()

    def trace(self, s):
        """Print the string on trace."""
        self.__aceQLHttpApi.trace(s)

    def _is_trace_on():
        """Says if trace is on."""
        return AceQLHttpApi.isTraceOn()

    _is_trace_on = staticmethod(_is_trace_on)

    def _set_trace_on(trace_on):
        """Sets the trace on/off."""
        AceQLHttpApi.setTraceOn(trace_on)

    _set_trace_on = staticmethod(_set_trace_on)

    def is_gzip_result(self):
        """Says if the query result is returned compressed with the GZIP file format."""
        return self.__aceQLHttpApi.isGzipResult()

    def set_gzip_result(self, gzipResult):
        """Define if result sets are compressed before download.  Defaults to true."""
        self.__aceQLHttpApi.setGzipResult(gzipResult)

    def get_server_version(self):
        """Gets the server version of AceQL HTTP."""
        return self.__aceQLHttpApi.getServerVersion()

    def get_client_version(self):
        """Gets the SDK version."""
        return self.__aceQLHttpApi.getClientVersion()

    def close(self):
        """Closes the connection to the remote database and closes the HTTP session."""
        self.__aceQLHttpApi.disconnect()

    def get_transaction_isolation(self):
        """Returns the current transaction isolation level."

           Will be one of the following constants:
                transaction_read_uncommitted,
                transaction_read_committed,
                transaction_repeatable_read,
                transaction_serializable, or
                transaction_none.
        """
        return self.__aceQLHttpApi.get_transaction_isolation()

    def set_transaction_isolation(self, level):
        """Sets the transaction isolation level."""
        self.__aceQLHttpApi.set_transaction_isolation(level)

    def get_holdability(self):
        """return the holdability.
         One of hold_cursors_over_commit or close_cursors_at_commit.
        """
        return self.__aceQLHttpApi.get_holdability()

    def set_holdability(self, holdability):
        """Sets the holdability."""
        self.__aceQLHttpApi.set_holdability(holdability)

    def is_read_only(self):
        """Says if Connection is read-only."""
        return self.__aceQLHttpApi.is_read_only()

    def set_read_only(self, read_only):
        """Allows to put Connection read-only mode."""
        self.__aceQLHttpApi.set_read_only(read_only)
