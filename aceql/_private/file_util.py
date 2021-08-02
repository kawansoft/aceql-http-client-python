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

import uuid
from os import sep
import os
import gzip
import sys
from io import open


class FileUtil(object):
    """Misc file utilities."""

    UNZIP_MODE_PY_2 = "rb"
    WRITE_MODE_PY_2 = "wb"

    UNZIP_MODE_PY_3 = "rt"
    WRITE_MODE_PY_3 = "wt"

    @staticmethod
    def get_unique_id() -> str:
        x = uuid.uuid4()
        return str(x)

    @staticmethod
    def get_user_home_dot_kawansoft_dir() -> str:
        # user.home
        # home = str(Path.home())
        home = os.path.expanduser("~")
        # print("home2: " + home2)

        # File.separator
        home_kawan_soft = home + sep + ".kawansoft"

        if not os.path.isdir(home_kawan_soft):
            os.mkdir(home_kawan_soft)

        return home_kawan_soft

    @staticmethod
    def get_kawansoft_temp_dir() -> str:
        home_kawan_soft = FileUtil.get_user_home_dot_kawansoft_dir()

        # File.separator
        home_kawan_soft_tmp = home_kawan_soft + sep + "tmp"

        if not os.path.isdir(home_kawan_soft_tmp):
            os.mkdir(home_kawan_soft_tmp)

        return home_kawan_soft_tmp

    @staticmethod
    def build_result_set_file() -> str:
        the_file = FileUtil.get_kawansoft_temp_dir() + sep + "pc-result-set-" + FileUtil.get_unique_id() + ".txt"
        return the_file

    @staticmethod
    def build_batch_file() -> str:
        the_file = FileUtil.get_kawansoft_temp_dir() + sep + "-batch-file-" + FileUtil.get_unique_id() + ".txt"
        return the_file

    @staticmethod
    def decompress(file_in: str, file_out: str):
        """Decompress GZIP text file into a text file."""

        if file_in is None:
            raise TypeError("file_in is null!")

        if not os.path.isfile(file_in):
            raise IOError("Compressed file_in does not exist: " + str(file_in))

        # P2 = rb / wb
        # P3 = rt / wt
        gzip_mode = FileUtil.get_unzip_mode()
        write_mode = FileUtil.get_write_mode()

        with gzip.open(file_in, gzip_mode) as f:
            with open(file_out, write_mode) as out:
                while True:
                    line = f.readline()
                    if line == '':
                        break
                        # print(line)
                    out.write(line)

    @staticmethod
    def get_unzip_mode() -> str:
        if FileUtil.is_python_3():
            return FileUtil.UNZIP_MODE_PY_3
        else:
            return FileUtil.UNZIP_MODE_PY_2

    @staticmethod
    def get_write_mode()-> str:
        if FileUtil.is_python_3():
            return FileUtil.WRITE_MODE_PY_3
        else:
            return FileUtil.WRITE_MODE_PY_2

    @staticmethod
    def is_python_2() -> bool:
        if sys.version_info[0] < 3:
            return True

    @staticmethod
    def is_python_3() -> bool:
        if sys.version_info[0] >= 3:
            return True
