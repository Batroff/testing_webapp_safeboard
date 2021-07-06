from ui.locators.login_locators import LoginPageLocators
from ui.pages.base_page import BasePage
from ui.pages.books_page import BooksPage


class LoginPage(BasePage):
    locators = LoginPageLocators()
    url = BasePage.url + 'login'

    def login(self, credentials, allow_redirect=True):
        self.keys_to_input(self.locators.INPUT_LOGIN, credentials['username'])
        self.keys_to_input(self.locators.INPUT_PASSWORD, credentials['password'])
        self.click(self.locators.BUTTON_SUBMIT)

        if allow_redirect:
            return BooksPage(driver=self.driver)
