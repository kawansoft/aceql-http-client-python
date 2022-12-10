#
# This file is part of AceQL Python Client SDK.
# AceQL Python Client SDK: Remote SQL access over HTTP with AceQL HTTP.
# Copyright (C) 2022,  KawanSoft SAS
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

from aceql._private.dto.limits_info_dto import LimitsInfoDto


@dataclass
class LimitsInfo:
    """
    A simple shortcut class that contains main remote database limits info:
    maxRows: the maximum number of SQL rows that may be returned to the
    client by the AceQL server.
    maxBlobLength: the maximum length allowed for a Blob upload.
    """
    maxRows: Optional[float]
    maxBlobLength: Optional[float]

    def __init__(self, limits_info_dto: LimitsInfoDto):
        self.maxRows = limits_info_dto.maxRows
        self.maxBlobLength = limits_info_dto.maxBlobLength

    def __str__(self):
        """ The string representation."""
        return "LimitsInfo [maxRows=" + str( self.maxRows) + ", maxBlobLength=" + str( self.maxBlobLength)  + "]"
