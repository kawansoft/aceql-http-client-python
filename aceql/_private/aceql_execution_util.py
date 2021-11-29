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

class AceQLExecutionUtil(object):
    """Utilities for SQL execution """

    @staticmethod
    def check_values(is_prepared_statement: bool, sql: str):
        if sql is None:
            raise TypeError("sql is null!")
        if is_prepared_statement is None:
            raise TypeError("isPreparedStatement is null!")

    @staticmethod
    def set_is_prepared_statement(dict_params: dict, is_prepared_statement: bool):
        if str(is_prepared_statement) == 'True':
            dict_params["prepared_statement"] = "true"
        else:
            dict_params["prepared_statement"] = "false"
