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
class Index:

    """A SQL Index with it's defining elements."""
    catalog: Optional[str]
    schema: Optional[str]
    indexName: Optional[str]
    tableName: Optional[str]
    nonUnique: Optional[bool]
    indexQualifier: Optional[str]
    type: Optional[str]
    ordinalPosition: Optional[int]
    columnName: Optional[str]
    ascendingOrDescending: Optional[str]
    cardinality: Optional[float]
    pages: Optional[float]
    filterCondition: Optional[str]

    class Meta:

        """Meta class is required."""
        ordered = True

    def __str__(self):
        """The string representation."""
        return "Index [indexName=" + str(self.indexName) + ", tableName=" + str(self.tableName) + ", nonUnique=" + str(
            self.nonUnique) + ", indexQualifier=" + str(self.indexQualifier) + ", type=" + str(
            self.type) + ", ordinalPosition=" + str(self.ordinalPosition) + ", columnName=" + str(
            self.columnName) + ", ascendingOrDescending=" + str(self.ascendingOrDescending) + ", cardinality=" + str(
            self.cardinality) + ", pages=" + str(self.pages) + ", filterCondition=" + str(self.filterCondition) + "]"
