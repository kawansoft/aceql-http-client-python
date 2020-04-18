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
from typing import Optional, List
import marshmallow_dataclass

from aceql.metadata.column import Column
from aceql.metadata.exportedkey import ExportedKey
from aceql.metadata.foreignkey import ForeignKey
from aceql.metadata.importedkey import ImportedKey
from aceql.metadata.index import Index
from aceql.metadata.primarykey import PrimaryKey


@dataclass
class Table:
    """A SQL Table with it's defining elements."""
    TABLE = "TABLE";
    VIEW = "VIEW";
    tableName: Optional[str]
    tableType: Optional[str]
    remarks: Optional[str]
    columns: Optional[List[Column]]
    primaryKeys: Optional[List[PrimaryKey]]
    indexes: Optional[List[Index]]
    importedforeignKeys: Optional[List[ImportedKey]]
    exportedforeignKeys: Optional[List[ExportedKey]]
    catalog: Optional[str]
    schema: Optional[str]

    class Meta:
        ordered = True

    def __str__(self):
        """ The string representation."""
        return "Table [tableName=" + str(self.tableName) + ", tableType=" + str(self.tableType) + ", remarks=" + str(
            self.remarks) + ", columns=" + str(self.columns) + ", primaryKeys=" + str(
            self.primaryKeys) + ", indexes=" + str(self.indexes) + ", importedforeignKeys=" + str(
            self.importedforeignKeys) + ", exportedforeignKeys=" + str(self.exportedforeignKeys) + ", catalog=" + str(
            self.catalog) + ", schema=" + str(self.schema) + "]"
