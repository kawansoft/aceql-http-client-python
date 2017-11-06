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


class ResultAnalyzer(object):
    """ <summary>
     Class <see cref="ResultAnalyzer"/>. Used to analyze a JSON response from the AceQL server.
     </summary>
    """

    # <summary>
    # The json result
    # </summary>
    # <summary>
    # We try to find status.  If error parsing, invalidJsonStream = true
    # </summary>
    # * Exception when parsing the JSON stream.  Future usage
    def __init__(self, jsonResult, httpStatusCode):
        """ <summary>
         Initializes a new instance of the <see cref="ResultAnalyzer"/> class.
         </summary>
         <param name="jsonResult">The json result.</param>
         <param name="httpStatusCode">The http status code.</param>
         <exception cref="System.ArgumentNullException">jsonResult is null!</exception>
        """
        self._invalidJsonStream = False
        self._parseException = None
        self._httpStatusCode = httpStatusCode
        self._jsonResult = jsonResult

    def isStatusOk(self):
        """ <summary>
         Determines whether the SQL command correctly executed on server side.
         </summary>
         <returns><c>true</c> if [is status ok]; otherwise, <c>false</c>.</returns>
        """

        if self._jsonResult == None or len(self._jsonResult) == 0:
            return False
        try:
            j = json.loads(self._jsonResult)
            status = j["status"]
            if status == "OK":
                return True
            else:
                return False
        except Exception as e:
            self._parseException = e
            self._invalidJsonStream = True
            return False

    def isInvalidJsonStream(self):
        """ <summary>
         Says if the JSON Stream is invalid.
         </summary>
         <returns>true if JSN stream is invalid</returns>
        """
        if self._jsonResult == None or len(self._jsonResult) == 0:
            return True
        if self._invalidJsonStream:
            return True
        return False

    def getResult(self, name):
        """ <summary>
         Gets the result for a a key name
         </summary>
         <param name="name">The name.</param>
         <returns>System.String.</returns>
        """
        return self.getValue(name)

    def getResult(self):
        """ <summary>
         Gets the result for the key name "result"
         </summary>
         <returns></returns>
        """
        return self.getValue("result")

    def getValue(self, name):
        """ <summary>
         Gets the value.
         </summary>
         <param name="name">The name.</param>
         <returns>System.String.</returns>
         <exception cref="System.ArgumentNullException">name is null!</exception>
         <exception cref="System.Exception">Illegal name: " + name</exception>
        """
        if name == None:
            raise ArgumentNullException("name is null!")
        if self.isInvalidJsonStream():
            return None

        try:
            j = json.loads(self._jsonResult)

            if name == "session_id":
                value = j[name]
            elif name == "length":
                value = j[name]
            elif name == "result":
                value = j[name]
            elif name == "row_count":
                value = j[name]
            else:
                raise Exception("Illegal name: " + name)
            return value
        except Exception as e:
            self._parseException = e
            self._invalidJsonStream = True
            return None

    def getErrorId(self):
        """ <summary>
         Gets the error_type.
         </summary>
         <returns>System.Int32.</returns>
        """
        if self.isInvalidJsonStream():
            return 0

        try:
            j = json.loads(self._jsonResult)
            errorType = j["error_type"]
            return errorType
        except Exception as e:
            self._parseException = e
            self._invalidJsonStream = True
            return 0

    def getErrorMessage(self):
        """ <summary>
         Gets the error_message.
         </summary>
         <returns>System.String.</returns>
        """
        if self.isInvalidJsonStream():
            theErrorMessage = "Unknown error."
            if self._httpStatusCode != HttpStatusCode.OK:
                theErrorMessage = "HTTP FAILURE " + self._httpStatusCode + " (" + self._httpStatusCode + ")"
            return theErrorMessage
        try:
            j = json.loads(self._jsonResult)
            errorMessage = j["error_message"]
            return errorMessage
        except Exception as e:
            self._parseException = e
            self._invalidJsonStream = True
            return None

    def getStackTrace(self):
        """ <summary>
         Gets the remote stack_trace.
         </summary>
         <returns>String.</returns>
        """
        if self.isInvalidJsonStream():
            return None
        try:
            j = json.loads(self._jsonResult)
            stackTrace = j["stack_trace"]
            return stackTrace
        except Exception as e:
            self._parseException = e
            self._invalidJsonStream = True
            return None

    def getIntvalue(self, name):
        """ <summary>
         Gets the int value.
         </summary>
         <param name="name">The name.</param>
         <returns>System.Int32.</returns>
        """
        insStr = self.getValue(name)
        if insStr == None:
            return -1
        return int(insStr)
