from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=0.5)

    def click_element(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            raise

    def send_keys(self, locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            raise

    def get_text(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text
        except TimeoutException:
            return None

    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_element_present(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_element(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return None

    def switch_to_tab(self, tab_name):
        from selenium.webdriver.common.by import By
        tabs = {
            "Номер": (By.XPATH, "//*[@id='t-btn-tab-phone']"),
            "Почта": (By.XPATH, "//*[@id='t-btn-tab-mail']"),
            "Логин": (By.XPATH, "//*[@id='t-btn-tab-login']"),
            "Лицевой счет": (By.XPATH, "//*[@id='t-btn-tab-ls']")
        }
        tab_locator = tabs.get(tab_name)
        if tab_locator:
            self.click_element(tab_locator)