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

from aceql import *
from datetime import datetime, date
from contextlib import contextmanager


class MyRemoteConnection(object):
    """
    This example:
        - Inserts a Customer and an Order on a remote database.
        - Displays the inserted raws on the console with two SELECT executed on the
          remote database.
    """

    def __init__(self, connection):
        self.connection = connection

    def remote_connection_builder():
        """Remote Connection Quick Start client example.

        Creates a Connection to a remote database.
        """

        # The URL of the AceQL Server servlet
        # Port number is the port number used to start the Web Server:
        url = "http://localhost:9090/aceql"

        # The remote database to use:
        database = "kawansoft_example"

        # (username, password) for authentication on server side.
        # No authentication will be done for our Quick Start:
        username = "MyUsername"
        password = "myPassword"

        # Attempt to establish a connection to the remote database.
        # On the server side, a JDBC connection is extracted from the
        # connection pool created by the server at startup.
        # The connection will remain ours during the session.
        connection = Connection(url, database, username, password)
        return connection

    remote_connection_builder = staticmethod(remote_connection_builder)

    def insert_customer_and_order_log(self, customer_id, item_id):
        """Example of 2 INSERT in the same transaction
            using a customer id and an order id.
        """

        self.connection.set_auto_commit(False)
        cursor = self.connection.cursor()

        try:
            # Create a Customer
            sql = "insert into customer values (?, ?, ?, ?, ?, ?, ?, ?)"
            params = (customer_id, 'Sir', 'John', 'Smith', '1 Madison Ave',
                      'New York', 'NY 10010', '+1 212-586-7000')
            cursor.execute(sql, params)

            # Create an Order for this Customer
            sql = "insert into orderlog values ( ?, ?, ?, ?, ?, ?, ?, ?, ? )"

            the_datetime = datetime.now()
            the_date = the_datetime.date()

            # (None, SqlNullType.BLOB) means to set the jpeg_image BLOB column to NULL on server:
            params = (customer_id, item_id, "Item Description", 99.99,
                      the_date, the_datetime, (None, SqlNullType.BLOB), 1, 2)
            cursor.execute(sql, params)

            self.connection.commit()
        except Error as e:
            print(e)
            self.connection.rollback()
        finally:
            self.connection.set_auto_commit(True)
            cursor.close()

    def select_customer_and_orderlog(self, customer_id, item_id):
        """Example of 2 SELECT calls"""

        cursor = self.connection.cursor()
        try:

            sql = "select customer_id, fname, lname from customer " \
                  "where customer_id = ?"
            params = (customer_id, )
            cursor.execute(sql, params)

            rows = cursor.fetchall()

            for row in rows:
                print()
                print("customer_id: " + str(row[0]))
                print("fname      : " + row[1])
                print("lname      : " + row[2])
        finally:
            cursor.close()

        cursor = self.connection.cursor()
        try:

            # Display the created Order
            sql = "select * from orderlog where  customer_id = ? and item_id = ? "

            params = (customer_id, item_id)
            cursor.execute(sql, params)

            rows = cursor.fetchall()

            for row in rows:
                print()
                print("customer_id : " + str(row[0]))
                print("item_id     : " + str(row[1]))
                print("description : " + str(row[2]))
                print("item_cost   : " + str(row[3]))
                print("date_placed : " + str(row[4]))
                print("date_shipped: " + str(row[5]))

                print("is_delivered: " + str(row[7]))
                print("quantity    : " + str(row[8]))
        finally:
            cursor.close()

    def delete_customer(self, customer_id):
        cursor = self.connection.cursor()
        sql = "delete from customer where customer_id = ?"
        params = (customer_id,)
        cursor.execute(sql, params)
        cursor.close()

    def delete_orderlog(self, customer_id, item_id):
        cursor = self.connection.cursor()
        sql = "delete from orderlog where customer_id = ? and item_id = ?"
        params = (customer_id, item_id)
        cursor.execute(sql, params)
        cursor.close()


def main():
    customer_id = 1
    item_id = 1

    # Make sure connection is always closed in order to close and release
    # server connection into the pool

    connection = MyRemoteConnection.remote_connection_builder()
    my_remote_connection = MyRemoteConnection(connection)

    print("deleting customer...")
    # Delete previous instances, so that user can recall class
    my_remote_connection.delete_customer(customer_id)
    print("deleting orderlog...")
    my_remote_connection.delete_orderlog(customer_id, item_id)

    my_remote_connection.insert_customer_and_order_log(customer_id, item_id)
    my_remote_connection.select_customer_and_orderlog(customer_id, item_id)


if __name__ == '__main__':
    main()

