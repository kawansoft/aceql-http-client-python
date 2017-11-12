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

from aceql._private.aceql_http_api import *
from aceql._private.file_util import *


class AceQLHttpApiTest(object):
    """description of class"""

    def doIt(self):
        AceQLHttpApi.set_stateless(True)
        isStateless = AceQLHttpApi.is_stateless()
        print("isStateless: " + str(isStateless))

        AceQLHttpApi.set_stateless(False)
        isStateless = AceQLHttpApi.is_stateless()
        print("isStateless: " + str(isStateless))

        aceQLHttpApi = AceQLHttpApi("http://localhost:9090/aceql", "kawansoft_example", "user1", "password1")
        print("connect done!")

        print("client version: " + aceQLHttpApi.get_client_version())
        print("server version: " + aceQLHttpApi.get_server_version())

        autoCommit = aceQLHttpApi.get_auto_commit()
        print("autoCommit: " + str(autoCommit))

        aceQLHttpApi.set_auto_commit(False)
        autoCommit = aceQLHttpApi.get_auto_commit()
        print("autoCommit: " + str(autoCommit))

        aceQLHttpApi.commit()
        aceQLHttpApi.rollback()
        aceQLHttpApi.set_auto_commit(True)

        autoCommit = aceQLHttpApi.get_auto_commit()
        print("autoCommit: " + str(autoCommit))

        holdability = aceQLHttpApi.get_holdability()
        print("holdability: " + holdability)

        transactionIsolation = aceQLHttpApi.get_transaction_isolation()
        print("transactionIsolation: " + transactionIsolation)

        readOnly = aceQLHttpApi.is_read_only()
        print("readOnly: " + str(readOnly))

        print()
        sql = "update customer set fname = ? where customer_id = ?"
        isPreparedStatement = True

        statementParameters = {}
        statementParameters["param_type_1"] = "VARCHAR"
        statementParameters["param_value_1"] = "Nicolas"
        statementParameters["param_type_2"] = "INTEGER"
        statementParameters["param_value_2"] = "1"

        result = aceQLHttpApi.execute_update(sql, isPreparedStatement, statementParameters)
        print("result: " + str(result))

        statusCode = aceQLHttpApi.get_http_status_code()
        print("statusCode: " + str(statusCode))

        statusMessage = aceQLHttpApi.get_http_status_message()
        print("statusMessage: " + str(statusMessage))
        print()

        print("UUID: " + FileUtil.get_unique_id())
        print("Home: " + FileUtil.get_user_home_dot_kawansoft_dir())
        print("Tmp : " + FileUtil.get_kawansoft_temp_dir())
        print()

        statementParameters2 = {}
        statementParameters2["param_type_1"] = "INTEGER"
        statementParameters2["param_value_1"] = "0"
        sql = "select * from customer where customer_id >= ? order by customer_id"
        aceQLHttpApi.set_pretty_printing(True)

        result = aceQLHttpApi.execute_query(sql, isPreparedStatement, statementParameters2)
        print("result: " + str(result))
        print()
