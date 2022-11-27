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
from aceql._private.dto.health_check_info_dto import HealthCheckInfoDto


class ServerMemoryInfo(object):
    """Contains health check Java memory info of the AceQL server running instance. """
    def __init__(self, health_check_info_dto: HealthCheckInfoDto):
        self.__init_memory= health_check_info_dto.initMemory
        self.__used_memory = health_check_info_dto.usedMemory
        self.__max_memory = health_check_info_dto.maxMemory
        self.__committed_memory = health_check_info_dto.committedMemory

    def get_init_memory(self) -> float:
        """
        Returns the amount of memory in bytes that the Java virtual machine
        initially requests from the operating system for memory management.
        This method returns -1 if the initial memory size is undefined.
        """
        return self.__init_memory

    def get_used_memory(self) -> float:
        """
        Returns the amount of used memory in bytes
        """
        return self.__used_memory

    def get_max_memory(self) -> float:
        """
        Returns the maximum amount of memory in bytes that can be
        used for memory management.  This method returns -1
        if the maximum memory size is undefined.

        This amount of memory is not guaranteed to be available
        for memory management if it is greater than the amount of
        committed memory.  The Java virtual machine may fail to allocate
        memory even if the amount of used memory does not exceed this
        maximum size.
        """
        return self.__max_memory

    def get_commited_memory(self) -> float:
        """
        Returns the maximum amount of memory in bytes that can be
        used for memory management.  This method returns -1
        if the maximum memory size is undefined.

        This amount of memory is not guaranteed to be available
        for memory management if it is greater than the amount of
        committed memory.  The Java virtual machine may fail to allocate
        memory even if the amount of used memory does not exceed this
        maximum size.
        """
        return self.__committed_memory

    def __str__(self):
        """ The string representation."""
        return "ServerMemoryInfo [initMemory=" + str( self.__init_memory) + ", usedMemory=" + str(
            self.__used_memory) + ", maxMemory=" + str(
            self.__max_memory) + ", committedMemory=" + str(
            self.__committed_memory) + "]"

