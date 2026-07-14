import os
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AuthPage(BasePage):
    # Локаторы
    ENTER_WITH_PASSWORD_BTN = (By.ID, "standard_auth_btn")
    USERNAME_INPUT = (By.ID, "username")
    USERNAME_CODE_INPUT = (By.ID, "address")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.ID, "kc-login")
    FORGOT_PASSWORD_LINK = (By.ID, "forgot_password")
    ERROR_MESSAGE = (By.ID, "form-error-message")
    ERROR_MESSAGE_USERNAME = (By.ID, "username-meta")
    PASSWORD_TOGGLE = (By.XPATH, "//*[contains(@class, 'rt-eye-icon')]")

    # Табы
    TAB_PHONE = (By.ID, "t-btn-tab-phone")
    TAB_EMAIL = (By.ID, "t-btn-tab-mail")
    TAB_LOGIN = (By.ID, "t-btn-tab-login")
    TAB_ACCOUNT = (By.ID, "t-btn-tab-ls")

    # Кнопки для кода
    GET_CODE_BTN = (By.ID, "otp_get_code")
    CHANGE_EMAIL_BTN = (By.ID, "otp-back")
    CODE_INPUTS = (By.XPATH, "//*[@id='page-right']/div/div/div/form/div/div")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self, url):
        self.driver.get(url)
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    def click_enter_with_password(self):
        self.click_element(self.ENTER_WITH_PASSWORD_BTN)

    def switch_to_phone_tab(self):
        self.click_element(self.TAB_PHONE)

    def switch_to_email_tab(self):
        self.click_element(self.TAB_EMAIL)

    def switch_to_login_tab(self):
        self.click_element(self.TAB_LOGIN)

    def switch_to_account_tab(self):
        self.click_element(self.TAB_ACCOUNT)

    def enter_username(self, username):
        self.send_keys(self.USERNAME_INPUT, username)

    def enter_code_username(self, username):
        self.send_keys(self.USERNAME_CODE_INPUT, username)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click_element(self.LOGIN_BTN)

    def click_forgot_password(self):
        self.click_element(self.FORGOT_PASSWORD_LINK)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def get_username_error_message(self):
        return self.get_text(self.ERROR_MESSAGE_USERNAME)

    def toggle_password(self):
        self.click_element(self.PASSWORD_TOGGLE)

    def is_password_visible(self):
        password_input = self.get_element(self.PASSWORD_INPUT)
        return password_input.get_attribute("type") == "text"

    def login_with_credentials(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_code(self):
        self.click_element(self.GET_CODE_BTN)

    def change_email(self):
        self.click_element(self.CHANGE_EMAIL_BTN)

    def is_tab_selected(self, tab_name):
        tab_map = {
            "Номер": self.TAB_PHONE,
            "Почта": self.TAB_EMAIL,
            "Логин": self.TAB_LOGIN,
            "Лицевой счет": self.TAB_ACCOUNT
        }
        tab = self.get_element(tab_map[tab_name])
        return "active" in tab.get_attribute("class") or "selected" in tab.get_attribute("class")

    def is_forgot_password_link_orange(self):
        link = self.get_element(self.FORGOT_PASSWORD_LINK)
        color = link.value_of_css_property("color")
        return "orange" in color.lower() or "255" in color or "rgb(255," in color