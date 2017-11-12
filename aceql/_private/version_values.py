#
# This file is part of AceQL Python Client SDK.
# AceQL Python Client SDK: Remote SQL access over HTTP with AceQL HTTP.
# Copyright (C) 2017,  KawanSoft SAS
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

# V 1.0-beta-1
# 28/10/2017 15:14 NDP: RowParser done & tested
# 28/10/2017 19:11 NDP: Packages creation done & tests created
# 29/10/2017 16:56 NDP: ColumnTypesBuilder creation
# 30/10/2017 14:40 NDP: AceQLConnection cleaning & Cursor creation
# 30/10/2017 14:40 NDP: Cursor: final execute_update done.
# 30/10/2017 23:19 NDP: RowParser rewritten & start implementing Cursor.__execute_query
# 31/10/2017 12:56 NDP: Add GZIP support & datetime in Util
# 31/10/2017 13:52 NDP: CursorUtil dedicated class creation
# 31/10/2017 14:51 NDP: CursorUtil: rewrite get_timestamp clean methods
# 31/10/2017 18:33 NDP: Cursor.fetchone & iterator done & remove headers
# 31/10/2017 20:34 NDP: Cursor.description done
# 31/10/2017 21:32 NDP: Add Parms & file delete if set in Parms
# 01/11/2017 12:53 NDP: CursorUtil is now instantiable because we need lists for BLOB info
# 01/11/2017 14:06 NDP: Cursor fetchmany & fetchall implemented
# 01/11/2017 14:20 NDP: Force all files open in utf-8
# 01/11/2017 16:04 NDP: Date, time and Timestamp ae ow in own class DateTimeUtil
# 01/11/2017 17:26 NDP: result set TIMESTAMP and DATE are convrted to datetime and date
# 01/11/2017 17:28 NDP: Complete dbapi2 as much as possible
# 01/11/2017 23:52 NDP: Blob download complete
# 02/11/2017 15:23 NDP: Remove Path 3.4
# 02/11/2017 18:07 NDP: Add BLOB download support
# 02/11/2017 21:15 NDP: Add BLOB upload support & pipenv install requests-toolbets
# 02/11/2017 23:06 NDP: BLOB uplod: close file descriptors in Cursor
# 02/11/2017 23:25 NDP: use from io import open in files with open() for P2 compatibility
# 02/11/2017 23:39 NDP: from builtins import int in classes that use isinstance(x, int)
# 02/11/2017 23:39 NDP: remove pip vendor ==> Requirements are only
#											 requests==2.18.4
#											 requests_toolbelt==0.8.0
#											 future==0.16.0
# 03/11/2017 13:58 NDP: Upload finished with progress indicator
# 03/11/2017 22:02 NDP: Version is now compatible with Python 2 & 3
# 04/11/2017 13:14 NDP: FileUtil rewritten for decompress to b compatible with version 2 and 3
# 04/11/2017 14:17 NDP: All fixed except RaiseError compatible with Py2 & Py3
# 04/11/2017 18:21 NDP: String with special chars are now accepted as statement parameters
# 04/11/2017 18:23 NDP: Clean unit tests & prepare Error class for all Exceptiosn
# 04/11/2017 18:44 NDP: Error is now main Exception class as required by DB API
# 04/11/2017 19:05 NDP: Enhance Error remove remaininf AceQLException
# 04/11/2017 20:42 NDP: All is one! Ready for last test class and packaging
# 05/11/2017 13:46 NDP: Prepare final version with _private package
# 05/11/2017 14:26 NDP: Move private classes to _private sub package
# 05/11/2017 17:24 NDP: Fix bugs after _private creation & clean comments
# 05/11/2017 19:00 NDP: Rename AceQLConnection to Connection & SqlNullType is now an enum
# 06/11/2017 14:43 NDP: SqlNullType: back to constants as enums are not supported in 2.7
# 06/11/2017 14:43 NDP: Rewrite ProgressIndicator by making some methods private
# 06/11/2017 14:43 NDP: Cursor.description sequence is now 7 long pre column as required by PEP 249
# 06/11/2017 14:43 NDP: Clean comments in all public classes and methods
# 06/11/2017 19:23 NDP: Clean comments in all public classes and methods
# 06/11/2017 21:44 NDP: Add header notice
# 07/11/2017 20:38 NDP: Clean code & tests: put var names in Python underscore convention
# 07/11/2017 21:50 NDP: Clean code
# 07/11/2017 22:28 NDP: Clean code: put var names in Python underscore convention
# 08/11/2017 15:15 NDP: AceQLHttpApi: clean code / underscores for var and methods
# 08/11/2017 15:15 NDP: All _private classes: clean code / underscores for var and methods
# 08/11/2017 16:12 NDP: Remove all PyCharm warnings
# 08/11/2017 19:40 NDP: Cursor: fix bug in __build_description: name_and_type was no reset for each column
# 08/11/2017 21:06 NDP: Cursor & Connection: clean comments
# 11/11/2017 18:36 NDP: RowParser: convert 'NULL' to None
# 11/11/2017 18:39 NDP: CursorUtil: Support datetime.time to TIME  & BLOB is 'file' type for Python 2.7s
# 11/11/2017 19:56 NDP: Error: multi lines reason & stack exception are split into list of str
# 11/11/2017 15:03 NDP: Clean comments in aceql module
# 11/11/2017 17:09 NDP: Cursor: raise error Error if Cursor is closed
# 11/11/2017 17:26 NDP: .py files are now all lowercase
# 11/11/2017 18:17 NDP: import all aceql classes in __init__


class VersionValues(object):
    NAME = "AceQL HTTP SDK"
    VERSION = "v1.0-beta-1"
    DATE = "12-nov-2017"
