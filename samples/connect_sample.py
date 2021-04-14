import unittest
import aceql

# URL of the AceQL server, Remote SQL database name authentication info
url = "https://www.acme.com:9443/aceql"
database = "sampledb"
username = "user1"
password = "password1"

url = "http://localhost:9090/aceql"

connection = aceql.connect(url=url, username=username, password=password, database=database)
print("aceql version     : " + connection.get_client_version())


