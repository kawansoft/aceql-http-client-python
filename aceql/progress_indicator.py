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

from aceql._private.parms import  *


class ProgressIndicator(object):
    """Class that hold a progress when transferring a Blob."""

    def __init__(self):
        self.__percent = 0
        self.__cancelled = False

    #
    # Private methods,, not to be called.
    #

    def _increment(self):
        """ Called by AceQL internal code during transfer progress."""
        if self.__percent < 99:
            self.__percent += 1
        if Parms.PRINT_PROGRESS_INDICATOR:
            print(str(self.__percent) + "%")

    def _set_complete(self):
        """ To be called by upload/download AceQL internal code when transfer is complete."""
        self.__percent = 100

    #
    # Public methods
    #

    def get_percent(self):
        """ Allows to get transfer progress from 0 to 100 """
        return self.__percent

    def cancel(self):
        """ Allows caller to cancel the transfer operation """
        self.__cancelled = True

    def is_cancelled(self):
        """ Allows for AceQL internal for transfer thread to test if cancelled """
        return self.__cancelled
