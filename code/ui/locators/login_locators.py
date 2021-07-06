from ui.locators.base_locators import BasePageLocators
from selenium.webdriver.common.by import By


class LoginPageLocators(BasePageLocators):
    INPUT_LOGIN = (By.ID, 'username')
    INPUT_PASSWORD = (By.ID, 'password')
    BUTTON_SUBMIT = (By.ID, 'submit')

