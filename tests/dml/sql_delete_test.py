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

from aceql import Connection


class SqlDeleteTest(object):
    """Delete all rows of customer and orderlog tables."""

    def __init__(self, connection: Connection):
        self.__connection = connection

    def delete_customer_all(self):
        sql = "delete from customer where customer_id >= ?"
        params = (0,)
        cursor = self.__connection.cursor()
        cursor.execute(sql, params)
        cursor.close()

    def delete_orderlog_all(self):
        sql = "delete from orderlog where customer_id >= ?"
        params = (0,)
        cursor = self.__connection.cursor()
        cursor.execute(sql, params)
        cursor.close()