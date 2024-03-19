from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def open(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_element(*locator)

    def wait_element_visible(self, *locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element by {locator} is not clickable'
        )

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self, expected_information, *locator):
        actual_information = self.find_element(*locator).get_attribute('value')
        assert expected_information == actual_information, \
            f"Expected '{expected_information}' but got '{actual_information}'"
        print(actual_information)
