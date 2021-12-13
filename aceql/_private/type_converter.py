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
from aceql._private.cursor_util import CursorUtil


class TypeConverter(object):
    """ Class TypeConverter. Converts the parameter type into Java equivalent"""

    # -2147483648 to 2147483647
    MIN_JAVA_INTEGER = -2147483648
    MAX_JAVA_INTEGER = 2147483647

    def __init__(self, the_value) -> None:
        """ Initializes a new instance of the <see cref="TypeConverter"/> class.

        Args:
            the_value: value to get type of
        """
        self.__the_value = the_value;

    def get_java_type_name(self) -> str:
        """ Gets the name of the java type.

        Returns:
            str: the type of the value in Java
        """

        name = CursorUtil.get_class_name(self.__the_value)

        if name.__eq__("bool"):
            return "Boolean"
        elif name.__eq__("int"):
            return TypeConverter.int_or_long(self.__the_value)
        elif name.__eq__("float"):
            return "Float"
        elif name.__eq__("str"):
            return "String"
        elif name.__eq__("datetime.datetime"):
            return "Timestamp"
        else:
            raise TypeError("This parameter type is unsupported in this AceQL version: " + name)

    @staticmethod
    def int_or_long(the_value):
        if the_value >= TypeConverter.MIN_JAVA_INTEGER and the_value <= TypeConverter.MAX_JAVA_INTEGER:
            return "Integer"
        else:
            return "Long"
