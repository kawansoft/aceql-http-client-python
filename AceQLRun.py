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

from aceql.ProgressIndicator import *
from aceql.Connection import *
from tests.AceQLHttpApiTest import *
from aceql.SqlNullType import *

import aceql
import sys
from datetime import datetime, date, time

print(sys.version)
# assert sys.version_info >= (2,5)
print()

serverHost = "https://www.aceql.com:9443/aceql"
localhost = "http://localhost:9090/aceql"

host = localhost

Connection.set_stateless(True)
connection = aceql.connect(host, "kawansoft_example", "user1", "password1")
connection.set_gzip_result(True)

cursor = connection.cursor()

sql = "update customer set lname = ? where customer_id = ?"
params = ("Python3.6", 1)
rows = cursor.execute(sql, params)
print("update rows: " + str(rows))
print()

try:
    sql = "update xxxxxxxxxxxxxxxx set lname = ? where customer_id = ?"
    params = ("Python3.6", 1)
    rows = cursor.execute(sql, params)
    print("update rows: " + str(rows))
    print()
except Exception as e:
    print(e)

connection.set_auto_commit(False)

doUpdate = True

if doUpdate:
    sql = "delete from orderlog where customer_id >= ?"
    params = (0,)
    cursor.execute(sql, params)

    # customer_id integer NOT NULL,
    # item_id integer NOT NULL,
    # description character varying(64) NOT NULL,
    # cost_price numeric,
    # date_placed date NOT NULL,
    # date_shipped timestamp without time zone,
    # jpeg_image oid,
    # is_delivered numeric,
    # quantity integer NOT NULL,

    connection.commit()

    theDate = date(2017, 11, 3)
    cpt = 0
    filename = "C:\\test\\AceQL-Schema.png"
    statinfo = os.stat(filename)
    the_length = statinfo.st_size * 3

    while True:

        progressIndicator = ProgressIndicator()
        connection.set_progress_indicator(progressIndicator)

        fd = open(filename, "rb")
        blob_tuple = (fd, the_length)

        sql = "insert into orderlog values (?, ?, ?, ?, ?, ?, ?, ?, ?)"

        # params = (cpt, cpt, u"intitulé_" + str(cpt), cpt * 1000, theDate, datetime.now(), (None, SqlNullType.BLOB), 1, cpt * 1000)
        params = (cpt, cpt, u"intitulé_" + str(cpt), cpt * 1000, theDate, datetime.now(), blob_tuple, 1, cpt * 1000)
        print("insert: " + str(params))
        cursor.execute(sql, params)
        cpt += 1
        if cpt >= 3:
            break

    connection.commit()

sql = "select * from orderlog where customer_id >= ? order by customer_id"
params = (0,)
cursor.execute(sql, params)
print("cursor.rowcount    : " + str(cursor.rowcount))
print("cursor.description: " + str(cursor.description))

doIterate = False

if doIterate:
    for row in cursor:
        print(row)

doFetchMany = True
if doFetchMany:
    rows = cursor.fetchmany(1)

    print("fetchmany:")
    for row in rows:
        print(row)
    print()

doFetchAll = True
if doFetchAll:
    rows = cursor.fetchall()

    print("fetchall:")
    for row in rows:
        print(row)
    print()

connection.commit()

sql = "select * from orderlog where customer_id >= ? order by customer_id"
params = (0,)
cursor.execute(sql, params)
print("cursor.rowcount    : " + str(cursor.rowcount))
print("cursor.description: ")
description = cursor.description
for desc in description:
    print(desc)

connection.commit()

print()
cpt = 0
while (True):
    row = cursor.fetchone()
    if row is None:
        break
    print(row)

    # 6 is is the index of BLOB in the row
    total_length = cursor.get_blob_length(6)

    cpt += 1
    # print("BLOB length : " + str(total_length))
    filename = "C:\\test\\out\\out_" + str(cpt) + ".jpg"
    response = cursor.get_blob_stream(6)

    with open(filename, 'wb') as fd:
        for chunk in response.iter_content(chunk_size=2048):
            fd.write(chunk)

cursor.close()
print()

connection.close()

# aceQLHttpApiTest = AceQLHttpApiTest()
# aceQLHttpApiTest.doIt()

# theTest = Test_ResultAnalyzerTest()
# theTest.test_A()

# rowCounterTest = Test_RowCounterTest()
# rowCounterTest.test_A()

# rowParserTest = Test_RowParserTest()
# rowParserTest.test_A()

# streamResultAnalyzerTest = Test_StreamResultAnalyzerTest()
# streamResultAnalyzerTest.test_A()

# print()
