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

import sys
from datetime import datetime

from aceql._private.cursor_util import CursorUtil


class TypesDisplayUtil:

    @staticmethod
    def test_csharp_types() -> None:
        my_bool = True
        my_short = 1
        my_int = int(42)
        my_string = "myString"
        mystring = "mystring"
        my_float = float(42)
        my_double = 42.42
        my_long = 2147483647 + 1000

        # datetime_util.py for conversion
        my_date_time = datetime.now()
        print("bool    : " + str(type(my_bool)))
        print("short   : " + str(type(my_short)))
        print("int     : " + str(type(my_int)))
        print("String  : " + str(type(my_string)))
        print("string  : " + str(type(mystring)))
        print("float   : " + str(type(my_float)))
        print("double  : " + str(type(my_double)))
        print("long    : " + str(type(my_long)))
        print("datetime.datetime: " + str(type(my_date_time)))
        print("")
        print("CursorUtil.get_class_name:")
        print("bool    : " + CursorUtil.get_class_name(my_bool))
        print("short   : " + CursorUtil.get_class_name(my_short))
        print("int     : " + CursorUtil.get_class_name(my_int))
        print("String  : " + CursorUtil.get_class_name(my_string))
        print("string  : " + CursorUtil.get_class_name(mystring))
        print("float   : " + CursorUtil.get_class_name(my_float))
        print("double  : " + CursorUtil.get_class_name(my_double))
        print("long    : " + CursorUtil.get_class_name(my_long))
        print("datetime.datetime: " + CursorUtil.get_class_name(my_date_time))
        print("")

        sys.stdin.readline()


if __name__ == '__main__':
    TypesDisplayUtil.test_csharp_types()