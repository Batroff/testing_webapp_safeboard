import os

import allure
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
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get('http://127.0.0.1:8080/')
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def ui_report(driver, request, test_dir):
    failed_tests_count = request.session.testsfailed
    yield
    if request.session.testsfailed > failed_tests_count:
        screenshot_file = os.path.join(test_dir, 'failure.png')
        driver.get_screenshot_as_file(screenshot_file)
        allure.attach.file(screenshot_file, 'failure.png', attachment_type=allure.attachment_type.PNG)

        browser_logfile = os.path.join(test_dir, 'browser.log')
        with open(browser_logfile, 'w') as f:
            for i in driver.get_log('browser'):
                f.write(f"{i['level']} - {i['source']}\n{i['message']}\n\n")

        with open(browser_logfile, 'r') as f:
            allure.attach(f.read(), 'browser.log', attachment_type=allure.attachment_type.TEXT)
