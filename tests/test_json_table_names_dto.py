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

import marshmallow_dataclass

from aceql._private.table_names_dto import TableNamesDto

table_names_dto_schema = marshmallow_dataclass.class_schema(TableNamesDto)
table_names = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# 1) Create the DTO  class instance
table_names_dto_0: TableNamesDto = TableNamesDto (status="OK", tableNames=table_names)
print(table_names_dto_0)

# 2) Transform the DTO class instance to Json with dumps():
my_str: str = table_names_dto_schema().dumps(table_names_dto_0)
print(my_str)

# 3) Transform back the Json string to DTO new class instance with loads()
result: str = my_str
table_names_dto: TableNamesDto = table_names_dto_schema().loads(result)
print()
print(table_names_dto)