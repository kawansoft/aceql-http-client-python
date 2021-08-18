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

from tests.misc.cursor_util_test import CursorUtilTest
from tests.misc.daterime_util_test import DateTimeUtilTest
from tests.misc.column_types_builder_test import ColumnTypesBuilderTest
from tests.result_analyzer.result_analyzer_test import ResultAnalyzerTest

from tests.row.row_counter_test import RowCounterTest
from tests.result_analyzer.stream_result_analyzer_test import StreamResultAnalyzerTest


cursorUtilTest = CursorUtilTest()
cursorUtilTest.test_A()

theTest = ColumnTypesBuilderTest()
theTest.test_A()

dateTimeUtilTest = DateTimeUtilTest()
dateTimeUtilTest.test_A()

resultAnalyzerTest = ResultAnalyzerTest()
resultAnalyzerTest.test_A()

rowCounterTest = RowCounterTest()
rowCounterTest.test_A()

rowCounterTest = RowCounterTest()
rowCounterTest.test_A()

streamResultAnalyzerTest = StreamResultAnalyzerTest()
streamResultAnalyzerTest.test_A()
exit()
