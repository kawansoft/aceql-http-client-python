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

from aceql._private.datetime_util import *


class DateTimeUtilTest(unittest.TestCase):
    def test_A(self):

        the_datetime = datetime.now()
        print("theDatetime       : " + str(the_datetime))

        timestamp_str = DateTimeUtil.get_timestamp_from_date(the_datetime)
        print("timestamp_str     : " + timestamp_str)

        the_datetime_new = DateTimeUtil.get_datetime_from_timestamp(timestamp_str)
        print("the_datetime_new  : " + str(the_datetime_new))

        timestamp_str_new = DateTimeUtil.get_timestamp_from_date(the_datetime_new)
        print("timestamp_str_new : " + timestamp_str_new)

        self.assertEqual(timestamp_str, timestamp_str_new)

    def print_datetime_values(self):
        the_datetime = datetime.now()
        the_date = the_datetime.date()
        the_time = the_datetime.time()

        print()
        print("the_datetime: " + str(type(the_datetime)))
        print("the_date    : " + str(type(the_date)))
        print("the_time    : " + str(type(the_time)))
        print()
        print("the_datetime: " + str(the_datetime))
        print("the_date    : " + str(the_date))
        print("the_time    : " + str(the_time))
        print()
        print("the_time hour   : " + str(the_time.hour))
        print("the_time minute : " + str(the_time.minute))
        print("the_time second : " + str(the_time.second))
        print("the_time micros : " + str(the_time.microsecond))

if __name__ == '__main__':
    unittest.main()
