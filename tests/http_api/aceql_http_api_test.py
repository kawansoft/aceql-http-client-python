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

from aceql._private.aceql_http_api import AceQLHttpApi
from aceql._private.file_util import FileUtil


class AceQLHttpApiTest(object):
    """description of class"""

    @staticmethod
    def do_it():

        aceql_http_api = AceQLHttpApi("http://localhost:9090/aceql", "user1", "password1", "sampledb")
        print("connect done!")

        print("client version: " + aceql_http_api.get_client_version())
        print("server version: " + aceql_http_api.get_server_version())

        auto_commit = aceql_http_api.get_auto_commit()
        print("auto_commit: " + str(auto_commit))

        aceql_http_api.set_auto_commit(False)
        auto_commit = aceql_http_api.get_auto_commit()
        print("auto_commit: " + str(auto_commit))

        aceql_http_api.commit()
        aceql_http_api.rollback()
        aceql_http_api.set_auto_commit(True)

        auto_commit = aceql_http_api.get_auto_commit()
        print("auto_commit: " + str(auto_commit))

        holdability = aceql_http_api.get_holdability()
        print("holdability: " + holdability)

        transaction_isolation = aceql_http_api.get_transaction_isolation()
        print("transaction_isolation: " + transaction_isolation)

        read_only = aceql_http_api.is_read_only()
        print("readOnly: " + str(read_only))

        print()
        sql = "update customer set fname = ? where customer_id = ?"
        is_prepared_statement = True

        statement_parameters = {}
        statement_parameters["param_type_1"] = "VARCHAR"
        statement_parameters["param_value_1"] = "Nicolas"
        statement_parameters["param_type_2"] = "INTEGER"
        statement_parameters["param_value_2"] = "1"

        result = aceql_http_api.execute_update(sql, is_prepared_statement, statement_parameters)
        print("result: " + str(result))

        status_code = aceql_http_api.get_http_status_code()
        print("statusCode: " + str(status_code))

        status_message = aceql_http_api.get_http_status_message()
        print("status_message: " + str(status_message))
        print()

        print("UUID: " + FileUtil.get_unique_id())
        print("Home: " + FileUtil.get_user_home_dot_kawansoft_dir())
        print("Tmp : " + FileUtil.get_kawansoft_temp_dir())
        print()

        statement_parameters2 = {}
        statement_parameters2["param_type_1"] = "INTEGER"
        statement_parameters2["param_value_1"] = "0"
        sql = "select * from customer where customer_id >= ? order by customer_id"
        aceql_http_api.set_pretty_printing(True)

        result = aceql_http_api.execute_query(sql, is_prepared_statement, statement_parameters2)
        print("result: " + str(result))
        print()
