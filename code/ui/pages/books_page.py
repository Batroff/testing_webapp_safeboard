from ui.locators.books_locators import BooksPageLocators
from ui.pages.base_page import BasePage


class BooksPage(BasePage):
    url = BasePage.url + 'books'
    locators = BooksPageLocators()

    def get_book_info(self, title):
        book_info = {
            'author': self.find(self.format_locator(self.locators.BOOK_AUTHOR, title)).text,
            'title': self.find(self.format_locator(self.locators.BOOK_TITLE, title)).text,
            'description': self.find(self.format_locator(self.locators.BOOK_DESCRIPTION, title)).text,
            'rating': self.find(self.format_locator(self.locators.BOOK_RATING, title)).text,
            'price': self.find(self.format_locator(self.locators.BOOK_PRICE, title)).text,
            'price_old': self.find(self.format_locator(self.locators.BOOK_PRICE_OLD, title)).text,
            'id_13': self.find(self.format_locator(self.locators.BOOK_ID_13, title)).text,
            'id_10': self.find(self.format_locator(self.locators.BOOK_ID_10, title)).text
        }

        return book_info

    def get_book_cart_btn(self, title):
        return self.find(self.format_locator(self.locators.BOOK_ADD_TO_CART, title))

    def get_book_by_title(self, title):
        return self.find(self.format_locator(self.locators.BOOK_TEMPLATE, title))

    def add_book_to_cart(self, title):
        self.click(self.format_locator(self.locators.BOOK_ADD_TO_CART, title))

    def add_books_to_cart(self, titles):
        for title in titles:
            self.add_book_to_cart(title)
