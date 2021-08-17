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
from tests.util.sha1 import Sha1


class BlobTestUtil:

    @staticmethod
    def check_blob_integrity(file_in, file_out):

        hash_file_in = Sha1.get_hexas_tring(file_in)
        hash_file_out = Sha1.get_hexas_tring(file_out)

        print("SHA1 of " + file_in + ": " + hash_file_in);
        print("SHA1 of " + file_out + ": " + hash_file_out);

        assert hash_file_in == hash_file_out, "Files are different."

