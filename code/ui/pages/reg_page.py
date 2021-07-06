from ui.locators.reg_locators import RegPageLocators
from ui.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class RegPage(BasePage):
    locators = RegPageLocators()
    url = BasePage.url + 'signup'

    def register(self, userdata: dict):
        self.keys_to_input(locator=self.locators.INPUT_NAME,
                           keys=userdata['name'])

        self.keys_to_input(locator=self.locators.INPUT_LOGIN,
                           keys=userdata['login'])

        self.keys_to_input(locator=self.locators.INPUT_PASSWORD,
                           keys=userdata['password'])

        self.keys_to_input(locator=self.locators.INPUT_CONFIRM_PASSWORD,
                           keys=userdata['confirm_password'])

        self.click(self.locators.BUTTON_REGISTER)

    def is_msg_exists(self, text):
        MSG_LOCATOR = (self.locators.MSG_TEMPLATE[0],
                       self.locators.MSG_TEMPLATE[1].format(text))

        return self.wait(timeout=10) \
            .until(EC.presence_of_element_located(MSG_LOCATOR))
