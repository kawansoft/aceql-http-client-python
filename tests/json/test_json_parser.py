# -*- coding: utf-8 -*-
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

import unittest
import sys
import os
import ijson


class TestAll(unittest.TestCase):
    def test_A(self):

        print(sys.version)

        filename = os.getcwd() + os.sep + "files" + os.sep + "result-set.txt"
        print("filename: " + filename)

        with open(filename, 'rb') as input_file:
            # load json iteratively
            parser = ijson.parse(input_file)
            for prefix, event, value in parser:
               print('prefix={}, event={}, value={}'.format(prefix, event, value))

        with open(filename, 'rb') as input_file:
            events = ijson.basic_parse(input_file)
            for value in events:
                print(str(value))


if __name__ == '__main__':
    unittest.main()
