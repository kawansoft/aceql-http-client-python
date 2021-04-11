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


class UserLoginStore(object):
    """ Stores the session Id per server_url/username/database triplet in order to
        get new AceQL Connection with /get_connection without new login action."""

    __logged_users = {}

    def __init__(self, server_url: str, username: str, database: str):
        """Constructor"""

        if server_url is None:
            raise TypeError("serverUrl is null!")
        if username is None:
            raise TypeError("username is null!")
        if database is None:
            raise TypeError("database is null!")

        self.__server_url = server_url
        self.__username = username
        self.__database = database

    def build_key(self) -> str:
        """Builds the Dict key for the (:, username, database) triplet key."""
        return self.__server_url + "/" + self.__username + "/" + self.__database;

    def is_already_logged(self) -> bool:
        """Says if user is already logged, aka key exists in Dict"""
        key = self.build_key()
        data = UserLoginStore.__logged_users.get(key)
        if data is None:
            return False
        else:
            return True

    def get_session_id(self) -> str:
        """Returns the session Id of logged user with (server_url, username, database) triplet."""
        key = self.build_key()
        session_id = UserLoginStore.__logged_users[key]
        return session_id

    def set_session_id(self, session_id: str):
        """Stores the session Id of a logged user with (server_url, username, database) triplet."""
        key = self.build_key()
        UserLoginStore.__logged_users[key] = session_id

    def remove(self):
        """Removes (server_url, username, database) triplet. This is to be called at /logout API.
        """
        key = self.build_key()
        del UserLoginStore.__logged_users[key]
