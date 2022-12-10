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


@dataclass
class LimitsInfoDto:
    """ Generated on 2022-12-10 10:05:38
    from com.aceql.jdbc.commons.main.metadata.dto.LimitsInfoDto.java translation """
    status: Optional[str]
    maxRows: Optional[float]
    maxBlobLength: Optional[float]

    class Meta:
        ordered = True

    def __str__(self):
        """ The string representation."""
        return "LimitsInfoDto [status=" + str( self.status) + ", maxRows=" + str( self.maxRows) + ", maxBlobLength=" + str(
            self.maxBlobLength)  + "]"
