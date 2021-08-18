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

from aceql._private.result_analyzer import ResultAnalyzer


class ResultAnalyzerTest(unittest.TestCase):

    def test_A(self):
        result = '{"status" : "OK","session_id" : "mn7andp2tt049iaeaskr28j9ch"}'
        analyzer = ResultAnalyzer(result, 200)
        status_ok = analyzer.is_status_ok()

        self.assertEqual(status_ok, True)
        session_id = analyzer.get_value("session_id")
        self.assertEqual(session_id, "mn7andp2tt049iaeaskr28j9ch")

        print("ResultAnalyzerTest Passed!")


if __name__ == '__main__':
    unittest.main()
