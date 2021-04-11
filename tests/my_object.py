

class MyObject(object):
    """Internal Tests"""

    def __init__(self, *, server_url: str = None, database: str = None,
                 username: str = None, password: str = None) -> None:
        self.__server_url = server_url
        self.__database = database
        self.__username = username
        self.__password = password

    def get_server_url(self) -> str:
        return self.__server_url

    def get_database(self) -> str:
        return self.__database

    def get_username(self) -> str:
        return self.__username

    def get_password(self) -> str:
        return self.__password
