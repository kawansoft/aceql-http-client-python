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


class ResultSetInfo(object):
    """Gives two info on result set
    1) the local filename,
    2) the number of rows"""

    def __init__(self, filename: str, row_count: int):
        self.__filename = filename
        self.__row_count = row_count

    def get_filename(self) -> str:
        return self.__filename

    def get_row_count(self) -> int:
        return self.__row_count

    def __str__(self):
        """ The string representation."""
        return str(self.__filename) + ", " + str(self.__row_count)