from faker import Faker
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import pytest
from ui.pages.home_page import HomePage

fake = Faker()


@pytest.fixture
def home_page(driver):
    return HomePage(driver=driver)


@pytest.fixture(scope='function')
def userdata() -> dict:
    password = fake.password(length=fake.random_int(min=5, max=200))
    return {
        'name': fake.name(),
        'username': fake.bothify('???#?' * fake.random_int(min=1, max=100)),
        'password': password,
        'confirm_password': password
    }


@pytest.fixture(scope='function')
def driver(config):
    # caps = {
    #     'browserName': 'chrome',
    #     'version': '91.0',
    #     'selenoid:options': {
    #         'enableVNC': True
    #     }
    # }
    # driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
    #                           desired_capabilities=caps)
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get('http://127.0.0.1:8080/')
    driver.maximize_window()

    yield driver

    driver.quit()
