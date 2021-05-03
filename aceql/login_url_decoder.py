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

from urllib.parse import urlsplit, parse_qsl


class LoginUrlDecoder(object):
    """Allows to split an URL into the basic login info: login URL, username, password and database."""

    def __init__(self, url: str):
        if url is None:
            raise TypeError("url is null!")

        my_dict: dict = dict(parse_qsl(urlsplit(url).query))

        self.__server_url: str = url.split('?')[0]

        self.__username = None
        self.__password = None
        self.__database = None

        for theKey, theValue in my_dict.items():
            if theKey == "username":
                self.__username = theValue
            if theKey == "password":
                self.__password = theValue
            if theKey == "database":
                self.__database = theValue

    @property
    def server_url(self) -> str:
        """Returns the server login url"""
        return self.__server_url

    @property
    def username(self) -> str:
        """Returns the username"""
        return self.__username

    @property
    def password(self) -> str:
        """Returns the password"""
        return self.__password

    @property
    def database(self) -> str:
        """Returns the database name"""
        return self.__database

