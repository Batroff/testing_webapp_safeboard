import pytest

from tests.base import Base


class TestBooks(Base):

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
    def test_books_info(self, title):
        info = self.books_page.get_book_info(title)

        for k, v in info.items():
            assert v != '', f'book "{info["title"]}": {k} is empty!'

    @pytest.mark.parametrize('title', titles, ids=['1', '2', '3', '4', '5'])
    def test_books_price(self, title):
        info = self.books_page.get_book_info(title)

        price = float(info['price'].strip().split(' ')[0])
        assert price > 0.0, f'book "{info["title"]}" price: {price} <= 0!'

        price_old = float(info['price_old'].strip().split(' ')[0])
        assert price_old > 0.0, f'book "{info["title"]}" old price: {price_old} <= 0!'

    @pytest.mark.parametrize('title', titles, ids=['1', '2', '3', '4', '5'])
    def test_books_id(self, title):
        ids = self.books_page.get_book_info(title)

        id_13 = ids['id_13'].strip().split(' ')[-1]
        id_10 = ids['id_10'].strip().split(' ')[-1]

        assert id_13[3] == '-', f'{id_13} does not have "-"'

        id_13 = id_13[0:3] + id_13[4:]
        assert len(id_13) == 13, f'{id_13} len != 13'
        assert id_13.isnumeric(), f'{id_13} has not only digits'

        assert len(id_10) == 10, f'{id_10} len != 10'
        assert id_10.isnumeric(), f'{id_10} has not only digits'

    @pytest.mark.parametrize('title', titles, ids=['1', '2', '3', '4', '5'])
    def test_book_cart_btn(self, title):
        books_btn = self.books_page.get_book_cart_btn(title)

        assert books_btn is not None
