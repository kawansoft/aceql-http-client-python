import unittest
from tests.my_object import MyObject
from urllib.parse import urlparse, urlsplit, parse_qsl

class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_something():
        URL = "http://localhost:9090/aceql?user=user1&password=password1&database=sampledb"
        parsed_url = urlparse(URL)
        my_base_url = URL.split('?')
        my_dict: dict = dict(parse_qsl(urlsplit(URL).query))

        print("server_url: " + URL.split('?')[0])
        print("my_dict   : " + str(my_dict))

        print("user   : " + str(my_dict["user"]))


if __name__ == '__main__':
    unittest.main()
