import logging

from ui.locators.base_locators import BasePageLocators

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

from utils.decorators import wait

logger = logging.getLogger('pytest')


class PageNotLoadedException(Exception):
    pass


class BasePage(object):
    DEFAULT_TIMEOUT = 10
    CLICK_RETRY = 3

    locators = BasePageLocators()
    url = 'http://127.0.0.1:8080/'

    def __init__(self, driver: webdriver):
        self.driver: webdriver = driver

        self._check_state()

    def _check_state(self):
        assert self.is_opened()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = self.DEFAULT_TIMEOUT

        return WebDriverWait(self.driver, timeout)

    def click(self, locator, timeout=None):
        for i in range(self.CLICK_RETRY):
            logger.info(f'Clicking on {locator}. Try {i + 1} of {self.CLICK_RETRY}...')
            try:
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i == self.CLICK_RETRY - 1:
                    raise

    def find(self, locator, timeout=None):
        logger.info(f'Finding element "{locator}"...')
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def is_opened(self, check_method=None):
        if check_method is None:
            check_method = self._url_equals
        return wait(check_method, error=PageNotLoadedException, check=True, timeout=self.DEFAULT_TIMEOUT, interval=0.2)

    def _url_equals(self):
        if self.driver.current_url != self.url:
            raise PageNotLoadedException(
                f'{self.url} did not opened in {self.DEFAULT_TIMEOUT} for {self.__class__.__name__}, '
                f'current url: {self.driver.current_url}')

        return True

    def _url_contains(self):
        if self.url not in self.driver.current_url:
            raise PageNotLoadedException(
                f'{self.url} did not opened in {self.DEFAULT_TIMEOUT} for {self.__class__.__name__}, '
                f'current url: {self.driver.current_url}')
        return True

    def keys_to_input(self, locator, keys):
        logger.info(f'Sending keys "{keys}" to {locator}')
        inp = self.wait().until(EC.element_to_be_clickable(locator))
        inp.clear()
        inp.send_keys(keys)

    def element_exists(self, locator) -> bool:
        return len(self.driver.find_elements(*locator)) != 0

    @staticmethod
    def format_locator(locator, *args) -> tuple:
        return locator[0], locator[1].format(*args)
