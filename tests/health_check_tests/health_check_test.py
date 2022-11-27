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

from aceql import Connection, Cursor, HealthCheck
from tests.dml.sql_delete_test import SqlDeleteTest
from tests.util.connection_builder import ConnectionBuilder


class HealthCheckTest(object):
    """Tests of health check features."""

    def __init__(self, connection: Connection):
        self.__connection = connection

    def execute(self):
        health_check = HealthCheck(self.__connection)
        print("health_check.ping()                      : " + str(health_check.ping()))
        print("health_check.get_response_time()         : " + str(health_check.get_response_time("select 1")))
        print("health_check.get_response_time_select_1(): " + str(health_check.get_response_time_select_1()))
        print("health_check.get_server_memory_info()    : " + str(health_check.get_server_memory_info()))
        print(str(datetime.now()) + " End.")


if __name__ == '__main__':
    connection: Connection = ConnectionBuilder.get_connection()
    try:
        health_check_test = HealthCheckTest(connection)
        health_check_test.execute()
    finally:
        connection.close()
    exit()