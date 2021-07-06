from ui.locators.base_locators import BasePageLocators
from selenium.webdriver.common.by import By


class OrderPageLocators(BasePageLocators):
    ROW_TEMPLATE = (By.XPATH, '//tbody//tr[.//a[text()="{0}"]]')
    QUANTITY_TEMPLATE = (By.XPATH, '//tbody//tr[.//a[text()="{0}"]]//td[2]')
    ID_TEMPLATE = (By.XPATH, '//tbody//tr[.//a[text()="{0}"]]//th')

    FINAL_QUANTITY = (By.XPATH, '//tfoot//tr//th[3]')
    CREATE_TIME = (By.XPATH, '//p[contains(text(),"Заказ оформлен")]')
    DELIVERY_TIME = (By.XPATH, '//p[contains(text(),"Дата доставки")]//span')
    ORDER_TITLE = (By.CSS_SELECTOR, 'h1.title')
