from ui.locators.base_locators import BasePageLocators
from selenium.webdriver.common.by import By


class HomePageLocators(BasePageLocators):

    BTN_TEMPLATE = (By.XPATH, '//a//strong[text()="{0}"]')
    BTN_REG = (BTN_TEMPLATE[0], BTN_TEMPLATE[1].format('Регистрация'))
    BTN_LOGIN = (BTN_TEMPLATE[0], BTN_TEMPLATE[1].format('Войти'))
    BTN_BOOKS = (By.XPATH, '//a[@href="/books"]')
    BTN_CART = (By.XPATH, '//a[@href="/cart"]')
