import unittest
from aceql.login_url_decoder import LoginUrlDecoder


class MyUrlTest(unittest.TestCase):
    @staticmethod
    def test_something():
        url = "http://localhost:9090/aceql?username=user1&password=password1&database=sampledb"

        login_url_decoder: LoginUrlDecoder = LoginUrlDecoder(url)

        print("login_url_decoder.server_url: " + login_url_decoder.server_url + ":")
        print("login_url_decoder.username  : " + login_url_decoder.username + ":")
        print("login_url_decoder.password  : " + login_url_decoder.password + ":")
        print("login_url_decoder.database  : " + login_url_decoder.database + ":")


if __name__ == '__main__':
    unittest.main()
