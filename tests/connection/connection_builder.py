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

import sys
import aceql
from aceql import ProxyAuth
from aceql import ConnectionOptions
from aceql.dbapi2 import apilevel
from aceql.dbapi2 import threadsafety
from aceql.dbapi2 import paramstyle


class ConnectionBuilder(object):
    """Allows to create a database connection to a remote server."""

    @staticmethod
    def get_connection():
        print(sys.version)
        # assert sys.version_info >= (2,5)
        print()

        print("aceql.apilevel    : " + apilevel)
        print("aceql.threadsafety: " + str(threadsafety))
        print("aceql.paramstyle  : " + paramstyle)

        proxies = None
        auth = None

        use_proxy = False
        if use_proxy:
            proxies = {
                "http": "http://localhost:8081",
            }

            auth = ConnectionBuilder.get_proxy_auth()

        localhost = "http://localhost:9090/aceql"
        # server_host = "https://www.aceql.com:9443/aceql"
        # server_host_no_ssl = "http://www.aceql.com:9090/aceql"

        url = localhost

        database = "sampledb"
        username = "user1"
        password = ConnectionBuilder.get_the_password()
        headers = {'user-agent': 'aceql-client'}

        connection_options = ConnectionOptions(proxies=proxies, auth=auth, gzip_result=True, timeout=10, request_headers=headers)

        connect_with_parms = False
        if connect_with_parms:
            print("connecting with parameters")
            connection = aceql.connect(url=url, username=username, password=password,
                                   database=database, connection_options=connection_options)
            return connection

        url = localhost + "?username="+username+"&password=" + password + "&database=" + database
        print("connecting with url: " + url)
        connection = aceql.connect(url=url, connection_options=connection_options)

        return connection

    @staticmethod
    def get_the_password():
        return "password1"

    @staticmethod
    def get_proxy_auth():
        """Get proxy auth info from a filename"""
        with open("I:\\neotunnel.txt", "rt") as fd:
            content = fd.read()
        lines = content.split()
        auth = ProxyAuth(lines[0].strip(), lines[1].strip())
        return auth
