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

import json
import os
from io import open
# -*- coding: utf-8 -*-
from aceql._private.AceQLDebug import *
from aceql._private.CursorUtil import *

class StreamResultAnalyzer(object):
    """ <summary>
     Class <see cref="StreamResultAnalyzer"/>. Allows to analyze the result of a downloaded result of a SQL query stored in a local PC file.
     </summary>
    """

    # <summary>
    # The error identifier
    # </summary>
    # <summary>
    # The error message
    # </summary>
    # <summary>
    # The stack trace
    # </summary>
    # The JSON file containing Result Set
    def __init__(self, filename, httpStatusCode):
        """ <summary>
         Initializes a new instance of the <see cref="StreamResultAnalyzer"/> class.
         </summary>
         <param name="filename">The file to analyze.</param>
         <param name="httpStatusCode">The http status code.</param>
         <exception cref="System.ArgumentNullException">The file is null.</exception>
        """

        if filename is None:
            raise TypeError("filename is null!")

        if not os.path.isfile(filename):
            raise FileNotFoundError("filename does not exist: " + str(filename))

        self.__filename = filename
        self.__httpStatusCode = httpStatusCode

        self.__error_type = None
        self.__error_message = None
        self.__stack_trace = None

    def isStatusOk(self):
        """ <summary>
         Determines whether the SQL correctly executed on server side.
         </summary>
         <returns><c>true</c> if [is status ok]; otherwise, <c>false</c>.</returns>
        """
        with open(self.__filename, mode="r", encoding="utf-8") as fd:
            status_ok = False
            while True:
                s = fd.readline()
                if s == '':
                    break
                s = s.strip()
                AceQLDebug.debug(s)
                if s.startswith("\"status\":"):
                    AceQLDebug.debug("status: " + s + "!")
                    if s.endswith("\"OK\","):
                        status_ok = True
                        break;

        if not status_ok:
            self.parseErrorKeywords()

        return status_ok

    def parseErrorKeywords(self):
        """ <summary>
         Parses the error keywords.
         </summary>
         <param name="reader">The reader.</param>
        """

        """
        while reader.Read():
            if reader.Value == None:
                continue
            if reader.TokenType == JsonToken.PropertyName and reader.Value.Equals("error_type"):
                if reader.Read():
                    self._errorType = reader.Value.ToString()
                else:
                    return 
            if reader.TokenType == JsonToken.PropertyName and reader.Value.Equals("error_message"):
                if reader.Read():
                    self._errorMessage = reader.Value.ToString()
                else:
                    return 
            if reader.TokenType == JsonToken.PropertyName and reader.Value.Equals("stack_trace"):
                if reader.Read():
                    self._stackTrace = reader.Value
                else:
                    return 
        """
        with open(self.__filename, mode="r", encoding="utf-8") as fd:
            s = fd.read();
            j = json.loads(s)
            self.__error_type = j["error_type"]
            self.__error_message = j["error_message"]

            try:
                self.__stack_trace = j["stack_trace"]
            except Exception as e:
                # AceQLDebug.print(e)
                pass

            return

    def getErrorMessage(self):
        """ <summary>
         Gets the error message.
         </summary>
         <returns>The error message</returns>
        """
        return self.__error_message

    def getErrorType(self):
        """ <summary>
         Gets the error type.
         </summary>
         <returns>The error type.</returns>
        """
        return self.__error_type

    def getStackTrace(self):
        """ <summary>
         Gets the remote stack trace.
         </summary>
         <returns>The remote stack trace.</returns>
        """
        return self.__stack_trace