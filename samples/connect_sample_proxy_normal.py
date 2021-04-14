import unittest
import aceql
from aceql import ConnectionOptions

# URL of the AceQL server, Remote SQL database name & authentication info
url = "http://www.runsafester.net:8081/aceql"
database = "sampledb"
username = "user1"
password = "password1"

proxies = {
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080',
}

# We use the ConnectionOptions wrapper class to pass the proxies
connection_options = ConnectionOptions(proxies=proxies)
connection = aceql.connect(url=url, username=username, password=password, database=database,
                           connection_options=connection_options)

print("aceql version     : " + connection.get_client_version())
