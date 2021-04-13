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

from datetime import datetime
import time
import pytz


class DateTimeUtil(object):
    """Date & datetime utilities

    Includes conversion from and to Unix Timestamp as date/time object
    are transferred as a long Unix Epoch
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

    @staticmethod
    def to_timestamp(a_date: str) -> int:
        if a_date.tzinfo:
            epoch = datetime(1970, 1, 1, tzinfo=pytz.UTC)
            diff = a_date.astimezone(pytz.UTC) - epoch
        else:
            epoch = datetime(1970, 1, 1)
            diff = a_date - epoch
        return int(diff.total_seconds())

    @staticmethod
    def get_timestamp_from_date(the_date: datetime) -> str:
        """"Returns an Epoch for date."""
        unix_time = time.mktime(the_date.timetuple())

        unix_time_str = str(unix_time)
        unix_time_str = unix_time_str[0:len(unix_time_str) - 2]
        return unix_time_str + "000"

    @staticmethod
    def get_datetime_from_timestamp(ts_str : str) -> datetime:
        """Returns a datetime from Unix Epoch."""

        ts = float(ts_str)
        ts_int = ts / 1000  # we want in seconds
        return datetime.fromtimestamp(ts_int)

    @staticmethod
    def get_date_from_timestamp(ts_str : str) -> datetime:
        """Returns a date from Unix Epoch."""

        ts = float(ts_str)
        ts_int = ts / 1000  # we want in seconds
        the_datetime = datetime.fromtimestamp(ts_int)
        return the_datetime.date()

    @staticmethod
    def get_time_from_timestamp(ts_str: str) -> datetime:
        """Returns a date from Unix Epoch."""

        ts = float(ts_str)
        ts_int = ts / 1000  # we want in seconds
        the_datetime = datetime.fromtimestamp(ts_int)
        return the_datetime.time()

