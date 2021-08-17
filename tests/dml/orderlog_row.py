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
from datetime import date, datetime
from pathlib import Path


class OrderLogRow(object):
    """Simple container for orderlog table values."""


    #IN_DIRECTORY = SystemUtils.USER_HOME + File.separator + "aceql_tests" + File.separator + "IN";
    #os.sep.join

    def __init__(self):
        self.customer_id = 1;
        self.item_id = 11;
        self.description = "customer id 1 and item id 1";
        self.item_cost = 2000.00;
        self.date_placed = date(2021, 1, 1)
        self.date_shipped = datetime.now()

        dir_in = str(Path.home()) + "/aceql_tests/IN"
        if not Path(dir_in).is_dir():
            os.mkdir(dir_in)

        dir_out = str(Path.home()) + "/aceql_tests/OUT"
        if not Path(dir_out).is_dir():
            os.mkdir(dir_out)

        self.jpeg_image = str(dir_in) + "/username_koala.jpg"
        self.out_jpeg_image = str(dir_out) + "/username_koala.jpg"

        self.is_delivered = True;
        self.quantity = 3000;

        if os.path.exists(self.out_jpeg_image):
            os.remove(self.out_jpeg_image)

    def __str__(self) -> str:
        return super().__str__()


if __name__ == '__main__':
    orderlog_raw = OrderLogRow()
    print(orderlog_raw.customer_id)




