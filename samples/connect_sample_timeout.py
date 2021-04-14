import unittest
import aceql
from aceql import ConnectionOptions

# URL of the AceQL server, Remote SQL database name & authentication info
url = "http://www.runsafester.net:8081/aceql"
database = "sampledb"
username = "user1"
password = "password1"

connection_options = ConnectionOptions(timeout=10)
connection = aceql.connect(url=url, username=username, password=password, database=database,
                           connection_options=connection_options)

print("aceql version     : " + connection.get_client_version())
