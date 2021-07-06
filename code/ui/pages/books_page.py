from ui.locators.books_locators import BooksPageLocators
from ui.pages.base_page import BasePage
from utils.conditions import elements_quantity_equals_to


class BooksPage(BasePage):
    url = BasePage.url + 'books'
    locators = BooksPageLocators()

    def get_books(self, quantity):
        return self.wait() \
            .until(elements_quantity_equals_to(
            locator=self.locators.BOOK_ARTICLE,
            quantity=quantity
        ))

    def get_book_info(self, book):
        book_info = {
            'author': book.find_element(*self.locators.BOOK_AUTHOR).text,
            'title': book.find_element(*self.locators.BOOK_TITLE).text,
            'description': book.find_element(*self.locators.BOOK_DESCRIPTION).text,
            'rating': book.find_element(*self.locators.BOOK_RATING).text,
            'price': book.find_element(*self.locators.BOOK_PRICE).text,
            'price_old': book.find_element(*self.locators.BOOK_PRICE_OLD).text
        }

        return book_info

    def get_book_ids(self, book):
        ids = {
            'id_13': book.find_element(*self.locators.BOOK_ID_13).text,
            'id_10': book.find_element(*self.locators.BOOK_ID_10).text,
        }

        return ids

    def get_book_cart_btn(self, book):
        return book.find_element(*self.locators.BOOK_ADD_TO_CART)

    def get_book_by_title(self, title):
        return self.find(self.format_locator(self.locators.BOOK_TEMPLATE, title))

    def get_book_price(self, book):
        price = book.find_element(*self.locators.BOOK_PRICE).text
        return float(price.strip().split(' ')[0])

    def add_book_to_cart(self, title):
        book = self.find(self.format_locator(self.locators.BOOK_TEMPLATE, title))
        book.find_element(*self.locators.BOOK_ADD_TO_CART).click()

    def add_books_to_cart(self, titles):
        for title in titles:
            self.add_book_to_cart(title)