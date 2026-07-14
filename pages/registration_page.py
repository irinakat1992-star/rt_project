from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage(BasePage):
    # Локаторы
    ENTER_WITH_PASSWORD_BTN = (By.ID, "standard_auth_btn")
    FIRST_NAME_INPUT = (By.NAME, "firstName")
    LAST_NAME_INPUT = (By.NAME, "lastName")
    REGION_SELECT = (By.XPATH, "//input[@autocomplete='new-password' and @type='text']")
    EMAIL_INPUT = (By.ID, "address")
    PASSWORD_INPUT = (By.ID, "password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "password-confirm")
    REGISTER_BTN = (By.NAME, "register")
    REGISTER_LINK = (By.ID, "kc-register")
    BACK_BTN = (By.XPATH, "//*[@id='register-back']")


    # Сообщения об ошибках
    NAME_ERROR = (By.XPATH, "//span[contains(text(), 'Необходимо заполнить поле кириллицей')]")
    PASSWORD_ERROR = (By.XPATH, "//span[contains(text(), 'Длина пароля должна быть')]")
    EMAIL_ERROR = (By.XPATH, "//span[contains(text(), 'Введите телефон в формате')]")
    GENERAL_ERROR = (By.XPATH, "//div[contains(@class, 'error')]//span")

    # Ссылки на политику
    PDN_LINK = (By.ID, "rt-auth-pdn-link")
    USER_AGREEMENT_LINK = (By.ID, "rt-auth-agreement-link")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self, url):
        self.driver.get(url)
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
        self.click_element(self.ENTER_WITH_PASSWORD_BTN)
        self.click_element(self.REGISTER_LINK)

    def enter_first_name(self, name):
        self.send_keys(self.FIRST_NAME_INPUT, name)

    def enter_last_name(self, surname):
        self.send_keys(self.LAST_NAME_INPUT, surname)

    def enter_email(self, email):
        self.send_keys(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_INPUT, password)

    def enter_confirm_password(self, password):
        self.send_keys(self.CONFIRM_PASSWORD_INPUT, password)

    def click_register(self):
        self.click_element(self.REGISTER_BTN)

    def click_register_link(self):
        self.click_element(self.REGISTER_LINK)

    def click_register_back(self):
        self.click_element(self.BACK_BTN)

    def get_name_error(self):
        return self.get_text(self.NAME_ERROR)

    def get_password_error(self):
        return self.get_text(self.PASSWORD_ERROR)

    def get_email_error(self):
        return self.get_text(self.EMAIL_ERROR)

    def get_error_message(self):
        return self.get_text(self.GENERAL_ERROR)