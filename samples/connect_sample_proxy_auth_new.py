import aceql
from aceql import ConnectionOptions
from aceql import ProxyAuth
from samples import my_proxy

# URL of the AceQL server, Remote SQL database name & authentication info
url = "http://www.runsafester.net:8081/aceql"
database = "sampledb"
username = "user1"
password = "password1"

proxies = {
    "http": "http://localhost:8081",
}

# Get the proxy credentials with our own application methods
proxy_username = my_proxy.get_username()
proxy_password = my_proxy.get_password()

# The AceQL ProxyAuth class allows to define the proxy credentials
auth = ProxyAuth(proxy_username, proxy_password)

# We use the ConnectionOptions wrapper class to pass both the proxies & auth
connection_options = ConnectionOptions(proxies=proxies, auth=auth)
connection = aceql.connect(url=url, username=username, password=password, database=database,
                           connection_options=connection_options)

print("aceql version     : " + connection.get_client_version())


