from ui.locators.base_locators import BasePageLocators
from selenium.webdriver.common.by import By


class BooksPageLocators(BasePageLocators):
    BOOK_TEMPLATE = (By.XPATH, '//article[.//*[contains(text(),"{0}")]]')

    BOOK_ARTICLE = (By.CSS_SELECTOR, 'article')
    BOOK_AUTHOR = (By.CSS_SELECTOR, 'p.subtitle')
    BOOK_TITLE = (By.CSS_SELECTOR, 'h2.title')
    BOOK_RATING = (By.CSS_SELECTOR, 'div.level')
    BOOK_DESCRIPTION = (By.CSS_SELECTOR, 'div.level + p')
    BOOK_PRICE = (By.CSS_SELECTOR, 'div.hero strong')
    BOOK_PRICE_OLD = (By.XPATH, './/small[contains(text(),"Старая цена:")]//span')
    BOOK_ID_13 = (By.XPATH, './/p[.//strong[text()="ISBN-13"]]')
    BOOK_ID_10 = (By.XPATH, './/p[.//strong[text()="ISBN-10"]]')
    BOOK_ADD_TO_CART = (By.XPATH, './/span[text()="Добавить в корзину"]')
