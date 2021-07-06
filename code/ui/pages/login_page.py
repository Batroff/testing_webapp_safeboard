from ui.locators.login_locators import LoginPageLocators
from ui.pages.base_page import BasePage


class LoginPage(BasePage):
    locators = LoginPageLocators()
    url = BasePage.url + 'login'

    def login(self, credentials):
        self.keys_to_input(self.locators.INPUT_LOGIN, credentials[0])
        self.keys_to_input(self.locators.INPUT_PASSWORD, credentials[1])
        self.click(self.locators.BUTTON_SUBMIT)
