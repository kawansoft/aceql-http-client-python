# -*- coding: utf-8 -*-
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
from typing import re

from aceql import Connection
from aceql._private.datetime_util import DateTimeUtil
from aceql._private.datetime_util import datetime
from aceql._private.file_util import FileUtil


class ConnectionUtil(object):
    """Utilities for Connection class. """

    SERVER_VERSION_NUMBER = None
    BATCH_MIN_SERVER_VERSION = "8.0"
    GET_DATABASE_INFO_MIN_SERVER_VERSION = "9.0"

    @staticmethod
    def is_get_database_info_supported(connection: Connection) -> bool:
        """ Says if GetDatabaseInfo call supported on server."""
        raw_server_version: str = ConnectionUtil.get_server_raw_version(connection)
        return ConnectionUtil.is_current_version_ok(raw_server_version,
                                                    ConnectionUtil.GET_DATABASE_INFO_MIN_SERVER_VERSION)

    @staticmethod
    def get_server_raw_version_(connection: Connection) -> str:
        """ For python 2: string values with special chars must be UTF-8 encoded """
        if ConnectionUtil.SERVER_VERSION_NUMBER is None:
            ConnectionUtil.SERVER_VERSION_NUMBER = connection.get_server_version()

        # https://stackoverflow.com/questions/3368969/find-string-between-two-substrings
        # s = 'asdf=5;iwantthis123jasd'
        # result = re.search('asdf=5;(.*)123jasd', s)
        #    print(result.group(1))

        raw_version: str = re.search('v(.*)-', ConnectionUtil.SERVER_VERSION_NUMBER)
        return raw_version

    @staticmethod
    def is_current_version_ok(raw_server_version: str, min_server_version: str) -> bool:
        # Says if the current version is OK , that is >= to the minimum required server version
        return float(raw_server_version) >= float(min_server_version)
