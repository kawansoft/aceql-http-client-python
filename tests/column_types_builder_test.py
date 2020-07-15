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

from aceql._private.column_types_builder import *
from aceql._private.file_util import *


class ColumnTypesBuilderTest(unittest.TestCase):
    def test_A(self):
        filename = os.getcwd() + sep + "files" + sep + "result-set.txt"
        column_types_builder = ColumnTypesBuilder(filename)
        dict_column_types = column_types_builder.get_types_per_col_index()
        print(dict_column_types)

        self.assertEqual(dict_column_types[0], "INTEGER")
        self.assertEqual(dict_column_types[1], "CHAR")
        self.assertEqual(dict_column_types[2], "VARCHAR")
        self.assertEqual(dict_column_types[3], "VARCHAR")
        self.assertEqual(dict_column_types[4], "VARCHAR")
        self.assertEqual(dict_column_types[5], "VARCHAR")
        self.assertEqual(dict_column_types[6], "CHAR")
        self.assertEqual(dict_column_types[7], "VARCHAR")


if __name__ == '__main__':
    unittest.main()
