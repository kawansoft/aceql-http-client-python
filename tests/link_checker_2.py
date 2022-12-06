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

import os
import sys
from datetime import datetime

import regex
import requests

# cd I:\_dev_awake\aceql-http-main\Python\aceql-http-client-python\tests

# Server
# python link_checker_2.py I:\_dev_awake\aceql-http-main\aceql-http\README.md
# python link_checker_2.py I:\_dev_awake\aceql-http-main\aceql-http\aceql-http-demo-guide.md
# python link_checker_2.py I:\_dev_awake\aceql-http-main\aceql-http\aceql-http-user-guide-api.md

# C#
# python link_checker_2.py I:\_dev_awake\aceql-http-main\C#\AceQL.Client2\README.md

# JDBC
# python link_checker_2.py I:\_dev_awake\aceql-http-main\aceql-http-client-jdbc-driver\README.md

# Python
# python link_checker_2.py I:\_dev_awake\aceql-http-main\Python\aceql-http-client-python\README.md

command_line = False

#the_doc = "I:\\_dev_awake\\aceql-http-main\\C#\\AceQL.Client2\\README.md"
#the_doc = "I:\\_dev_awake\\aceql-http-main\\aceql-http\\aceql-http-demo-guide.md"
#the_doc = "I:\\_dev_awake\\aceql-http-main\\aceql-http\\aceql-http-user-guide-api.md"

#the_doc = "I:\\_dev_awake\\aceql-http-main\\C#\\AceQL.Client2\\README.md"
#the_doc = "I:\\_dev_awake\\aceql-http-main\\aceql-http-client-jdbc-driver\\README.md"
the_doc = "I:\\_dev_awake\\aceql-http-main\\Python\\aceql-http-client-python\\README.md"

if command_line:
    if len(sys.argv) < 2:
        print("Please pass markdown file as parameter!")
        sys.exit()

    md_file:str = sys.argv[1]
else:
    md_file: str = the_doc

only_false:bool = False

if len(sys.argv) == 3:
    only_false = sys.argv[2]

#print(md_file)

if not os.path.isfile(md_file):
    print("Invalid file: " + md_file )
    sys.exit()

print(str(datetime.now()) + " Starting scan...")

with open (md_file, "r") as myfile:
    body_markdown=myfile.read()

rex = """(?|(?<txt>(?<url>(?:ht|f)tps?://\S+(?<=\P{P})))|\(([^)]+)\)\[(\g<url>)\])"""
pattern = regex.compile(rex)
matches = regex.findall(pattern, body_markdown, overlapped=True)
for m in matches:
    url: str = m[0]
    if not url.__contains__("localhost") and not url.__contains__(".acme.com") and not url.__contains__("acme.org"):
        if not only_false:
            print("Testing " + url + "...")

        try:
            request_response = requests.head(url, timeout=3)
            status_code = request_response.status_code
            website_is_up = False
            if status_code == 200 or status_code == 301 or status_code == 302 or status_code == 305 or status_code == 306 or status_code == 307:
                website_is_up = True
            if not website_is_up:
                print(str(website_is_up) + " " + str(status_code) + " " + url)
        except requests.exceptions.RequestException as e:
            print(str(False) + " Probably Timeout " + url)

print(str(datetime.now()) + " Done!")