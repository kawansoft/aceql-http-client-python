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

from datetime import datetime, time
import time
import pytz


class DateTimeUtil(object):
    """Date & datetime utilities

    Includes conversion from and to Unix Timestamp as date/time object
    are transfere a long Unix Epoch
    """

    # def get_timestamp_from_datetime(the_date_time):
    #
    # 	# "Returns an Epoch for a datetime."
    # 	# ts = the_date_time.timestamp()
    # 	# tsStr = str(ts * 1000)
    # 	# dotIndex = tsStr.index(".")
    # 	# tsStr = tsStr[0: dotIndex]
    #    #
    # 	# print ("tsStr: " + tsStr)
    # 	# return tsStr

    # get_timestamp_from_datetime = staticmethod(get_timestamp_from_datetime)

    def to_timestamp(a_date):
        if a_date.tzinfo:
            epoch = datetime(1970, 1, 1, tzinfo=pytz.UTC)
            diff = a_date.astimezone(pytz.UTC) - epoch
        else:
            epoch = datetime(1970, 1, 1)
            diff = a_date - epoch
        return int(diff.total_seconds())

    to_timestamp = staticmethod(to_timestamp)

    def get_timestamp_from_date(the_date):
        "Returns an Epoch for date."
        unixtime = time.mktime(the_date.timetuple())

        # print("unixtime: " + str(unixtime))
        # unixtimeStr = str(unixtime * 1000)
        unixtimeStr = str(unixtime)
        unixtimeStr = unixtimeStr[0:len(unixtimeStr) - 2]
        return unixtimeStr + "000"

    get_timestamp_from_date = staticmethod(get_timestamp_from_date)

    def get_datetime_from_timestamp(tsStr):
        """Returns a datetime from Unix Epoch."""

        ts = float(tsStr)
        tsInt = ts / 1000  # we want in seconds
        return datetime.fromtimestamp(tsInt)

    get_datetime_from_timestamp = staticmethod(get_datetime_from_timestamp)

    def get_date_from_timestamp(tsStr):
        """Returns a date from Unix Epoch."""

        ts = float(tsStr)
        tsInt = ts / 1000  # we want in seconds
        theDatetime = datetime.fromtimestamp(tsInt)
        return theDatetime.date()

    get_date_from_timestamp = staticmethod(get_date_from_timestamp)
