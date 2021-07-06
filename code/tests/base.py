import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.home_page import HomePage


class Base:
    driver = None
    authorize = False

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest, cookies):
        self.driver = driver

        if self.authorize:
            session_cookie = [c for c in cookies if c.name == 'sessionup'][0]
            self.driver.add_cookie({
                'name': session_cookie.name,
                'value': session_cookie.value
            })
            self.driver.refresh()

        self.home_page: HomePage = request.getfixturevalue('home_page')
        self.prepare()

    def prepare(self):
        pass
