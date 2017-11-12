# -*- coding: utf-8 -*-
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

import aceql
from aceql import *


# URL of the AceQL server, Remote SQL database name
# & authentication info
host = "http://localhost:9090/aceql"
database = "kawansoft_example"
username = "user1"
password = "password1"

connection = aceql.connect(host, database, username, password)

cursor = connection.cursor()

if True:
    try:
        sql = "update xxxxxxxxxxxxxxxx set lname = ? where customer_id = ?"
        params = ("Python3.6", 1)
        rows = cursor.execute(sql, params)
        print("update rows: " + str(rows))
        print()
    except Exception as e:
        print(e)

sql = "drop table if exists customer"
cursor.execute(sql)

sql = "drop table if exists customer_3"
cursor.execute(sql)

sql = """CREATE TABLE customer 
(
    customer_id     integer     not null,
    customer_title  char(4)         null,
    fname           varchar(32)     null,
    lname           varchar(32) not null,
    addressline     varchar(64) not null,
    town            varchar(32) not null,
    zipcode         char(10)    not null,
    phone           varchar(32)     null,
        PRIMARY KEY(customer_id)
)"""
cursor.execute(sql)

sql = """CREATE TABLE customer_3 
(
    customer_id     integer     not null,
    customer_title  char(4)         null,
    fname           varchar(32)     null,
    lname           varchar(32) not null,
    addressline     varchar(64) not null,
    town            varchar(32) not null,
    zipcode         integer          null,
    phone           varchar(32)     null,
        PRIMARY KEY(customer_id)
)"""
cursor.execute(sql)

sql = "delete from customer where customer_id >= ?"
params = (0,)
cursor.execute(sql, params)

sql = "insert into customer values (?, ?, ?, ?, ?, ?, ?, ?)"
params = (1, 'Sir', 'John', 'Smith', '1 Madison Ave', 'New York', 'NY 10010', '+1 212-586-7000')
cursor.execute(sql, params)

print("rows inserted: " + str(cursor.rowcount))

sql = "select * from customer where customer_id = ?"
params = (1,)
cursor.execute(sql, params)

print()
for desc in cursor.description:
    print(desc[0] + ", " + desc[1])

print()
row = cursor.fetchone()
print (row)

cursor.close()
cursor = connection.cursor()

sql = "insert into customer values (?, ?, ?, ?, ?, ?, ?, ?)"
params = (2, 'Sir', 'William', 'Smith II', '1 Madison Ave', 'New York', 'NY 10010', '+1 212-586-7002')
cursor.execute(sql, params)

sql = "insert into customer values (?, ?, ?, ?, ?, ?, ?, ?)"
params = (3, 'Sir', 'William', 'Smith III', '1 Madison Ave', 'New York', 'NY 10010', '+1 212-586-7003')
cursor.execute(sql, params)

cursor.close()
cursor = connection.cursor()

sql = "select * from customer where customer_id >= ? order by customer_id"
params = (1,)
cursor.execute(sql, params)

print()

rows  = cursor.fetchall()

for row in rows:
    print(row)
print("rows: " + str(cursor.rowcount))

cursor.close()
cursor = connection.cursor()

sql = "insert into customer values (?, ?, ?, ?, ?, ?, ?, ?)"
params = (4, 'Sir', 'William', 'Smith II', '1 Madison Ave', 'New York', 'NY 10010', (None, SqlNullType.VARCHAR))
cursor.execute(sql, params)

sql = "select * from customer where customer_id = ? order by customer_id"
params = (4,)
cursor.execute(sql, params)

cursor.close()
cursor = connection.cursor()

sql = "insert into customer_3 values (?, ?, ?, ?, ?, ?, ?, ?)"
params = (4, 'Sir', 'William', 'Smith II', '1 Madison Ave', 'New York', (None, SqlNullType.INTEGER), '+1 212-586-7004')
cursor.execute(sql, params)

sql = "select * from customer_3 where customer_id = ? order by customer_id"
params = (4,)
cursor.execute(sql, params)

print()
row = cursor.fetchone()
print (row)

cursor.close()







