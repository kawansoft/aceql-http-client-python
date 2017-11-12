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


class SqlNullType(object):
    """Defines nullable SQL Types when setting a SQL parameter to NULL.

        To set a prepared statement to NULL, set the value to a tuple (None, SqlNullType.<SQL_TYPE>).
        Example: set to NULL an INTEGER column ==>  (None, SqlNullType.INTEGER) """

    BIT = -7
    TINYINT = -6
    SMALLINT = 5
    INTEGER = 4
    BIGINT = -5
    FLOAT = 6
    REAL = 7
    DOUBLE = 8
    NUMERIC = 2
    DECIMAL = 3
    CHAR = 1
    VARCHAR = 12
    DATE = 91
    TIME = 92
    TIMESTAMP = 93
    BLOB = 2004
    CLOB = 2005
    BOOLEAN = 16
