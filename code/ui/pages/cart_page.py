from ui.locators.cart_locators import CartPageLocators
from ui.pages.base_page import BasePage


class CartPage(BasePage):
    url = BasePage.url + 'cart'
    locators = CartPageLocators()

    def get_final_price(self):
        return float(self.find(self.locators.FINAL_PRICE).text)

    def get_book_quantity(self, title):
        element = self.find(self.format_locator(self.locators.QUANTITY_INPUT, title))
        return int(element.get_attribute('value'))

    def get_book_price(self, book):
        price = book.find_element(*self.locators.BOOK_PRICE).text
        return float(price.rstrip().split(' ')[0])

    def change_book_quantity(self, title, quantity):
        locator = self.format_locator(self.locators.QUANTITY_INPUT, title)
        self.keys_to_input(locator=locator, keys=quantity)

        self.click(self.format_locator(self.locators.BTN_UPDATE, title))

    def delete_book(self, title):
        self.click(self.format_locator(self.locators.BTN_REMOVE, title))
