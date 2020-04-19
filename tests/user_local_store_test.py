#
# This file is part of AceQL Python Client SDK.
# AceQL Python Client SDK: Remote SQL access over HTTP with AceQL HTTP.
# Copyright (C) 2020,  KawanSoft SAS
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

from aceql._private.user_login_store import *

user_login_store= UserLoginStore("http://localhost:9090/aceql", "username", "sampledb")
user_login_store.set_session_id("session_id_value")

if user_login_store.is_already_logged():
    print("User is already logged!")
    print("sesssion_id: " + user_login_store.get_session_id())
else:
    print("User is not logged.")

user_login_store.remove()

if user_login_store.is_already_logged():
    print("User is already logged!")
    print("sesssion_id: " + user_login_store.get_session_id())
else:
    print("User is not logged.")



