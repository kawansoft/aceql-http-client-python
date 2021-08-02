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

from aceql._private.datetime_util import DateTimeUtil
from aceql._private.datetime_util import datetime
from aceql._private.file_util import FileUtil


class CursorUtil(object):
    """Utilities for Cursor class. """

    JAVA_MAX_INT_VALUE = 2147483647

    def __init__(self):
        self.blob_ids = []
        self.blob_streams = []
        self.blob_lengths = []

    def get_http_parameters_dict(self, params: dict) -> dict:
        """ Build the http parameters dictionary to pass to remote server. """
        parms_dict: dict = {}
        param_index = 0

        # Blob lists
        if params is None:
            return parms_dict

        for x in params:
            param_index += 1

            # For Py2 always convert "unicode" aka str with special chars to str
            x = CursorUtil.get_utf8_value(x)

            param_type = CursorUtil.get_sql_type(x)
            parms_dict["param_type_" + str(param_index)] = param_type

            # print(str(param_index) + " param_type: " + str(param_type))

            # NULL values are defined in a (None, SqlNullType.TYPE) typle
            # BLOB values are defined in a (fd,) or (fd, length) tuple where
            # fd = open(filename)
            if CursorUtil.get_class_name(x) == "tuple":
                if param_type == "BLOB":
                    blob_id = FileUtil.get_unique_id() + ".blob"
                    parms_dict["param_value_" + str(param_index)] = blob_id

                    self.blob_ids.append(blob_id)
                    self.blob_streams.append(x[0])

                    if len(x) == 2:
                        self.blob_lengths.append(x[1])
                    else:
                        self.blob_lengths.append(0)
                else:
                    parms_dict["param_value_" + str(param_index)] = "NULL"

            elif CursorUtil.get_class_name(x) == "datetime.datetime":
                parms_dict["param_value_" + str(param_index)] = DateTimeUtil.get_timestamp_from_date(x)
            elif CursorUtil.get_class_name(x) == "datetime.date":
                parms_dict["param_value_" + str(param_index)] = DateTimeUtil.get_timestamp_from_date(x)
            elif CursorUtil.get_class_name(x) == "datetime.time":
                the_datetime = datetime.now()
                the_datetime.hour = x.hour
                the_datetime.minute = x.minute
                the_datetime.second = x.second
                parms_dict["param_value_" + str(param_index)] = DateTimeUtil.get_timestamp_from_date(the_datetime)
            else:
                parms_dict["param_value_" + str(param_index)] = str(x)

        return parms_dict

    @staticmethod
    def get_utf8_value(x: str) -> str:
        """ For python 2: string values with special chars must be UTF-8 encoded """
        if FileUtil.is_python_2() and CursorUtil.get_class_name(x) == "unicode":
            x = x.encode('utf-8')
        return x

    # None / <class 'NoneType'>
    # 1 / <class 'int'>
    # 12.53 / <class 'float'>
    # True / <class 'bool'>
    # text / <class 'str'>
    # 2005-07-14 00:00:00 / <class 'datetime.datetime'>
    # 2005-07-14 / <class 'datetime.date'>
    # 12:30:00 / <class 'datetime.time'>

    @staticmethod
    def get_sql_type(x) -> str:
        """get the SQL type of the passed param value. """

        if x is None:
            raise TypeError("Parameter value is None!")

        if CursorUtil.get_class_name(x) == "tuple":
            if x[0] is None:
                # HACK for BOOL that must be converted to BIT
                # NO! Do not know why. Comment it:
                # if x[1] == SqlNullType.BLOB:
                #   x[1] = SqlNullType.BIT
                sql_type = "TYPE_NULL" + str(x[1])
            elif CursorUtil.get_class_name(x[0]) == "_io.BufferedReader":
                sql_type = "BLOB"
            elif CursorUtil.get_class_name(x[0]) == "file":
                sql_type = "BLOB"
            else:
                raise TypeError("Invalid tuple parameter. Not a NULL Type nor a BLOB: " + str(x))
        # Because P2 int and long are different, and p3 int and long are awlays int, special treatment:
        elif CursorUtil.get_class_name(x) == "int" or CursorUtil.get_class_name(x) == "long":
            if x < CursorUtil.JAVA_MAX_INT_VALUE * -1 or x > CursorUtil.JAVA_MAX_INT_VALUE:
                sql_type = "BIGINT"
            else:
                sql_type = "INTEGER"
        elif CursorUtil.get_class_name(x) == "bool":
            sql_type = "BIT"
        elif CursorUtil.get_class_name(x) == "float":
            sql_type = "REAL"
        elif CursorUtil.get_class_name(x) == "str":
            sql_type = "VARCHAR"
        # NO! unicode is translate to str previously
        # elif CursorUtil.get_class_name(x) == "unicode":
        #    sql_type = "VARCHAR"
        elif CursorUtil.get_class_name(x) == "datetime.datetime":
            sql_type = "TIMESTAMP"
        elif CursorUtil.get_class_name(x) == "datetime.date":
            sql_type = "DATE"
        elif CursorUtil.get_class_name(x) == "datetime.time":
            sql_type = "TIME"
        else:
            raise TypeError("Type is not supported for value: " + str(x))

        return sql_type

    @staticmethod
    def get_class_name(x) -> str:
        """ Parse <class 'class_name'> to get only class_name. """

        s = str(type(x))
        s = s.replace("<class '", "")
        s = s.replace("<type '", "")  # Python2 syntax
        s = s[0:len(s) - 2]
        return s
