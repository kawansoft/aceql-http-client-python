# -*- coding: utf-8 -*-
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

# P2
# <type 'datetime.datetime'>
# <type 'datetime.date'>
# <type 'datetime.time'>
# <type 'file'>

# P3
# <class 'datetime.datetime'>
# <class 'datetime.date'>
# <class 'datetime.time'>
# <class '_io.BufferedReader'>

import StringIO
from datetime import datetime, date,  time

datetimeNow = datetime.now()
date = datetimeNow.date()
theTime = time(12, 40)
fd = open("c:\\test\\koala.jpg" ,"rb")

print(str(type(datetimeNow)))
print(str(type(date)))
print(str(type(theTime)))
print(str(type(fd)))

input = StringIO.StringIO()
input.write("line1\n")
input.write("line2\n")

input.readlines()