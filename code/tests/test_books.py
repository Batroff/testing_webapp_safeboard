import pytest

from tests.base import Base


class TestBooks(Base):

    def prepare(self):
        self.books_page = self.home_page.go_to_books_page()
        self.books = self.books_page.get_books(quantity=5)

    def get_books_info(self):
        return [self.books_page.get_book_info(book) for book in self.books]

    def get_books_ids(self):
        return [self.books_page.get_book_ids(book) for book in self.books]

    def get_books_cart_btn(self):
        return [self.books_page.get_book_cart_btn(book) for book in self.books]

    def test_books_info(self):
        books_info = self.get_books_info()

        for info in books_info:
            for k, v in info.items():
                assert v != '', f'book "{info["title"]}": {k} is empty!'

    def test_books_price(self):
        books_info = self.get_books_info()

        for info in books_info:
            price = float(info['price'].strip().split(' ')[0])
            price_old = float(info['price_old'].strip().split(' ')[0])

            assert price > 0.0, f'book "{info["title"]}" price: {price} <= 0!'
            assert price_old > 0.0, f'book "{info["title"]}" old price: {price_old} <= 0!'

    def test_books_id(self):
        books_ids = self.get_books_ids()

        for ids in books_ids:
            id_13 = ids['id_13'].strip().split(' ')[-1]
            id_10 = ids['id_10'].strip().split(' ')[-1]

            assert id_13[3] == '-', f'{id_13} does not have "-"'

            id_13 = id_13[0:3] + id_13[4:]
            assert len(id_13) == 13, f'{id_13} len != 13'
            assert id_13.isnumeric(), f'{id_13} has not only digits'

            assert len(id_10) == 10, f'{id_10} len != 10'
            assert id_10.isnumeric(), f'{id_10} has not only digits'

    def test_book_cart_btn(self):
        books_btn = self.get_books_cart_btn()

        for btn in books_btn:
            assert btn is not None
