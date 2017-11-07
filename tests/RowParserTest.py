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

import unittest

from aceql._private.RowParser import *
from aceql._private.RowCounter import *
from aceql._private.FileUtil import *


class RowParserTest(unittest.TestCase):
    def test_A(self):
        filename = os.getcwd() + sep + "files" + sep + "result-set.txt"

        rowCounter = RowCounter(filename)
        row_cout = rowCounter.count()
        print("row_count: " + str(row_cout))

        rowParser = None
        try:
            rowParser = RowParser(filename, row_cout)
            rowParser.buildNextRow()

            valuesPerColIndex = rowParser.get_values_per_col_index()
            typesPerColIndex = rowParser.get_types_per_col_index()

            print("values per col index: " + str(valuesPerColIndex))
            print("types per col index : " + str(typesPerColIndex))

            self.assertEqual(valuesPerColIndex[0], 0)
            self.assertEqual(valuesPerColIndex[1], "Sir ")
            self.assertEqual(valuesPerColIndex[2], u"André_0")
            self.assertEqual(valuesPerColIndex[3], "Name_0")
            self.assertEqual(valuesPerColIndex[4], "0, road 66")
            self.assertEqual(valuesPerColIndex[5], "Town_0")
            self.assertEqual(str(valuesPerColIndex[6]).strip(), "01111")
            self.assertEqual(valuesPerColIndex[7], "NULL")

            self.assertEqual(typesPerColIndex[0], "INTEGER")
            self.assertEqual(typesPerColIndex[1], "CHAR")
            self.assertEqual(typesPerColIndex[2], "VARCHAR")
            self.assertEqual(typesPerColIndex[3], "VARCHAR")
            self.assertEqual(typesPerColIndex[4], "VARCHAR")
            self.assertEqual(typesPerColIndex[5], "VARCHAR")
            self.assertEqual(typesPerColIndex[6], "CHAR")
            self.assertEqual(typesPerColIndex[7], "VARCHAR")
        finally:
            rowParser.close()

        # loop test
        try:
            rowParser = RowParser(filename, row_cout)

            cpt = 0

            while (True):

                if (rowParser.buildNextRow()):
                    valuesPerColIndex = rowParser.get_values_per_col_index()
                    typesPerColIndex = rowParser.get_types_per_col_index()
                    print()
                    print("cpt: " + str(cpt))
                    print("values per col name : " + str(typesPerColIndex))
                    print("values per col index: " + str(valuesPerColIndex))
                    cpt += 1
                else:
                    break

            self.assertEqual(cpt, 3)
            print("Done!")

        finally:
            rowParser.close()


if __name__ == '__main__':
    unittest.main()
