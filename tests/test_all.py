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

from aceql import Connection
from aceql import ProgressIndicator
from aceql import SqlNullType
import os
from os import sep
from datetime import datetime, date

from aceql._private.aceql_debug_parms import AceQLDebugParms
from tests.util.connection_builder import ConnectionBuilder
from tests.dml.dml_sequence_test import DmlSequenceTest
from tests.dml_batch.sql_batch_test import SqlBatchTest
from tests.metadata.test_metadata_api import TestMedata


class TestAll():

    @staticmethod
    def test_main(connection: Connection):

        AceQLDebugParms.PRINT_PROGRESS_INDICATOR = True;

        print()
        print("aceql version      : " + Connection.get_client_version())
        print("aceql version full : " + Connection.get_client_version_full())
        print("Connection Options : " + str(connection.get_connections_options()))
        print("Connection creation: " + str(connection.get_creation_datetime()))
        print("Database Info       : " + str(connection.get_database_info()))

        connection.set_holdability("hold_cursors_over_commit")
        holdability = connection.get_holdability()
        print("holdability: " + holdability)
        assert holdability == "hold_cursors_over_commit", "Fail holdability=hold_cursors_over_commit"

        connection.set_holdability("close_cursors_at_commit")
        holdability = connection.get_holdability()
        print("holdability: " + holdability)
        assert holdability == "close_cursors_at_commit", "Fail holdability=close_cursors_at_commit"

        connection.set_auto_commit(True)
        auto_commit = connection.get_auto_commit()
        print("auto_commit: " + str(auto_commit))
        assert auto_commit is True, "Fail auto_commit == True"

        connection.set_auto_commit(False)
        auto_commit = connection.get_auto_commit()
        print("auto_commit: " + str(auto_commit))
        assert auto_commit is False, "Fail auto_commit == True"

        cursor = connection.cursor()

        sql = "delete from orderlog where customer_id = ? and order_id = ?"
        print("sql before mogrify: " + sql)
        sql = cursor.mogrify(sql, (11, 22))
        print("sql after mogrify: " + str(sql))

        print("Before delete all orderlog")
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

        # Test all DML
        dml_sequence_test: DmlSequenceTest = DmlSequenceTest(connection)
        dml_sequence_test.test_sequence()

        sql_batch_test: SqlBatchTest = SqlBatchTest(connection)
        sql_batch_test.insert_using_batch()

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

            do_use_blob = True
            if not do_use_blob:
                blob_tuple = (None, SqlNullType.BLOB)
                print("NULL BLOB INSERT")

            the_float = float((cpt * 1000) + 0.44)
            print("theFloat: " + str(the_float))

            params = (cpt, cpt, "intitulé_" + str(cpt), the_float,
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
            filename = os.path.expanduser("~") + sep + "AceQL-Schema_OUT_" + str(cpt) + ".png"
            response = cursor.get_blob_stream(6)

            with open(filename, 'wb') as fd:
                for chunk in response.iter_content(chunk_size=2048):
                    fd.write(chunk)

        cursor.close()


if __name__ == '__main__':
    connection: Connection = ConnectionBuilder.get_connection()
    try:
        TestAll.test_main(connection)
    finally:
        connection.close()

    # Test Metadata
    test_medata: TestMedata = TestMedata()
    test_medata.test_A()

    print("The End!")
    exit()