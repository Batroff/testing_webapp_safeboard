import time

import pytest
from selenium.common.exceptions import NoSuchElementException

from tests.base import Base


class TestCart(Base):
    """
    Обновить не работает
    Удалить удаляет все книги
    цены отображаются неправильно
    У input одинаковые id
    """

    authorize = True

    titles = [
        'Тестирование DOT COM',
        'A Friendly Introduction to Software Testing',
        'The Way of the Web Tester: A Beginner\'s Guide to Automating Tests',
        'Explore It!: Reduce Risk and Increase Confidence with Exploratory Testing',
        'Ключевые процессы тестирования'
    ]

    def prepare(self):
        self.books_page = self.home_page.go_to_books_page()

    @pytest.mark.parametrize('title', titles, ids=['1', '2', '3', '4', '5'])
    def test_book_price(self, title):
        book = self.books_page.get_book_by_title(title)
        price = self.books_page.get_book_price(book)

        self.books_page.add_book_to_cart(title)
        cart_page = self.home_page.go_to_cart_page()

        cart_book = self.books_page.get_book_by_title(title)
        cart_price = cart_page.get_book_price(cart_book)
        assert price == cart_price

        final_price = cart_page.get_final_price()
        book_quantity = cart_page.get_book_quantity(title)
        assert book_quantity * price == final_price

    def test_update_book_quantity(self):
        title = self.titles[0]

        book = self.books_page.get_book_by_title(title)
        self.books_page.add_book_to_cart(title)

        cart_page = self.home_page.go_to_cart_page()

        cart_page.change_book_quantity(title, quantity=5)
        cart_page.driver.refresh()
        quantity = cart_page.get_book_quantity(title)

        assert quantity == 5

    def test_delete_book_from_cart(self):
        self.books_page.add_books_to_cart(self.titles[0:2])

        cart_page = self.home_page.go_to_cart_page()
        cart_page.delete_book(self.titles[0])

        with pytest.raises(NoSuchElementException):
            self.books_page.get_book_by_title(self.titles[0])

        assert self.books_page.get_book_by_title(self.titles[1]) is not None
