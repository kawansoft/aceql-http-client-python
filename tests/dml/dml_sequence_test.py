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

from aceql import Connection, Cursor, ProgressIndicator
from tests.dml.blob_test_util import BlobTestUtil
from tests.dml.orderlog_row import OrderLogRow
from tests.dml.sql_delete_test import SqlDeleteTest


class DmlSequenceTest(object):
    """
    Do a full sequence of INSERT / SELECT / UPDATE / SELECT and test at each
    action that attended values are OK with unitest
    """

    def __init__(self, connection: Connection):
        self.connection: Connection = connection

    def test_sequence(self):
        print("Delete with delete_orderlog_all() done to clear all for test.")
        sql_delete_test = SqlDeleteTest(self.connection)
        sql_delete_test.delete_orderlog_all()

        orderlog_row: OrderLogRow = OrderLogRow()

        cursor: Cursor = self.connection.cursor()
        self.connection.set_auto_commit(False)

        progress_indicator = ProgressIndicator()
        self.connection.set_progress_indicator(progress_indicator)

        rows: int = self.__insert_row(cursor, orderlog_row)
        print("Insert done. Rows: " + str(rows));
        self.connection.commit()
        cursor.close()

        cursor: Cursor = self.connection.cursor()
        self.__select_row(cursor, orderlog_row)
        self.connection.commit()
        cursor.close()

    @staticmethod
    def __insert_row(cursor: Cursor, orderlog_row: OrderLogRow) -> int:
        """Insert a single row wuth a BLOB file"""
        filename = orderlog_row.jpeg_image
        statinfo = os.stat(filename)
        the_length = statinfo.st_size

        fd = open(filename, "rb")
        blob_tuple = (fd, the_length)

        sql = "insert into orderlog values (?, ?, ?, ?, ?, ?, ?, ?, ?)"

        is_delivered = 0;
        if orderlog_row.is_delivered:
            is_delivered = 1

        params = (orderlog_row.customer_id, orderlog_row.item_id, orderlog_row.description, orderlog_row.item_cost,
                  orderlog_row.date_placed, orderlog_row.date_shipped, blob_tuple, is_delivered, orderlog_row.quantity)
        print("Insert values: " + str(params))
        return cursor.execute(sql, params)

    @staticmethod
    def __select_row(cursor: Cursor, orderlog_row: OrderLogRow):
        """Select back one row"""

        sql = "select * from orderlog where customer_id = ? and item_id = ?"
        params = (orderlog_row.customer_id, orderlog_row.item_id)
        cursor.execute(sql, params)
        print("cursor.rowcount    : " + str(cursor.rowcount))
        row = cursor.fetchone()

        customer_id = row[0]
        item_id = row[1]
        description = row[2]
        item_cost = row[3]
        date_placed = row[4]
        date_shipped = row[5]
        jpeg_image = row[6]

        is_delivered = row[7]
        quantity = row[8]

        file = orderlog_row.out_jpeg_image;
        if os.path.exists(file):
            os.remove(file)

        response = cursor.get_blob_stream(6)
        with open(file, 'wb') as fd:
            for chunk in response.iter_content(chunk_size=2048):
                fd.write(chunk)

        print();
        print("customer_id   : " + str(customer_id));
        print("item_id       : " + str(item_id));
        print("description   : " + str(description));
        print("item_cost     : " + str(item_cost));
        print("date_placed   : " + str(date_placed));
        print("date_shipped  : " + str(date_shipped));
        print("jpeg_image    : " + "<binary> of " + str(jpeg_image));

        print("is_delivered  : " + str(is_delivered));
        print("quantity      : " + str(quantity));

        assert customer_id == orderlog_row.customer_id, "customer_id are different."
        assert item_id == orderlog_row.item_id, "item_id are different."
        assert description == orderlog_row.description, "description are different."
        assert item_cost == orderlog_row.item_cost, "item_cost are different."

        assert date_placed == orderlog_row.date_placed, "date_placed are different."
        assert date_shipped == orderlog_row.date_shipped, "date_shipped are different."

        assert is_delivered == orderlog_row.is_delivered, "is_delivered are different."
        assert quantity == orderlog_row.quantity, "quantity are different."

        print("Testing  files in/out are equals");
        BlobTestUtil.check_blob_integrity(orderlog_row.jpeg_image, file)

    @staticmethod
    def print_description(cursor):
        """Debug tool to print the columns details"""
        description = cursor.description
        print("len(description): " + str(len(description)))
        print("cursor.description: ")
        for the_col_desc in description:
            print(the_col_desc)




