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
from tests.util.connection_builder import ConnectionBuilder
from tests.dml.dml_sequence_test import DmlSequenceTest
from tests.dml_batch.sql_batch_test import SqlBatchTest


class DmlTest(object):

    def __init__(self):
        print("Contructor.")

    def do_it(self):
        connection: Connection = ConnectionBuilder.get_connection()
        try:
            dml_sequence_test: DmlSequenceTest = DmlSequenceTest(connection)
            dml_sequence_test.test_sequence()
        finally:
            connection.close()

        connection = ConnectionBuilder.get_connection()
        try:
            sql_batch_test: SqlBatchTest = SqlBatchTest(connection)
            sql_batch_test.insert_using_batch()
        finally:
            connection.close()


if __name__ == '__main__':
     dmlTest: DmlTest = DmlTest()
     dmlTest.do_it()