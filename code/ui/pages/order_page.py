from ui.locators.order_locators import OrderPageLocators
from ui.pages.base_page import BasePage


class OrderPage(BasePage):
    url = BasePage.url + 'orders/'
    locators = OrderPageLocators()

    def _check_state(self):
        assert self.is_opened(check_method=self._url_contains())

