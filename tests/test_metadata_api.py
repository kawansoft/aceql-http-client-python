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

import aceql
from aceql import Connection
import unittest
import sys
from aceql.metadata.remote_database_metadata import RemoteDatabaseMetaData
import webbrowser
import os


class TestAll(unittest.TestCase):
    @staticmethod
    def test_A():

        print(sys.version)
        # assert sys.version_info >= (2,5)
        print()

        print("aceql.apilevel    : " + aceql.apilevel)
        print("aceql.threadsafety: " + str(aceql.threadsafety))
        print("aceql.paramstyle  : " + aceql.paramstyle)

        proxies = None
        auth = None

        use_proxy = False
        if use_proxy:
            proxies = {
                "http": "http://localhost:8080",
            }

            auth = TestAll.getProxyAuth()

        localhost = "http://localhost:9090/aceql"
        #server_host = "https://www.aceql.com:9443/aceql"
        #server_host_no_ssl = "http://www.aceql.com:9090/aceql"

        host = localhost

        Connection.set_timeout(10)
        Connection.set_stateless(False)
        connection = aceql.connect(host, "sampledb", "user1", "password1", proxies=proxies, auth=auth)
        connection.set_gzip_result(True)

        print()
        print("aceql version: " + get_client_version())
        print()

        remote_database_meta_data = RemoteDatabaseMetaData(connection)

        filename = os.path.expanduser("~") + os.sep + "db_schema.html"
        remote_database_meta_data.db_schema_download(filename)

        do_webbrowser = True
        if do_webbrowser is True:
            webbrowser.open('file://' + os.path.realpath(filename))
        print("Done db_schema_download!")

        jdbc_meta_data = remote_database_meta_data.get_jdbc_database_meta_data()
        print("Major Version: " + str(jdbc_meta_data.getJDBCMajorVersion))
        print("Minor Version: " + str(jdbc_meta_data.getJDBCMinorVersion))
        print("IsReadOnly   : " + str(jdbc_meta_data.isReadOnly))

        print(jdbc_meta_data.getURL)
        print(jdbc_meta_data)
        print("Done get_jdbc_database_meta_data!")

        print()

        print("Get the table names:");
        table_names = remote_database_meta_data.get_table_names()

        print("Print the column details of each table:")
        for table_name in table_names:
            table = remote_database_meta_data.get_table(table_name)

            print()
            print("Columns of table: " + table_name)
            for column in table.columns:
                print(column)

        connection.close()


if __name__ == '__main__':
    unittest.main()
