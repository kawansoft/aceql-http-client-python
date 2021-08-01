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

from aceql._private.batch import prep_statement_params_holder
from aceql._private.batch import prepared_statements_batch_dto
from datetime import datetime
import marshmallow_dataclass

from aceql._private.batch.prep_statement_params_holder import PrepStatementParametersHolder
from aceql._private.batch.prepared_statements_batch_dto import PreparedStatementsBatchDto

my_rows: list = [int]
my_rows.append(12)
my_rows.append(13)
my_rows.append(14)
print(my_rows)

preparedStatement: dict = {}
preparedStatement["param_type_1"] = "int"
preparedStatement["param_value_1"] = "12"
preparedStatement["param_type_2"] = "string"
preparedStatement["param_value_2"] = "my_value"

preparedStatement2: dict = {}
preparedStatement2["param_type_1"] = "int"
preparedStatement2["param_value_1"] = "13"
preparedStatement2["param_type_2"] = "string"
preparedStatement2["param_value_2"] = "my_new_value"

prep_statement_parameters_holder_schema = marshmallow_dataclass.class_schema(PrepStatementParametersHolder)
prep_statement_parameters_holder: PrepStatementParametersHolder = PrepStatementParametersHolder(
    statement_parameters=preparedStatement)

print(prep_statement_parameters_holder)

json_string: str = prep_statement_parameters_holder_schema().dumps(prep_statement_parameters_holder)
print(json_string)

prep_statement_parameters_holder_list1: list = []
prep_statement_parameters_holder_list1.append(preparedStatement)
prep_statement_parameters_holder_list1.append(preparedStatement2)

print()
print("prep_statement_parameters_holder_list1: " + str(prep_statement_parameters_holder_list1))

prepared_statements_batch_dto_schema = marshmallow_dataclass.class_schema(PreparedStatementsBatchDto)
prepared_statements_batch_dto = PreparedStatementsBatchDto(prep_statement_params_holder_list = prep_statement_parameters_holder_list1)
print(prepared_statements_batch_dto)
print()

json_string2: str = prepared_statements_batch_dto_schema().dumps(prepared_statements_batch_dto)
print("json_string2: " + json_string2)
print()

prepared_statements_batch_dto_back: PreparedStatementsBatchDto = prepared_statements_batch_dto_schema().loads(json_string2)
print("prepared_statements_batch_dto_back: " + str(prepared_statements_batch_dto_back))
print()

prep_statement_parameters_holder_list_back = prepared_statements_batch_dto_back.prep_statement_params_holder_list
print("prep_statement_parameters_holder_list_back:")
for preparedStatementBack in prep_statement_parameters_holder_list_back:
    print("preparedStatementBack: " + str(preparedStatementBack))

print()
print(str(datetime.now) + " End.")

