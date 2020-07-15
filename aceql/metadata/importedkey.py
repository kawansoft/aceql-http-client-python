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

from dataclasses import dataclass
from typing import Optional


@dataclass
class ImportedKey:

    """A SQL Foreign Key."""
    catalog: Optional[str]
    schema: Optional[str]
    primaryKeyTable: Optional[str]
    primaryKeyColumn: Optional[str]
    foreignKeyCatalog: Optional[str]
    foreignKeySchema: Optional[str]
    foreignKeyTable: Optional[str]
    foreignKeyColumn: Optional[str]
    keySequence: Optional[int]
    updateRule: Optional[str]
    deleteRule: Optional[str]
    foreignKeyName: Optional[str]
    primaryKeyName: Optional[str]
    deferrability: Optional[int]

    class Meta:

        """Meta class is required."""
        ordered = True

    def __str__(self):
        """The string representation."""
        return "ImportedKey [primaryKeyTable=" + str(self.primaryKeyTable) + ", primaryKeyColumn=" + str(
            self.primaryKeyColumn) + ", foreignKeyCatalog=" + str(self.foreignKeyCatalog) + ", foreignKeySchema=" + str(
            self.foreignKeySchema) + ", foreignKeyTable=" + str(self.foreignKeyTable) + ", foreignKeyColumn=" + str(
            self.foreignKeyColumn) + ", keySequence=" + str(self.keySequence) + ", updateRule=" + str(
            self.updateRule) + ", deleteRule=" + str(self.deleteRule) + ", foreignKeyName=" + str(
            self.foreignKeyName) + ", primaryKeyName=" + str(self.primaryKeyName) + ", deferrability=" + str(
            self.deferrability) + "]"
