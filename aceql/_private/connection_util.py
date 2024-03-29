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
from typing import TYPE_CHECKING

if TYPE_CHECKING:
   from aceql.connection import Connection


class ConnectionUtil(object):
    """Utilities for Connection class. """

    SERVER_VERSION_NUMBER = None
    SERVER_VERSION_12_2 = "12.2";

    @staticmethod
    def get_server_raw_version(connection: 'Connection') -> str:
        """ Extract the server number version between the v and - """
        if ConnectionUtil.SERVER_VERSION_NUMBER is None:
            ConnectionUtil.SERVER_VERSION_NUMBER = connection.get_server_version()

        end_string: str = ConnectionUtil.SERVER_VERSION_NUMBER.partition("v")[2]
        version_str: str = end_string.partition('-')[0]
        return version_str

    @staticmethod
    def is_current_version_ok(raw_server_version: str, min_server_version: str) -> bool:
        # Says if the current version is OK, that is >= to the minimum required server version
        return float(raw_server_version) >= float(min_server_version)

    @staticmethod
    def is_version12_2_or_higher(connection: 'Connection') -> bool:
        raw_server_version = ConnectionUtil.get_server_raw_version(connection)
        return ConnectionUtil.is_current_version_ok(raw_server_version, ConnectionUtil.SERVER_VERSION_12_2)



