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

from dataclasses import dataclass
from typing import Optional

from aceql._private.dto.database_info_dto import DatabaseInfoDto


@dataclass
class DatabaseInfo(object):
    """A simple shortcut class that contains main remote database & JDBC info."""
    datatabaseMajorVersion: Optional[int]
    databaseMinorVersion: Optional[int]
    databaseProductName: Optional[str]
    databaseProductVersion: Optional[str]
    driverMajorVersion: Optional[int]
    driverMinorVersion: Optional[int]
    driverName: Optional[str]
    driverVersion: Optional[str]

    def __init__(self, database_info_dto: DatabaseInfoDto):
        self.datatabaseMajorVersion = database_info_dto.datatabaseMajorVersion
        self.databaseMinorVersion = database_info_dto.databaseMinorVersion
        self.databaseProductName = database_info_dto.databaseProductName
        self.databaseProductVersion = database_info_dto.databaseProductVersion
        self.driverMajorVersion = database_info_dto.driverMajorVersion
        self.driverMinorVersion = database_info_dto.databaseMinorVersion
        self.driverName = database_info_dto.driverName
        self.driverVersion = database_info_dto.driverVersion

    def __str__(self):
        """ The string representation."""
        return "DatabaseInfoDto [datatabaseMajorVersion=" + str(
            self.datatabaseMajorVersion) + ", databaseMinorVersion=" + str(
            self.databaseMinorVersion) + ", databaseProductName=" + str(
            self.databaseProductName) + ", databaseProductVersion=" + str(
            self.databaseProductVersion) + ", driverMajorVersion=" + str(
            self.driverMajorVersion) + ", driverMinorVersion=" + str(self.driverMinorVersion) + ", driverName=" + str(
            self.driverName) + ", driverVersion=" + str(self.driverVersion) + "]"

