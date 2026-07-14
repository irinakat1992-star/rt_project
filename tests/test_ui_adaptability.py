import pytest
from selenium.webdriver.common.by import By

from pages.auth_page import AuthPage
import time


class TestUIAdaptability:

    """5. Адаптивность и интерфейс"""
    @pytest.mark.ui
    def test_tc036_mobile_device(self, driver, base_url):
        """TC-036: Отображение на мобильном устройстве"""
        # Устанавливаем размер окна для iPhone 14 Pro Max
        driver.set_window_size(393, 852)
        time.sleep(1)

        auth_page = AuthPage(driver)
        auth_page.open(base_url)
        auth_page.click_enter_with_password()

        # Проверяем отображение основных элементов на мобильном устройстве
        assert auth_page.is_element_visible(auth_page.USERNAME_INPUT), \
            "Поле ввода логина не отображается на мобильном устройстве"
        assert auth_page.is_element_visible(auth_page.PASSWORD_INPUT), \
            "Поле ввода пароля не отображается на мобильном устройстве"

        # Проверяем, что все табы отображаются
        assert auth_page.is_element_visible(auth_page.TAB_PHONE), \
            "Таб 'Номер' не отображается на мобильном устройстве"
        assert auth_page.is_element_visible(auth_page.TAB_EMAIL), \
            "Таб 'Почта' не отображается на мобильном устройстве"
        assert auth_page.is_element_visible(auth_page.TAB_LOGIN), \
            "Таб 'Логин' не отображается на мобильном устройстве"
        assert auth_page.is_element_visible(auth_page.TAB_ACCOUNT), \
            "Таб 'Лицевой счет' не отображается на мобильном устройстве"

        # Проверяем, что кнопка "Войти" отображается
        assert auth_page.is_element_visible(auth_page.LOGIN_BTN), \
            "Кнопка 'Войти' не отображается на мобильном устройстве"

        # Проверяем, что ссылка "Забыл пароль" отображается
        assert auth_page.is_element_visible(auth_page.FORGOT_PASSWORD_LINK), \
            "Ссылка 'Забыл пароль' не отображается на мобильном устройстве"

        # Проверяем, что все элементы видны на экране (без горизонтальной прокрутки)
        # Получаем ширину страницы
        page_width = driver.execute_script("return document.documentElement.scrollWidth")
        window_width = driver.execute_script("return window.innerWidth")
        assert page_width <= window_width, \
            f"Страница имеет горизонтальную прокрутку. Ширина страницы: {page_width}, ширина окна: {window_width}"

        # Проверяем, что нет перекрытия элементов
        username_element = auth_page.get_element(auth_page.USERNAME_INPUT)
        password_element = auth_page.get_element(auth_page.PASSWORD_INPUT)

        # Проверяем, что элементы находятся в видимой области
        is_username_visible = driver.execute_script(
            "var rect = arguments[0].getBoundingClientRect(); "
            "return rect.top >= 0 && rect.left >= 0 && "
            "rect.bottom <= window.innerHeight && rect.right <= window.innerWidth;",
            username_element
        )
        assert is_username_visible, "Поле ввода логина находится за пределами видимой области"

        is_password_visible = driver.execute_script(
            "var rect = arguments[0].getBoundingClientRect(); "
            "return rect.top >= 0 && rect.left >= 0 && "
            "rect.bottom <= window.innerHeight && rect.right <= window.innerWidth;",
            password_element
        )
        assert is_password_visible, "Поле ввода пароля находится за пределами видимой области"

    @pytest.mark.ui
    def test_tc037_tablet_device(self, driver, base_url):
        """TC-037: Отображение на планшете"""
        # Устанавливаем размер окна для iPad Air
        driver.set_window_size(820, 1180)
        time.sleep(1)

        auth_page = AuthPage(driver)
        auth_page.open(base_url)
        auth_page.click_enter_with_password()

        # Проверяем отображение основных элементов на планшете
        assert auth_page.is_element_visible(auth_page.USERNAME_INPUT), \
            "Поле ввода логина не отображается на планшете"
        assert auth_page.is_element_visible(auth_page.PASSWORD_INPUT), \
            "Поле ввода пароля не отображается на планшете"

        # Проверяем, что все табы отображаются
        assert auth_page.is_element_visible(auth_page.TAB_PHONE), \
            "Таб 'Номер' не отображается на планшете"
        assert auth_page.is_element_visible(auth_page.TAB_EMAIL), \
            "Таб 'Почта' не отображается на планшете"
        assert auth_page.is_element_visible(auth_page.TAB_LOGIN), \
            "Таб 'Логин' не отображается на планшете"
        assert auth_page.is_element_visible(auth_page.TAB_ACCOUNT), \
            "Таб 'Лицевой счет' не отображается на планшете"

        # Проверяем, что кнопка "Войти" отображается
        assert auth_page.is_element_visible(auth_page.LOGIN_BTN), \
            "Кнопка 'Войти' не отображается на планшете"

        # Проверяем, что ссылка "Забыл пароль" отображается
        assert auth_page.is_element_visible(auth_page.FORGOT_PASSWORD_LINK), \
            "Ссылка 'Забыл пароль' не отображается на планшете"

        # Проверяем, что все элементы видны на экране (без горизонтальной прокрутки)
        page_width = driver.execute_script("return document.documentElement.scrollWidth")
        window_width = driver.execute_script("return window.innerWidth")
        assert page_width <= window_width, \
            f"Страница имеет горизонтальную прокрутку. Ширина страницы: {page_width}, ширина окна: {window_width}"

        # Проверяем, что нет перекрытия элементов
        username_element = auth_page.get_element(auth_page.USERNAME_INPUT)
        password_element = auth_page.get_element(auth_page.PASSWORD_INPUT)

        # Проверяем, что элементы находятся в видимой области
        is_username_visible = driver.execute_script(
            "var rect = arguments[0].getBoundingClientRect(); "
            "return rect.top >= 0 && rect.left >= 0 && "
            "rect.bottom <= window.innerHeight && rect.right <= window.innerWidth;",
            username_element
        )
        assert is_username_visible, "Поле ввода логина находится за пределами видимой области"

        is_password_visible = driver.execute_script(
            "var rect = arguments[0].getBoundingClientRect(); "
            "return rect.top >= 0 && rect.left >= 0 && "
            "rect.bottom <= window.innerHeight && rect.right <= window.innerWidth;",
            password_element
        )
        assert is_password_visible, "Поле ввода пароля находится за пределами видимой области"