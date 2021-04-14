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

from aceql._private.parms import Parms


class AceQLDebug(object):
    """debug class"""

    # stack = inspect.stack()
    # the_class = stack[1][0].f_locals["self"].__class__
    # the_method = stack[1][0].f_code.co_name

    # print("I was called by {}.{}()".format(str(calling_class),
    # calling_code_name))
    ## => I was called by A.a()

    @staticmethod
    def debug_empty():
        if Parms.DEBUG_ON:
            print("debug> ")

    @staticmethod
    def debug(s: str):
        if Parms.DEBUG_ON:
            print("debug> " + str(s))

