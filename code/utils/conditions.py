
class elements_quantity_equals_to(object):

    def __init__(self, locator, quantity):
        self.locator = locator
        self.quantity = quantity

    def __call__(self, driver):
        elements = driver.find_elements(*self.locator)
        if len(elements) == self.quantity:
            return elements
        else:
            return False
