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

import unittest
import aceql
import sys
from datetime import datetime, date


class TestAll(unittest.TestCase):
    def test_A(self):

        print(sys.version)
        # assert sys.version_info >= (2,5)
        print()

        #server_host = "https://www.aceql.com:9443/aceql"
        localhost = "http://localhost:9090/aceql"

        host = localhost

        Connection.set_stateless(False)
        connection = aceql.connect(host, "kawansoft_example", "user1", "password1")
        connection.set_gzip_result(True)

        connection.set_holdability("hold_cursors_over_commit")
        holdability = connection.get_holdability()
        print("holdability: " + holdability)
        self.assertEqual(holdability, u"hold_cursors_over_commit")

        connection.set_holdability("close_cursors_at_commit")
        holdability = connection.get_holdability()
        print("holdability: " + holdability)
        self.assertEqual(holdability, u"close_cursors_at_commit")

        connection.set_auto_commit(True)
        auto_commit = connection.get_auto_commit()
        print("auto_commit: " + str(auto_commit))
        self.assertEqual(auto_commit, True)

        connection.set_auto_commit(False)
        auto_commit = connection.get_auto_commit()
        print("auto_commit: " + str(auto_commit))
        self.assertEqual(auto_commit, False)

        connection.commit()
        connection.set_auto_commit(True)

        cursor = connection.cursor()

        sql = "delete from customer where customer_id >= ?"
        params = (0,)
        cursor.execute(sql, params)

        sql = "insert into customer values (?, ?, ?, ?, ?, ?, ?, ?)"
        cpt = 0
        while cpt < 10:
            customer_id = cpt
            params = (customer_id, (None, SqlNullType.VARCHAR), u"André" + str(customer_id),
                      u"Smith_" + str(customer_id), str(customer_id) + u" César Avenue",
                      u"Town_" + str(customer_id),
                      str(customer_id) + "", str(customer_id) + u"12345678")
            cursor.execute(sql, params)
            cpt += 1

        sql = "select count(customer_id) from customer where customer_id >= ?"
        params = (0,)
        cursor.execute(sql, params)
        the_tup = cursor.fetchone()
        self.assertEqual(the_tup[0], 10)

        sql = "update customer set lname = ? where customer_id = ?"
        params = ("Python3.6", 1)
        rows = cursor.execute(sql, params)
        print("update rows: " + str(rows))
        self.assertEqual(rows, 1)
        print()

        cursor.close()
        cursor = connection.cursor()

        sql = "select * from customer where customer_id >= ? order by customer_id "
        params = (0,)
        cursor.execute(sql, params)
        the_tup = cursor.fetchone()
        print("the_tup: " + str(the_tup))
        self.assertEqual(the_tup[0], 0)

        cursor.close()
        cursor = connection.cursor()

        sql = "select * from customer where customer_id >= ? order by customer_id"
        params = (0,)
        cursor.execute(sql, params)

        rows = cursor.fetchall()
        for row in rows:
            print(row)

        print("cursor.rowcount    : " + str(cursor.rowcount))
        print("cursor.description: " + str(cursor.description))
        print("")

        cursor.close()
        cursor = connection.cursor()

        if True:
            try:
                sql = "update xxxxxxxxxxxxxxxx set lname = ? where customer_id = ?"
                params = ("Python3.6", 1)
                rows = cursor.execute(sql, params)
                print("update rows: " + str(rows))
                print()
            except Error as e:
                print(str(e))

        connection.set_auto_commit(False)

        cursor.close()
        cursor = connection.cursor()

        do_update = True

        print("Before delete all orderlog")
        if do_update:
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

            the_date = date(2017, 11, 3)
            cpt = 0
            filename = os.getcwd() + sep + "files" + sep + "AceQL-Schema.png"
            statinfo = os.stat(filename)
            the_length = statinfo.st_size * 3

            while True:

                progress_indicator = ProgressIndicator()
                connection.set_progress_indicator(progress_indicator)

                fd = open(filename, "rb")
                blob_tuple = (fd, the_length)

                sql = "insert into orderlog values (?, ?, ?, ?, ?, ?, ?, ?, ?)"

                params = (cpt, cpt, u"intitulé_" + str(cpt), cpt * 1000,
                          the_date, datetime.now(), blob_tuple, 1, cpt * 1000)
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

        do_fetch_many = True
        if do_fetch_many:
            rows = cursor.fetchmany(1)

            print("fetchmany:")
            for row in rows:
                print(row)
            print()

        do_fetch_all = True
        if do_fetch_all:
            rows = cursor.fetchall()

            print("fetchall:")
            for row in rows:
                print(row)
            print()

        connection.commit()

        cursor.close()
        cursor = connection.cursor()

        sql = "select * from orderlog where customer_id >= ? order by customer_id"
        params = (0,)
        cursor.execute(sql, params)
        print("cursor.rowcount    : " + str(cursor.rowcount))

        description = cursor.description
        print("len(description): " + str(len(description)))
        print("cursor.description: ")

        for the_col_desc in description:
            print(the_col_desc)

        connection.commit()

        print()
        cpt = 0
        while True:
            row = cursor.fetchone()
            if row is None:
                break
            print(row)

            # 6 is is the index of BLOB in the row
            total_length = cursor.get_blob_length(6)
            print("total_length: " + str(total_length))

            cpt += 1
            # print("BLOB length : " + str(total_length))
            filename = os.path.expanduser("~") + sep + "AceQL-Schema_OUT.png"
            response = cursor.get_blob_stream(6)

            with open(filename, 'wb') as fd:
                for chunk in response.iter_content(chunk_size=2048):
                    fd.write(chunk)

        cursor.close()
        print()

        connection.close()


if __name__ == '__main__':
    unittest.main()
