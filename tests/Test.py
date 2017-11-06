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

import sys

from aceql.Error import *
from aceql.SqlNullType import *

the_type = SqlNullType.INTEGER

x = 12

if isinstance(x, int):
    print ("OK")
else:
    print ("KO")

print(sys.version_info)

do_raise = False

if do_raise:

    raise Error("The error message", 0, None, None, 200)

    # try:
    #     pass
    # except Exception as e:
    #     print(str(e))

try:

    raise Error("SQL error message", 2, None, "stackTrace", 200)

except Exception as e:
    if type(e) == Error:
        print("Before raise alone")
        raise
    else:
        raise Error(str(e), 0, e, None, 200)
