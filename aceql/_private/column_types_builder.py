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

import collections
import json
import os
from io import open


class ColumnTypesBuilder(object):
    """Allows to build the dictionary of SQL types per coumn index of a
       valid result set file (no check is done)"""

    def __init__(self, filename: str):
        self.__filename = filename

        if filename is None:
            raise TypeError("filename is null!")

        if not os.path.isfile(filename):
            raise IOError("filename does not exist: " + str(filename))

    def get_types_per_col_index(self) -> dict:
        with open(self.__filename, 'r') as fd:
            s = ""
            while True:
                line = fd.readline()
                if line == '':
                    break
                line = line.strip()
                # end of "column_types" array: close the JSON and quit
                if line == "],":
                    s += "]}"
                    break
                s += line

            j = json.loads(s, object_pairs_hook=collections.OrderedDict)
            list_column_types = j["column_types"]

            # debug("list_column_types: " + str(list_column_types))

            dict_column_types: dict = {}

            # index = 0
            # for s in list_column_types:
            # 	dict_column_types[index] = s
            # 	index +=1

            index = 0
            while index < len(list_column_types):
                dict_column_types[index] = list_column_types[index]
                index += 1

            # print("dict_column_types: " + str(dict_column_types))
            return dict_column_types
