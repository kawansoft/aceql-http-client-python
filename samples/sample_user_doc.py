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
from contextlib import closing
from datetime import datetime, time
import os
from os import sep
from io import open

# URL of the AceQL server, Remote SQL database name
# & authentication info
#host = "http://localhost:9090/aceql"

host = "http://localhost:9090/aceql"
database = "kawansoft_example"
username = "user1"
password = "password1"

print("aceql.apilevel: " + aceql.apilevel)

Connection.set_timeout(0.1)
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
cursor.close()

cursor = connection.cursor()

sql = "insert into customer values (?, ?, ?, ?, ?, ?, ?, ?)"
params = (1, 'Sir', 'John', 'Smith', '1 Madison Ave', 'New York',
          'NY 10010', '+1 212-586-7001')
cursor.execute(sql, params)
rows_inserted = cursor.rowcount

sql = "insert into customer values (?, ?, ?, ?, ?, ?, ?, ?)"
params = (2, 'Sir', 'William', 'Smith II', '1 Madison Ave', 'New York',
          'NY 10010', '+1 212-586-7002')
cursor.execute(sql, params)
rows_inserted += cursor.rowcount

sql = "insert into customer values (?, ?, ?, ?, ?, ?, ?, ?)"
params = (3, 'Sir', 'William', 'Smith III', '1 Madison Ave', 'New York',
          'NY 10010', '+1 212-586-7003')
cursor.execute(sql, params)
rows_inserted += cursor.rowcount

print("rows inserted: " + str(rows_inserted))



sql = "select * from customer where customer_id = ?"
params = (1,)
cursor.execute(sql, params)
row = cursor.fetchone()
print (row)

print()
for desc in cursor.description:
    print(desc[0] + ", " + desc[1])

cursor.close()

print()


with closing(connection.cursor()) as cursor:
    sql = "select * from customer where customer_id >= ? order by customer_id"
    params = (1,)
    cursor.execute(sql, params)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    print("rows: " + str(cursor.rowcount))

cursor = connection.cursor()

sql = "insert into customer values (?, ?, ?, ?, ?, ?, ?, ?)"
params = (4, 'Sir', 'William', 'Smith II', '1 Madison Ave', 'New York', 'NY 10010', (None, SqlNullType.VARCHAR))
cursor.execute(sql, params)

sql = "select * from customer where customer_id = ? order by customer_id"
params = (4,)
cursor.execute(sql, params)
row = cursor.fetchone()
print (row)

cursor.close()
cursor = connection.cursor()

sql = "insert into customer_3 values (?, ?, ?, ?, ?, ?, ?, ?)"
params = (4, 'Sir', 'William', 'Smith II', '1 Madison Ave', 'New York', (None, SqlNullType.INTEGER), '+1 212-586-7004')
cursor.execute(sql, params)

print()
sql = "select * from customer_3 where customer_id = ? order by customer_id"
params = (4,)
cursor.execute(sql, params)
row = cursor.fetchone()
print (row)

cursor.close()

cursor = connection.cursor()
print()
sql = "delete from orderlog where item_id = ?"
params = (1,)
cursor.execute(sql, params)
print (row)

connection.set_auto_commit(False)

with closing(connection.cursor()) as cursor:
    filename = os.getcwd() + sep + "item_1_image.jpg"
    file_length = os.stat(filename).st_size

    fd = open(filename, "rb")
    blob_tuple = (fd, file_length)

    progress_indicator = ProgressIndicator()
    connection.set_progress_indicator(progress_indicator)

    sql = "insert into orderlog values ( ?, ?, ?, ?, ?, ?, ?, ?, ? )"

    params = (1, 1, "Item 1 Description", 9999,
              datetime.now() , datetime.now().date(),
              blob_tuple, 1, 2)
    cursor.execute(sql, params)

connection.commit()
cursor.close();

with closing(connection.cursor()) as cursor:

    sql = "select customer_id, item_id, jpeg_image from orderlog " \
          "where customer_id = ? and item_id = ?"
    params = (1, 1)
    cursor.execute(sql, params)
    row = cursor.fetchone()

    # You can get BLOB length if you want to use a progress indicator
    blob_length = cursor.get_blob_length(2)
    print("blob length: " + str(blob_length))

    # Get the stream to the remote BLOB
    response = cursor.get_blob_stream(2)

    # Download is streamed and writen into filename
    filename = os.path.expanduser("~") + sep + "jpeg_image.jpg"
    with open(filename, 'wb') as fd:
        for chunk in response.iter_content(chunk_size=2048):
            fd.write(chunk)

    stat_info = os.stat(filename)
    print("file length: " + str(stat_info.st_size))

connection.commit()

cursor.close();
# Make sure connection is always closed in order to close and release
# server connection into the pool:
connection.close()






