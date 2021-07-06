from ui.locators.base_locators import BasePageLocators
from selenium.webdriver.common.by import By


class BooksPageLocators(BasePageLocators):
    BOOK_TEMPLATE = (By.XPATH, '//article[.//*[contains(text(),"{0}")]]')

    BOOK_AUTHOR = (By.XPATH, BOOK_TEMPLATE[1] + '//p[contains(@class, "subtitle")]')
    BOOK_TITLE = (By.XPATH, BOOK_TEMPLATE[1] + '//h2[contains(@class, "title")]')
    BOOK_RATING = (By.XPATH, BOOK_TEMPLATE[1] + '//div[contains(@class, "level")]')
    BOOK_DESCRIPTION = (By.XPATH, BOOK_TEMPLATE[1] + '//*[contains(@class, "level")]/following-sibling::p')
    BOOK_PRICE = (By.XPATH, BOOK_TEMPLATE[1] + '//div[contains(@class, "hero")]//strong')
    BOOK_PRICE_OLD = (By.XPATH, BOOK_TEMPLATE[1] + '//small[contains(text(),"Старая цена:")]//span')
    BOOK_ID_13 = (By.XPATH, BOOK_TEMPLATE[1] + '//p[.//strong[text()="ISBN-13"]]')
    BOOK_ID_10 = (By.XPATH, BOOK_TEMPLATE[1] + '//p[.//strong[text()="ISBN-10"]]')
    BOOK_ADD_TO_CART = (By.XPATH, BOOK_TEMPLATE[1] + '//span[text()="Добавить в корзину"]')
