from ui.locators.home_locators import HomePageLocators
from ui.pages.base_page import BasePage
from ui.pages.books_page import BooksPage
from ui.pages.cart_page import CartPage
from ui.pages.reg_page import RegPage


class HomePage(BasePage):
    locators = HomePageLocators()

    def go_to_reg_page(self):
        self.click(self.locators.BTN_REG)
        return RegPage(driver=self.driver)

    def go_to_books_page(self):
        self.click(self.locators.BTN_BOOKS)
        return BooksPage(driver=self.driver)

    def go_to_cart_page(self):
        self.click(self.locators.BTN_CART)
        return CartPage(driver=self.driver)
