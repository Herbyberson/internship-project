from pages.base_page import Page
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.registration_page = RegistrationPage(driver)
        self.main_page = MainPage(driver)





