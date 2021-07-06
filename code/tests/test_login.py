import pytest

from api.client import ApiClient
from tests.base import Base


class TestLogin(Base):

    def prepare(self):
        self.api_client = ApiClient(url='http://localhost:8080/')
        self.login_page = self.home_page.go_to_login_page()

    def test_login(self):
        userdata = {
            'username': 'Testing_admin',
            'password': 'qwerty123'
        }

        self.api_client.register(userdata)
        books_page = self.login_page.login(userdata)
        assert books_page.is_opened()
