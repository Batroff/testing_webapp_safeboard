import datetime
import random

import pytest
from time import gmtime, strftime

from tests.base import Base

titles = [
    'Тестирование DOT COM',
    'A Friendly Introduction to Software Testing',
    'The Way of the Web Tester: A Beginner\'s Guide to Automating Tests',
    'Explore It!: Reduce Risk and Increase Confidence with Exploratory Testing',
    'Ключевые процессы тестирования'
]


class TestOrder(Base):
    """
    <abbr title="Error">№</abbr> - ошибка в DOM
    № должны быть уникальными
    """
    authorize = True

    def prepare(self):
        self.books_page = self.home_page.go_to_books_page()

    @pytest.mark.parametrize('title', titles, ids=['1', '2', '3', '4', '5'])
    def test_books_quantity(self, title):
        quantity = random.choice([1, 5, 10, 20])
        for i in range(quantity):
            self.books_page.add_book_to_cart(title)

        cart_page = self.home_page.go_to_cart_page()
        order_page = cart_page.go_to_order_page()

        order_quantity = order_page.get_book_quantity(title)
        assert quantity == order_quantity

        final_quantity = order_page.get_final_quantity()
        assert quantity == final_quantity


class TestOrderInfo(Base):
    authorize = True

    def prepare(self):
        self.books_page = self.home_page.go_to_books_page()

    def create_order(self):
        self.books_page.add_book_to_cart(titles[0])

        cart_page = self.home_page.go_to_cart_page()
        return cart_page.go_to_order_page()

    def test_order_create_time(self):
        self.books_page.add_book_to_cart(titles[0])
        curr_time = strftime("%d.%m.%Y %H:%M:%S", gmtime())

        order_page = self.create_order()
        create_time = order_page.get_create_time()

        assert curr_time == create_time

    def test_order_id_exist(self):
        self.books_page.add_book_to_cart(titles[0])

        order_page = self.create_order()

        title = order_page.get_order_title()
        assert title.strip().split(' #')[-1].isnumeric()

    def test_order_delivery_time(self):
        self.books_page.add_book_to_cart(titles[0])
        curr_date = datetime.date.today()

        order_page = self.create_order()

        delivery_date = datetime.date(*reversed([int(x) for x in order_page.get_delivery_time().split('-')]))
        assert delivery_date >= curr_date

