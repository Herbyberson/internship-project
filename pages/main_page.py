from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):

    def open_page(self):
        self.open('https://soft.reelly.io/sign-up')
