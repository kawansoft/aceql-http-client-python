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
from os.path import sep

from aceql._private.file_util import FileUtil


class FrameworkDebug(object):
    CLASSES_TO_DEBUG = set()

    @staticmethod
    def is_set(class_name: str) -> bool:
        """Says if the passed class names is set to for debug."""
        classname_in_set = class_name in FrameworkDebug.CLASSES_TO_DEBUG
        return classname_in_set

    @staticmethod
    def load():
        """Loads the file that contains the classes to debug and update the CLASSES_TO_DEBUG set."""
        if len(FrameworkDebug.CLASSES_TO_DEBUG) > 0:
            return;
        aceql_debug_file = FileUtil.get_user_home_dot_kawansoft_dir() + sep + "aceql-debug-python.ini"

        if not os.path.isfile(aceql_debug_file):
            return;

        # Loads from file classes to debug
        with open(aceql_debug_file) as f:
            lines = f.readlines()
            for line in lines:
                FrameworkDebug.CLASSES_TO_DEBUG.add(line.strip())


if __name__ == '__main__':
    FrameworkDebug.load()
    print(str(FrameworkDebug.CLASSES_TO_DEBUG))



