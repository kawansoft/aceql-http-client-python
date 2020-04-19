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
from typing import List

import aceql
from aceql import *

import unittest
import sys

from aceql.metadata.column import Column
from aceql.metadata.remote_database_metadata import RemoteDatabaseMetaData
import webbrowser
import os


class TestAll(unittest.TestCase):
    def test_A(self):

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
        server_host = "https://www.aceql.com:9443/aceql"
        server_host_no_ssl = "http://www.aceql.com:9090/aceql"

        host = localhost

        Connection.set_timeout(10)
        Connection.set_stateless(False)
        connection = aceql.connect(host, "sampledb", "user1", "password1", proxies=proxies, auth=auth)
        connection.set_gzip_result(True)

        print()
        print("aceql version: " + connection.get_client_version())
        print()

        the_file = "c:\\test\\python_schema.html";
        if os.path.exists(the_file):
            os.remove(the_file)

        remote_database_meta_data = RemoteDatabaseMetaData(connection)
        remote_database_meta_data.db_schema_download(the_file, "html", )

        do_webbrowser = True
        if do_webbrowser is True:
            webbrowser.open('file://' + os.path.realpath(the_file))
        print("Done db_schema_download!")

        jdbc_database_meta_data = remote_database_meta_data.get_jdbc_database_meta_data()
        print(jdbc_database_meta_data.getURL)
        print(jdbc_database_meta_data)
        print("Done get_jdbc_database_meta_data!")

        print()
        print("Printing table names:")
        table_names = remote_database_meta_data.get_table_names()
        print(table_names)

        print()
        the_table = "customer"
        print("Printing table details for: " + the_table)
        table = remote_database_meta_data.get_table(the_table)
        print("table: " + str(table))

        columns: List[Column] = table.columns

        print()
        for column in columns:
            print ("column: " + str(column))


if __name__ == '__main__':
    unittest.main()
