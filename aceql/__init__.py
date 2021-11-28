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

"""aceql library. Allows to wrap the AceQL HTTP APIs to access remote SQL databases.

    The library supports Python 3.6 to 3.9.
    It provides a SQL interface compliant with the DB-API 2.0 specification described by PEP 249.
"""

from aceql.connection import Connection
from aceql.progress_indicator import ProgressIndicator
from aceql.sql_null_type import SqlNullType
from aceql.cursor import Cursor
from aceql.error import Error
from aceql.proxy_auth import ProxyAuth
from aceql.connection_options import ConnectionOptions

from aceql.metadata.exportedkey import ExportedKey
from aceql.metadata.foreignkey import ForeignKey
from aceql.metadata.importedkey import ImportedKey
from aceql.metadata.index import Index
from aceql.metadata.jdbc_database_meta_data import JdbcDatabaseMetaData
from aceql.metadata.primarykey import PrimaryKey
from aceql.metadata.remote_database_metadata import RemoteDatabaseMetaData
from aceql.metadata.table import Table
from aceql.metadata.column import Column


__all__ = ["Connection", "Cursor", "Error", "ConnectionOptions", "ProgressIndicator", "ProxyAuth", "SqlNullType",
           "Column", "ExportedKey",
           "ForeignKey", "ImportedKey", "Index", "JdbcDatabaseMetaData", "PrimaryKey", "RemoteDatabaseMetaData",
           "Table"]


def connect(*, url: str, username: str = None, password: str = None, database: str = None, connection_options: ConnectionOptions = None):
    """
    Creates a database connection to the remote AceQL HTTP server.

    Parameters
    ----------
    url : str
        The URL of the AceQL server. Example: https://www.acme.com:9443/aceql.
        The URL may includes all parameters:
        https://www.acme.com:9443/acel?username=my_name&password=my_passwd&database=my_db
    username : str
        The authentication username.
    password : str
        the authentication password.
    database : str
        The remote database name.
    connection_options : ConnectionOptions
            the  supplemental Connection Options (Container that allows define some options: proxies,
            timeout, request headers, etc.)

    Returns
    -------
    Connection
        A connection to the remote database.

    """

    the_connection = Connection(url=url, username=username, password=password, database=database,
                                connection_options=connection_options)
    return the_connection
