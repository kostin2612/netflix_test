from playwright.sync_api import Page

from config import BASE_URL
from locators.login_page_locators import LoginPageLocators


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(BASE_URL)

    def login(self, username, password):
        self.page.fill(LoginPageLocators.USERNAME_INPUT, username)
        self.page.fill(LoginPageLocators.PASSWORD_INPUT, password)
        self.page.click(LoginPageLocators.SUBMIT_BUTTON)

    def get_error_message(self):
        return self.page.inner_text(LoginPageLocators.ERROR_MESSAGE)

    def is_logged_in(self):
        return self.page.is_visible(LoginPageLocators.PROFILE_LABEL)
