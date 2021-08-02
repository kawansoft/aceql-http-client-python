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
from aceql import Connection
from tests.connection_builder import ConnectionBuilder
from datetime import datetime

connection = ConnectionBuilder.get_connection()

print()
print("aceql version     : " + Connection.get_client_version())
print("aceql version full: " + Connection.get_client_version_full())
print("Connection Options: " + str(connection.get_connections_options()))
print()
cursor = connection.cursor()

print("Before SQL delete all customer")
sql = "delete from customer where customer_id >= 1"
cursor.execute(sql, None)

print("Before SQL insert call")
sql = "insert into customer values (?, ?, ?, ?, ?, ?, ?, ?)"
params = (1, 'Sir', 'John', 'Smith I', '11 Madison Ave', 'New York',
          'NY 10010', '+1 212-586-7001')
cursor.execute(sql, params)

print("Before SQL delete all customer")
sql = "delete from customer where customer_id >= 1"
cursor.execute(sql, None)

print("Before SQL executemany")
params_list:list = []
sql = "insert into customer values (?, ?, ?, ?, ?, ?, ?, ?)"
params = (1, 'Sir', 'John', 'Smith I', '1 Madison Ave', 'New York',
          'NY 10010', '+1 212-586-7001')
params_list.append(params)
params = (2, 'Mme', 'John', 'Smith II', '2 Madison Ave', 'New York',
          'NY 20020', '+1 212-586-7002')
params_list.append(params)
cursor.executemany(sql, params_list)

print(str(datetime.now()) + " End.")
