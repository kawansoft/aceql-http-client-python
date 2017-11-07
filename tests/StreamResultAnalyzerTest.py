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

import unittest

from aceql._private.StreamResultAnalyzer import *

from aceql._private.FileUtil import *


class StreamResultAnalyzerTest(unittest.TestCase):
    def test_A(self):

        filename = os.getcwd() + sep + "files" + sep + "exception.txt"
        streamResultAnalyzer = StreamResultAnalyzer(filename, 200)

        isOk = streamResultAnalyzer.isStatusOk()
        print("status: " + str(streamResultAnalyzer.isStatusOk()))

        self.assertEqual(isOk, False)

        # {
        #   "status":"FAIL",
        #   "error_type":1,
        #   "error_message":"ERREUR: la colonne « customer_id1 » n'existe pas\n
        #   Position : 38",
        #   "http_status":400
        # }

        if not isOk:
            print("error_type: " + str(streamResultAnalyzer.getErrorType()))
            print("error_message: " + streamResultAnalyzer.getErrorMessage())

            self.assertEqual(streamResultAnalyzer.getErrorType(), 1)
            self.assertEqual(streamResultAnalyzer.getErrorMessage()[:18], "ERREUR: la colonne")

            if streamResultAnalyzer.getStackTrace() is not None:
                print("statck_trace: " + streamResultAnalyzer.getStackTrace())

        else:
            print("status OK!")


if __name__ == '__main__':
    unittest.main()