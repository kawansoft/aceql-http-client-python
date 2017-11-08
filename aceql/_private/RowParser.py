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

import collections
import json
import os
from io import open

from aceql._private.ColumnTypesBuilder import *
from aceql._private.AceQLDebug import *

class RowParser(object):
    """Allows to parse rows in retrieved JSON result set and return each row content dictionaries"""

    def __init__(self, filename, row_count):
        self.__filename = filename
        self.__last_row = 1
        self.__row_count = row_count
        self.__rows_parsed = 0

        self.__column_names_per_index = {}
        self.__values_per_col_index = {}
        self.__types_per_col_index = {}

        if filename is None:
            raise TypeError("filename is null!")

        if not os.path.isfile(filename):
            raise IOError("filename does not exist: " + str(filename))

        # Builds the column types
        column_types_builder = ColumnTypesBuilder(filename)
        self.__types_per_col_index = column_types_builder.get_types_per_col_index()

        self.__fd = open(filename, mode="r", encoding="utf-8")

        # Go to row_1
        while True:
            s = self.__fd.readline()
            if s == '':
                break
            s = s.strip()
            if s == "\"row_1\":[":
                break

    def build_next_row(self):
        """Build the dictionaries of values per column name & values per column index for the next row"""

        # No parse of course if no rows in file...
        if self.__row_count == 0:
            return False

        # Stop parsing if end of file reached
        if self.__rows_parsed >= self.__row_count:
            self.__column_names_per_index = {}
            self.__values_per_col_index = {}
            return False

        s = ""
        while True:
            line = self.__fd.readline()
            if line == '':
                break
            line = line.strip()
            if line == ("\"row_" + str(self.__last_row + 1) + "\":["):
                self.__last_row += 1
                break

            # Case last row
            if self.__last_row == self.__row_count:
                if line == "]":
                    self.__last_row += 1
                    break

            # doe not include closing array bracket
            if not line.startswith("]"):
                s += line

        if s == '':
            return

        # AceQLDebug.print("s:" + s)
        AceQLDebug.debug("")
        AceQLDebug.debug("s               : " + s)
        AceQLDebug.debug("self.__last_row : " + str(self.__last_row))

        s = s.replace("{", "")
        s = s.replace("}", "")
        s = "{" + s + "}"
        resp = json.loads(s, object_pairs_hook=collections.OrderedDict)

        index = 0
        for key, value in resp.items():
            # AceQLDebug.debug("key/value: " + str(key) + " " + str(value))
            self.__column_names_per_index[index] = key
            self.__values_per_col_index[index] = value
            index += 1
        # AceQLDebug.debug("key: %s , value: %s" % (key, self.__values_per_col_name [key]))

        self.__rows_parsed += 1
        return True

    def column_names_per_index(self):
        """Returns the dictionary of column names per column index, starting at 0 """
        return self.__column_names_per_index

    def get_values_per_col_index(self):
        """Returns the dictionary of values per column index, starting at 0 """
        return self.__values_per_col_index

    def get_types_per_col_index(self):
        """Returns the dictionary of type per column index, starting at 0 """
        return self.__types_per_col_index

    def get_row_cout(self):
        return self.__row_count

    def close(self):
        """Mandatory close at end of use"""
        self.__fd.close()
