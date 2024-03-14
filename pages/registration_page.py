from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class RegistrationPage(Page):
    FIRST_LAST_NAME_FIELDS = (By.XPATH, "//input[@wized='fullNameInput']")

    def element_visible(self):
        self.wait_element_visible(*self.FIRST_LAST_NAME_FIELDS)

    def enter_information(self, information):
        self.input_text(information, *self.FIRST_LAST_NAME_FIELDS)

    def verify_information(self, expected_information):
        self.verify_text(expected_information, *self.FIRST_LAST_NAME_FIELDS)