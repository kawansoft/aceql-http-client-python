# -*- coding: utf-8 -*-
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

from aceql._private.cursor_util import *


class Error(Exception):
    """
    Wrapper class for Exceptions thrown on client side or server side.
    """

    def __init__(self, reason, error_type, cause, remote_stack_trace, http_status_code):
        """
        Builds an Error that wraps/traps an Exception.

        reason
                   the error message
        error_type
                   The error type:
                        0 for local Exception.
                        1 for JDBC Driver Exception on the server.
                        2 for AceQL Exception on the server.
                        3 for AceQL Security Exception on the server.
                        4 for AceQL failure.
        cause
                   the wrapped/trapped Exception

        remote_stack_trace
                   the stack trace in case for remote Exception

        http_status_code
                   the http status code
        """

        # Format all to UTF-8 for Python-2 server messages, we may be have weird messages from server
        if reason is None:
            self._reason = None
        else:
            reason = CursorUtil.get_utf8_value(reason)
            self._reason = reason.splitlines()

        self._error_type = error_type
        self._cause = cause

        if remote_stack_trace is None:
            self._remote_stack_trace = None
        else:
            remote_stack_trace = CursorUtil.get_utf8_value(remote_stack_trace)
            self._remote_stack_trace = remote_stack_trace.splitlines()

        self._http_status_code = http_status_code

    @property
    def reason(self):
        """ The main error wrapped Exception message as a list of a split str. Can be None"""
        return self._reason

    @property
    def error_type(self):
        """
        The error type

        0 for local Exception.
        1 for JDBC Driver Exception on the server.
        2 for AceQL Exception on the server.
        3 for AceQL Security Exception on the server.
        4 for AceQL failure.
        """
        return self._error_type

    @property
    def cause(self):
        """ The Exception cause, None if no cause."""
        return self._cause

    @property
    def remote_stack_trace(self):
        """ The Remote Stack Trace as a list of a split str. None if Exception raised locally"""
        return self._remote_stack_trace

    @property
    def http_status_code(self):
        """ The HTTP Status Code."""
        return self._http_status_code

    def __str__(self):
        """ The string representation."""
        return str(self._reason) + ", " + str(self._error_type) + ", " + str(type(self._cause)) + ", " + str(
             self._remote_stack_trace) + ", " + str(self._http_status_code)


class InterfaceError(Error):
    pass


class DatabaseError(Error):
    pass


class InternalError(DatabaseError):
    pass


class OperationalError(DatabaseError):
    pass


class ProgrammingError(DatabaseError):
    pass


class IntegrityError(DatabaseError):
    pass


class DataError(DatabaseError):
    pass


class NotSupportedError(DatabaseError):
    pass
