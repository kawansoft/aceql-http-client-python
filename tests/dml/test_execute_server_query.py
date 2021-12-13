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
import os
from os.path import sep

from aceql import Connection

from aceql._private.aceql_debug_parms import AceQLDebugParms
from tests.util.connection_builder import ConnectionBuilder


class TestExecuteServerQuery():

    @staticmethod
    def test_main(connection: Connection):
        AceQLDebugParms.DEBUG_ON = False

        print()
        print("aceql version      : " + Connection.get_client_version())
        print("aceql version full : " + Connection.get_client_version_full())
        print("Connection Options : " + str(connection.get_connections_options()))
        print("Connection creation: " + str(connection.get_creation_datetime()))
        print("Database Info       : " + str(connection.get_database_info()))

        cursor = connection.cursor()

        server_query_executor_class_name = "org.kawanfw.test.api.server.executor.MyServerQueryExecutor"
        my_parameters = [1]

        cursor.execute_server_query(server_query_executor_class_name, my_parameters)
        print("cursor.rowcount    : " + str(cursor.rowcount))
        rows = cursor.fetchall()

        print("fetchall:")
        for row in rows:
            print(row)
        print()

        cursor.close()


if __name__ == '__main__':
    connection: Connection = ConnectionBuilder.get_connection()
    try:
        TestExecuteServerQuery.test_main(connection)
    finally:
        connection.close()

    print("The End!")
    exit()