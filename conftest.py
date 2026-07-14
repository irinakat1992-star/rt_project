import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import sys
import os
from dotenv import load_dotenv

load_dotenv()

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=os.getenv("browser", "chrome"),
                     help="Browser: chrome or firefox")
    parser.addoption("--headless", action="store_true",
                     default=os.getenv("headless", "false").lower() == "true",
                     help="Run browser in headless mode")

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    implicit_wait = int(os.getenv("implicit_wait", 5))
    driver.implicitly_wait(implicit_wait)

    yield driver

    driver.quit()

@pytest.fixture(scope="function")
def base_url():
    """Получение базового URL из переменных окружения"""
    return os.getenv("base_url", "https://lk.rt.ru/")

@pytest.fixture(scope="function")
def test_data():
    """Получение тестовых данных из переменных окружения"""
    return {
        "valid_email": os.getenv("valid_email", "merci8207@web-library.net"),
        "valid_password": os.getenv("valid_password", "332211QWErty"),
        "valid_login": os.getenv("valid_login", "rtkid_1783790624184"),
        "invalid_phone": os.getenv("invalid_phone", "123"),
        "unregistered_phone": os.getenv("unregistered_phone", "2228889999"),
        "invalid_password": os.getenv("invalid_password", "WrongPassword123!"),
        "nonexistent_login": os.getenv("nonexistent_login", "nonexistent_login321"),
        "nonexistent_ls": os.getenv("nonexistent_ls", "111111111111"),
        "test_email": os.getenv("test_email", "merci8207@web-library.net"),
        "test_password": os.getenv("test_password", "332211QWErty"),
    }

@pytest.fixture(scope="function")
def timeout():
    """Получение таймаута из переменных окружения"""
    return int(os.getenv("default_timeout", 5))