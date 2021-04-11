import unittest
from tests.my_object import MyObject
from urllib.parse import urlparse, urlsplit, parse_qsl


class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_something():
        my_object = MyObject(username="username42")
        print("my_object: " + str(my_object.get_username()))


if __name__ == '__main__':
    unittest.main()
