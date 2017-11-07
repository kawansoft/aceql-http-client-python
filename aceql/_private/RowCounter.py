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

import os
from io import open

from aceql._private.AceQLDebug import *


class RowCounter(object):
    """Allows to count rows in retrieved JSON result set"""

    def __init__(self, filename):
        self.__filename = filename

        if filename is None:
            raise TypeError("filename is null!")

        if not os.path.isfile(filename):
            raise IOError("filename does not exist: " + str(filename))

    def count(self):
        """Returns the number of rows in JSON file (key "row_count") """
        with open(self.__filename, mode="r", encoding="utf-8") as fd:
            rows = 0
            while (True):
                s = fd.readline()
                if s == '':
                    break
                s = s.strip()
                if s.startswith("\"row_count\":"):
                    count_str = s[12:]
                    AceQLDebug.debug("countStr: " + count_str + "!")
                    rows = int(count_str)
                AceQLDebug.debug(s)
            return rows
