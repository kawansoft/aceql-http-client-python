# -*- coding: utf-8 -*-
#
# This file is part of AceQL Python Client SDK.
# AceQL Python Client SDK: Remote SQL access over HTTP with AceQL HTTP.
# Copyright (C) 2020,  KawanSoft SAS
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

import unittest

from aceql._private.row_parser import *
from aceql._private.row_counter import *
from aceql._private.file_util import *


class RowParserTest(unittest.TestCase):
    def test_A(self):
        filename = os.getcwd() + sep + "files" + sep + "result-set.txt"

        row_counter = RowCounter(filename)
        row_cout = row_counter.count()
        print("row_count: " + str(row_cout))

        row_parser = None
        try:
            row_parser = RowParser(filename, row_cout)
            row_parser.build_next_row()

            values_per_col_index = row_parser.get_values_per_col_index()
            types_per_col_index = row_parser.get_types_per_col_index()

            print("values per col index: " + str(values_per_col_index))
            print("types per col index : " + str(types_per_col_index))

            self.assertEqual(values_per_col_index[0], 0)
            self.assertEqual(values_per_col_index[1], "Sir ")
            self.assertEqual(values_per_col_index[2], u"André_0")
            self.assertEqual(values_per_col_index[3], "Name_0")
            self.assertEqual(values_per_col_index[4], "0, road 66")
            self.assertEqual(values_per_col_index[5], "Town_0")
            self.assertEqual(str(values_per_col_index[6]).strip(), "01111")
            self.assertEqual(values_per_col_index[7], "NULL")

            self.assertEqual(types_per_col_index[0], "INTEGER")
            self.assertEqual(types_per_col_index[1], "CHAR")
            self.assertEqual(types_per_col_index[2], "VARCHAR")
            self.assertEqual(types_per_col_index[3], "VARCHAR")
            self.assertEqual(types_per_col_index[4], "VARCHAR")
            self.assertEqual(types_per_col_index[5], "VARCHAR")
            self.assertEqual(types_per_col_index[6], "CHAR")
            self.assertEqual(types_per_col_index[7], "VARCHAR")
        finally:
            row_parser.close()

        # loop test
        try:
            row_parser = RowParser(filename, row_cout)

            cpt = 0

            while True:

                if row_parser.build_next_row():
                    values_per_col_index = row_parser.get_values_per_col_index()
                    types_per_col_index = row_parser.get_types_per_col_index()
                    print()
                    print("cpt: " + str(cpt))
                    print("values per col name : " + str(types_per_col_index))
                    print("values per col index: " + str(values_per_col_index))
                    cpt += 1
                else:
                    break

            self.assertEqual(cpt, 3)
            print("Done!")

        finally:
            row_parser.close()


if __name__ == '__main__':
    unittest.main()
