from ui.locators.base_locators import BasePageLocators
from selenium.webdriver.common.by import By


class HomePageLocators(BasePageLocators):

    BTN_REG = (By.XPATH, '//a//strong[text()="Регистрация"]')
    BTN_LOGIN = (By.XPATH, '//a//span[text()="Войти"]')
    BTN_BOOKS = (By.XPATH, '//a[@href="/books"]')
    BTN_CART = (By.XPATH, '//a[@href="/cart"]')
