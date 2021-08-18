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

import unittest

from datetime import date, datetime
from aceql._private.cursor_util import CursorUtil
from aceql.sql_null_type import SqlNullType


class CursorUtilTest(unittest.TestCase):
    def test_A(self):
        the_datetime = datetime.now()
        the_date = date(2017, 10, 31)
        the_time = the_datetime.time()

        # for NULL values
        tup_null_integer = None, SqlNullType.INTEGER

        the_list = [tup_null_integer, 1, 12.53, True, "text", the_datetime, the_date, the_time]

        cpt = 0
        for x in the_list:
            print()
            print(str(x) + " / type: " + str(type(x)))
            sql_type = CursorUtil.get_sql_type(x)
            print("sql_type : " + sql_type)

            if cpt == 0:
                self.assertEqual(sql_type, "TYPE_NULL4")

            if cpt == 1:
                self.assertEqual(sql_type, "INTEGER")

            if cpt == 2:
                self.assertEqual(sql_type, "REAL")

            if cpt == 3:
                self.assertEqual(sql_type, "BIT")

            if cpt == 4:
                self.assertEqual(sql_type, "VARCHAR")

            if cpt == 5:
                self.assertEqual(sql_type, "TIMESTAMP")

            if cpt == 6:
                self.assertEqual(sql_type, "DATE")

            if cpt == 7:
                self.assertEqual(sql_type, "TIME")

            cpt += 1


if __name__ == '__main__':
    unittest.main()
