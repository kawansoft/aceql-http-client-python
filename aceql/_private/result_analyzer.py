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
    def __init__(self, json_result: str, http_status_code: int):
        """ <summary>
         Initializes a new instance of the <see cref="ResultAnalyzer"/> class.
         </summary>
         <param name="son_result">The json result.</param>
         <param name="http_status_code">The http status code.</param>
         <exception cref="System.ArgumentNullException">son_result is null!</exception>
        """
        self._invalid_json_stream = False
        self._parse_exception = None
        self._http_status_code = http_status_code
        self._json_result = json_result

    def is_status_ok(self):
        """ <summary>
         Determines whether the SQL command correctly executed on server side.
         </summary>
         <returns><c>true</c> if [is status ok]; otherwise, <c>false</c>.</returns>
        """

        if self._json_result is None or len(self._json_result) == 0:
            return False
        try:
            j = json.loads(self._json_result)
            status = j["status"]
            if status == "OK":
                return True
            else:
                return False
        except Exception as e:
            self._parse_exception = e
            self._invalid_json_stream = True
            return False

    def is_invalid_json_stream(self) -> bool:
        """ <summary>
         Says if the JSON Stream is invalid.
         </summary>
         <returns>true if JSN stream is invalid</returns>
        """
        if self._json_result is None or len(self._json_result) == 0:
            return True
        if self._invalid_json_stream:
            return True
        return False

    def get_result(self, name) -> str:
        """ <summary>
         Gets the result for a a key name
         </summary>
         <param name="name">The name.</param>
         <returns>System.String.</returns>
        """
        return self.get_value(name)

    def get_result_default(self) -> str:
        """ <summary>
         Gets the result for the key name "result"
         </summary>
         <returns></returns>
        """
        return self.get_value("result")

    def get_value(self, name) -> str:
        """ <summary>
         Gets the value.
         </summary>
         <param name="name">The name.</param>
         <returns>System.String.</returns>
         <exception cref="System.ArgumentNullException">name is null!</exception>
         <exception cref="System.Exception">Illegal name: " + name</exception>
        """
        if name is None:
            raise TypeError("name is null!")
        if self.is_invalid_json_stream():
            return None

        try:
            j = json.loads(self._json_result)

            if name == "session_id":
                value = j[name]
            elif name == "connection_id":
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
            self._parse_exception = e
            self._invalid_json_stream = True
            return None

    def get_error_type(self) -> int:
        """ <summary>
         Gets the error_type.
         </summary>
         <returns>System.Int32.</returns>
        """
        if self.is_invalid_json_stream():
            return 0

        try:
            j = json.loads(self._json_result)
            error_type = j["error_type"]
            return error_type
        except Exception as e:
            self._parse_exception = e
            self._invalid_json_stream = True
            return 0

    def get_error_message(self) -> str:
        """ <summary>
         Gets the error_message.
         </summary>
         <returns>System.String.</returns>
        """
        if self.is_invalid_json_stream():
            the_error_message = "Unknown error."
            if self._http_status_code != 200:
                the_error_message = "HTTP FAILURE " + str(self._http_status_code);
            return the_error_message
        try:
            j = json.loads(self._json_result)
            error_message = j["error_message"]
            return error_message
        except Exception as e:
            self._parse_exception = e
            self._invalid_json_stream = True
            return None

    def get_stack_trace(self) -> str:
        """ <summary>
         Gets the remote stack_trace.
         </summary>
         <returns>String.</returns>
        """
        if self.is_invalid_json_stream():
            return None
        try:
            j = json.loads(self._json_result)
            stack_trace = j["stack_trace"]
            return stack_trace
        except Exception as e:
            self._parse_exception = e
            self._invalid_json_stream = True
            return None

    def get_int_value(self, name: str) -> int:
        """ <summary>
         Gets the int value.
         </summary>
         <param name="name">The name.</param>
         <returns>System.Int32.</returns>
        """
        ins_str = self.get_value(name)
        if ins_str is None:
            return -1
        return int(ins_str)
