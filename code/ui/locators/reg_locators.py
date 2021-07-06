from ui.locators.base_locators import BasePageLocators
from selenium.webdriver.common.by import By


class RegPageLocators(BasePageLocators):
    INPUT_TEMPLATE = (By.XPATH, '//input[@id="{0}"]')
    INPUT_NAME = (INPUT_TEMPLATE[0], INPUT_TEMPLATE[1].format('name'))
    INPUT_LOGIN = (INPUT_TEMPLATE[0], INPUT_TEMPLATE[1].format('username'))
    INPUT_PASSWORD = (INPUT_TEMPLATE[0], INPUT_TEMPLATE[1].format('password'))
    INPUT_CONFIRM_PASSWORD = (INPUT_TEMPLATE[0], INPUT_TEMPLATE[1].format('password-confirm'))

    BUTTON_REGISTER = (By.XPATH, '//button[text()="Зарегистрироваться"]')

    MSG_TEMPLATE = (By.XPATH, '//div[contains(text(), "{0}")]')
