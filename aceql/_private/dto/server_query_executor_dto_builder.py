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

import typing

from aceql._private.dto.server_query_executor_dto import ServerQueryExecutorDto
from aceql._private.type_converter import TypeConverter


class ServerQueryExecutorDtoBuilder:

    @staticmethod
    def build(server_query_executor_class_name: str, parameters: typing.List[object]):
        """ Builds the specified server query executor class name.

        Args:
            sql(str): Name of the server AceQL query executor class.
            parameters(typing.List[object]): The parameters.

        Returns:
            ServerQueryExecutorDto: ServerQueryExecutorDto.
            :param server_query_executor_class_name:
        """
        params_types = list()
        params_values = list()

        for parameter in parameters:
            type_converter = TypeConverter(parameter)
            params_types.append(type_converter.get_java_type_name())
            params_values.append(str(parameter))
            server_query_executor_dto: ServerQueryExecutorDto = ServerQueryExecutorDto(server_query_executor_class_name,
                                                                                       params_types,
                                                                                       params_values)
        return server_query_executor_dto
