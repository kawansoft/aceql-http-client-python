import unittest
from urllib.parse import urlparse, urlsplit, parse_qsl


class MyUrlTest(unittest.TestCase):
    @staticmethod
    def test_something():
        url = "http://localhost:9090/aceql?user=user1&password=password1&database=sampledb"
        #parsed_url = urlparse(URL)
        #my_base_url = URL.split('?')
        my_dict: dict = dict(parse_qsl(urlsplit(url).query))

        print("server_url: " + url.split('?')[0])
        print("my_dict   : " + str(my_dict))
        #print("user      : " + str(my_dict["user"]))


if __name__ == '__main__':
    unittest.main()
