import logging
import os
import shutil

import allure
from faker import Faker

from api.client import ApiClient
from ui.fixtures import *
from _pytest.config.argparsing import Parser
from _pytest.fixtures import FixtureRequest


def pytest_addoption(parser: Parser):
    parser.addoption('--selenoid', action='store_true')


def pytest_configure(config):
    base_test_dir = os.path.join('/tmp', 'tests')

    if not hasattr(config, 'workerinput'):
        # Recreate test directories
        if os.path.exists(base_test_dir):
            shutil.rmtree(base_test_dir)
        os.makedirs(base_test_dir)

    config.base_test_dir = base_test_dir


@pytest.fixture
def api_client():
    return ApiClient('http://localhost:8080')


@pytest.fixture(scope='session')
def config(request: FixtureRequest) -> dict:
    cfg = {
        'selenoid': request.config.getoption('--selenoid')
    }

    return cfg


@pytest.fixture
def cookies(api_client, credentials):
    api_client.register(credentials)
    login_resp = api_client.login(credentials)

    return login_resp.cookies


@pytest.fixture
def credentials():
    fake = Faker()
    return {
        'username': fake.bothify('??????##'),
        'password': fake.lexify('??????')
    }


@pytest.fixture(scope='function')
def test_dir(request) -> str:
    test_dir = os.path.join(request.config.base_test_dir, request._pyfuncitem.nodeid.replace('::', '-'))
    os.makedirs(test_dir)
    return test_dir


@pytest.fixture(scope='session')
def repo_root() -> str:
    return os.path.abspath(os.path.join(__file__, os.pardir))


@pytest.fixture(scope='function', autouse=True)
def logger(test_dir):
    log_formatter = logging.Formatter('%(asctime)s - %(filename)-15s - %(levelname)-6s - %(message)s')
    log_file = os.path.join(test_dir, 'pytest.log')

    log_level = logging.INFO

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('pytest')
    log.propagate = False
    log.setLevel(log_level)
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()

    with open(log_file, 'r') as f:
        allure.attach(f.read(), 'pytest.log', attachment_type=allure.attachment_type.TEXT)