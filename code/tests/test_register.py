from tests.base import Base
from faker import Faker
import pytest

from ui.fixtures import userdata

fake = Faker()


class TestRegistration(Base):

    def prepare(self):
        self.reg_page = self.home_page.go_to_reg_page()

    def test_correct_reg(self, userdata):
        self.reg_page.register(userdata=userdata)

        assert self.reg_page.is_msg_exists('Регистрация прошла успешно!')

    def test_without_name(self, userdata):
        userdata['name'] = ''

        self.reg_page.register(userdata=userdata)

        assert self.reg_page.is_msg_exists('Регистрация прошла успешно!')

    @pytest.mark.parametrize('username',
                             ['', fake.lexify('#?#?')],
                             ids=['Empty', '4 symbols'])
    def test_wrong_login(self, userdata, username):
        userdata['username'] = username

        self.reg_page.register(userdata=userdata)

        assert self.reg_page.is_msg_exists('Укажите Username и Password.')

    @pytest.mark.parametrize('password', [
        '',
        fake.password(length=4),
        fake.lexify('????'),
        fake.numerify('####'),
        fake.lexify('???????'),
        fake.numerify('########'),
    ], ids=['Empty', '4 mixed', '4 symbols', '4 numbers', 'Without number', 'Without letter'])
    def test_wrong_password(self, userdata, password):
        userdata['password'] = password

        self.reg_page.register(userdata=userdata)

        assert self.reg_page.is_msg_exists('Укажите Username и Password.')
