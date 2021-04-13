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

from requests_toolbelt.auth.guess import GuessProxyAuth


class ProxyAuth(GuessProxyAuth):
    """ Allows to set authenticated proxy username and password.

        Class inherits requests_toolbelt GuessProxyAuth and GuessAuth.
        This allows to pass and use directly parent instances if necessary.
    """

    def __init__(self,
                 proxy_username: str = None, proxy_password: str = None):
        super(ProxyAuth, self).__init__('user', 'passwd')
        self.proxy_username = proxy_username
        self.proxy_password = proxy_password

    def __str__(self):
        """ The string representation."""
        return "ProxyAuth [proxy_username=" + str(self.proxy_username) + ", proxy_password=" + str(
            self.self.proxy_password) + "]"
