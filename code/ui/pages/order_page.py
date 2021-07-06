from ui.locators.order_locators import OrderPageLocators
from ui.pages.base_page import BasePage


class OrderPage(BasePage):
    url = BasePage.url + 'orders/'
    locators = OrderPageLocators()

    def _check_state(self):
        assert self.is_opened(check_method=self._url_contains)

    def get_book_quantity(self, title):
        element = self.find(self.format_locator(self.locators.QUANTITY_TEMPLATE, title))
        return int(element.text)

    def get_final_quantity(self):
        return int(self.find(self.locators.FINAL_QUANTITY).text)

    def get_book_id(self, title):
        element = self.find(self.format_locator(self.locators.ID_TEMPLATE, title))
        return int(element.text)

    def get_create_time(self):
        return ' '.join(self.find(self.locators.CREATE_TIME).text.rstrip().split(' ')[2:])

    def get_order_title(self):
        return self.find(self.locators.ORDER_TITLE).text

    def get_delivery_time(self):
        return self.find(self.locators.DELIVERY_TIME).text
