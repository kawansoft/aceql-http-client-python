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
from datetime import datetime

from aceql import Connection, Cursor
from tests.dml.sql_delete_test import SqlDeleteTest
from tests.util.connection_builder import ConnectionBuilder


class SqlBatchTest(object):
    """Delete all rows of customer and orderlog tables."""

    def __init__(self, connection: Connection):
        self.__connection = connection

    def insert_using_batch(self):
        cursor: Cursor = self.__connection.cursor()
        print("Before delete all customer")
        sql_delete_test = SqlDeleteTest(self.__connection)
        sql_delete_test.delete_customer_all()

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

        print()
        sql = "select * from customer where customer_id >= ?"
        params = (1,)
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        print(str(datetime.now()) + " End.")


if __name__ == '__main__':
    connection: Connection = ConnectionBuilder.get_connection()
    try:
        sql_batch_test = SqlBatchTest(connection)
        sql_batch_test.insert_using_batch()
    finally:
        connection.close()
    exit()