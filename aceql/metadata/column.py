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
import marshmallow_dataclass


@dataclass
class Column:
    catalog: Optional[str]
    schema: Optional[str]
    columnName: Optional[str]
    tableName: Optional[str]
    typeName: Optional[str]
    size: Optional[int]
    decimalDigits: Optional[int]
    radix: Optional[int]
    nullable: Optional[str]
    remarks: Optional[str]
    defaultValue: Optional[str]
    charOctetLength: Optional[int]
    ordinalPosition: Optional[int]
    isNullable: Optional[str]
    scopeCatalog: Optional[str]
    scopeSchema: Optional[str]
    scopeTable: Optional[str]
    sourceDataType: Optional[int]
    isAutoincrement: Optional[str]

    class Meta:
        ordered = True

    def __str__(self):
        """ The string representation."""
        return "Column [columnName=" + str(self.columnName) + ", tableName=" + str(
            self.tableName) + ", typeName=" + str(self.typeName) + ", size=" + str(
            self.size) + ", decimalDigits=" + str(self.decimalDigits) + ", radix=" + str(
            self.radix) + ", nullable=" + str(self.nullable) + ", remarks=" + str(
            self.remarks) + ", defaultValue=" + str(self.defaultValue) + ", charOctetLength=" + str(
            self.charOctetLength) + ", ordinalPosition=" + str(self.ordinalPosition) + ", isNullable=" + str(
            self.isNullable) + ", scopeCatalog=" + str(self.scopeCatalog) + ", scopeSchema=" + str(
            self.scopeSchema) + ", scopeTable=" + str(self.scopeTable) + ", sourceDataType=" + str(
            self.sourceDataType) + ", isAutoincrement=" + str(self.isAutoincrement) + "]"
