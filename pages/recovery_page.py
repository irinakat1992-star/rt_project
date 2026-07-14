from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RecoveryPage(BasePage):
    ENTER_WITH_PASSWORD_BTN = (By.ID, "standard_auth_btn")
    FORGOT_PASSWORD_LINK = (By.ID, "forgot_password")
    EMAIL_INPUT = (By.ID, "username")
    CONTINUE_BTN = (By.ID, "reset")
    BACK_BTN = (By.ID, "reset-back")
    BY_EMAIL_LINK = (By.ID, "t-btn-tab-mail")


    def __init__(self, driver):
        super().__init__(driver)

    def open(self, url):
        self.driver.get(url)
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        self.click_element(self.ENTER_WITH_PASSWORD_BTN)
        self.click_element(self.FORGOT_PASSWORD_LINK)

    def select_recovery_by_email(self):
        self.click_element(self.BY_EMAIL_LINK)

    def enter_email(self, email):
        self.send_keys(self.EMAIL_INPUT, email)

    def back_to_auth(self):
        self.click_element(self.BACK_BTN)