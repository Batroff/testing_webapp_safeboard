from ui.locators.base_locators import BasePageLocators
from selenium.webdriver.common.by import By


class CartPageLocators(BasePageLocators):
    FINAL_PRICE = (By.CSS_SELECTOR, 'div.panel strong')
    BOOK_PRICE = (By.XPATH, '//article[.//*[contains(text(),"{0}")]]//strong')
    QUANTITY_INPUT = (By.XPATH, '//article[.//*[contains(text(),"{0}")]]//input')
    BTN_UPDATE = (By.XPATH, '//article[.//*[contains(text(),"{0}")]]//button[text()="Обновить"]')
    BTN_REMOVE = (By.XPATH, '//article[.//*[contains(text(),"{0}")]]//button[text()="Удалить"]')
    BTN_BUY = (By.XPATH, '//button[contains(text(),"Купить")]')
