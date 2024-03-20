from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class RegistrationPage(Page):
    NAME_FIELD = (By.XPATH, "//input[@wized='fullNameInput']")
    PHONE_FIELD = (By.XPATH, "//*[@id='phone2']")
    EMAIL_FIELD = (By.XPATH, "//*[@id='Email-3']")
    PASSWORD_FIELD = (By.XPATH, "//*[@id='field']")

    def element_visible(self):
        self.wait_element_visible(*self.NAME_FIELD)

    def name_information(self, information):
        self.input_text(information, *self.NAME_FIELD)

    def phone_number_information(self, phone):
        self.input_text(phone, *self.PHONE_FIELD)

    def email_address_information(self, email):
        self.input_text(email, *self.EMAIL_FIELD)

    def password_information(self, password):
        self.input_text(password, *self.PASSWORD_FIELD)

    def verify_information(self, expected_information: dict):
        self.verify_text(expected_information['email'], *self.EMAIL_FIELD)
        self.verify_text(expected_information['password'], *self.PASSWORD_FIELD)
        self.verify_text(expected_information['name'], *self.NAME_FIELD)
        self.verify_text(expected_information['phone'], *self.PHONE_FIELD)
