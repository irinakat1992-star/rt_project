import pytest
from pages.auth_page import AuthPage
import time


class TestAuthorization:

    """1. Стандартная авторизация пользователя по логину и паролю"""
    @pytest.mark.smoke
    def test_tc001_load_auth_page(self, driver, base_url):
        """TC-001: Загрузка страницы авторизации на сайте"""
        auth_page = AuthPage(driver)
        auth_page.open(base_url)
        auth_page.click_enter_with_password()

        assert auth_page.is_element_visible(auth_page.USERNAME_INPUT), "Поле ввода логина не отображается"
        assert auth_page.is_element_visible(auth_page.PASSWORD_INPUT), "Поле ввода пароля не отображается"
        assert auth_page.is_element_visible(auth_page.TAB_PHONE), "Таб 'Номер' не отображается"
        assert auth_page.is_element_visible(auth_page.TAB_EMAIL), "Таб 'Почта' не отображается"
        assert auth_page.is_element_visible(auth_page.TAB_LOGIN), "Таб 'Логин' не отображается"
        assert auth_page.is_element_visible(auth_page.TAB_ACCOUNT), "Таб 'Лицевой счет' не отображается"

        tabs_selected = any([
            auth_page.is_tab_selected("Номер"),
            auth_page.is_tab_selected("Почта"),
            auth_page.is_tab_selected("Логин"),
            auth_page.is_tab_selected("Лицевой счет")
        ])
        assert tabs_selected, "Ни один таб не выбран"
        print(f"\nФорма авторизации отображается корректно")

    @pytest.mark.negative
    def test_tc002_login_invalid_phone(self, driver, base_url, test_data):
        """TC-002: Авторизация по номеру телефона (некорректный номер)"""
        auth_page = AuthPage(driver)
        auth_page.open(base_url)
        auth_page.click_enter_with_password()
        auth_page.switch_to_phone_tab()

        auth_page.enter_username(test_data["invalid_phone"])
        auth_page.enter_password(test_data["valid_password"])
        auth_page.click_login()

        error_msg = auth_page.get_username_error_message()
        assert "Неверный формат телефона" in error_msg, f"Неверное сообщение об ошибке: {error_msg}"
        print(f"\nПоле 'Телефон' не прошло валидацию. Неверный формат телефона '{test_data['invalid_phone']}'")

    @pytest.mark.negative
    def test_tc003_login_unregistered_phone(self, driver, base_url, test_data):
        """TC-003: Авторизация по номеру телефона (незарегистрированный номер)"""
        auth_page = AuthPage(driver)
        auth_page.open(base_url)
        auth_page.click_enter_with_password()
        auth_page.switch_to_phone_tab()

        auth_page.enter_username(test_data["unregistered_phone"])
        auth_page.enter_password(test_data["valid_password"])
        auth_page.click_login()

        error_msg = auth_page.get_error_message()
        assert "Неверный логин или пароль" in error_msg, f"Неверное сообщение об ошибке: {error_msg}"
        assert auth_page.is_forgot_password_link_orange(), "Ссылка 'Забыл пароль' не оранжевая"
        print(f"\nОшибка авторизации. Указан неверный номер телефона '{test_data['unregistered_phone']}'")

    @pytest.mark.positive
    def test_tc004_login_email_success(self, driver, base_url, test_data):
        """TC-004: Авторизация по почте (успешная)"""
        auth_page = AuthPage(driver)
        auth_page.open(base_url)
        auth_page.click_enter_with_password()
        auth_page.switch_to_email_tab()

        assert auth_page.is_tab_selected("Почта"), "Таб 'Почта' не выбран"

        auth_page.login_with_credentials(
            test_data["valid_email"],
            test_data["valid_password"]
        )

        time.sleep(2)
        assert "redirect_uri" in driver.current_url or driver.current_url != base_url, \
            "Перенаправление не произошло"
        print(f"\nАвторизация прошла успешно")

    @pytest.mark.negative
    def test_tc005_login_email_wrong_password(self, driver, base_url, test_data):
        """TC-005: Авторизация по почте (неверный пароль)"""
        auth_page = AuthPage(driver)
        auth_page.open(base_url)
        auth_page.click_enter_with_password()
        auth_page.switch_to_email_tab()

        auth_page.login_with_credentials(
            test_data["valid_email"],
            test_data["invalid_password"]
        )

        error_msg = auth_page.get_error_message()
        assert "Неверный логин или пароль" in error_msg, f"Неверное сообщение об ошибке: {error_msg}"
        assert auth_page.is_forgot_password_link_orange(), "Ссылка 'Забыл пароль' не оранжевая"
        print(f"\nОшибка авторизации. Указан неверный пароль '{test_data['invalid_password']}'")

    @pytest.mark.negative
    def test_tc006_login_email_empty(self, driver, base_url, test_data):
        """TC-006: Авторизация по почте (поле 'Почта' пустое)"""
        auth_page = AuthPage(driver)
        auth_page.open(base_url)
        auth_page.click_enter_with_password()
        auth_page.switch_to_email_tab()

        auth_page.enter_password(test_data["valid_password"])
        auth_page.click_login()

        error_msg = auth_page.get_username_error_message()
        assert "Введите адрес, указанный при регистрации" in error_msg, \
            f"Неверное сообщение об ошибке: {error_msg}"
        print(f"\nПоле 'Почта' не прошло валидацию. Не указан адрес электронной почты")

    @pytest.mark.positive
    def test_tc007_login_success(self, driver, base_url, test_data):
        """TC-007: Авторизация по логину (успешная)"""
        auth_page = AuthPage(driver)
        auth_page.open(base_url)
        auth_page.click_enter_with_password()
        auth_page.switch_to_login_tab()

        assert auth_page.is_tab_selected("Логин"), "Таб 'Логин' не выбран"

        auth_page.login_with_credentials(
            test_data["valid_login"],
            test_data["valid_password"]
        )

        time.sleep(2)
        assert "redirect_uri" in driver.current_url or driver.current_url != base_url, \
            "Перенаправление не произошло"
        print(f"\nАвторизация прошла успешно")

    @pytest.mark.negative
    def test_tc008_login_wrong_login(self, driver, base_url, test_data):
        """TC-008: Авторизация по логину (неверный логин)"""
        auth_page = AuthPage(driver)
        auth_page.open(base_url)
        auth_page.click_enter_with_password()
        auth_page.switch_to_login_tab()

        auth_page.login_with_credentials(
            test_data["nonexistent_login"],
            test_data["valid_password"]
        )

        error_msg = auth_page.get_error_message()
        assert "Неверный логин или пароль" in error_msg, f"Неверное сообщение об ошибке: {error_msg}"
        assert auth_page.is_forgot_password_link_orange(), "Ссылка 'Забыл пароль' не оранжевая"
        print(f"\nОшибка авторизации. Указан неверный логин '{test_data['nonexistent_login']}'")

    @pytest.mark.negative
    def test_tc009_login_wrong_account(self, driver, base_url, test_data):
        """TC-009: Авторизация по ЛС (некорректный лицевой счет)"""
        auth_page = AuthPage(driver)
        auth_page.open(base_url)
        auth_page.click_enter_with_password()
        auth_page.switch_to_account_tab()

        auth_page.login_with_credentials(
            test_data["nonexistent_ls"],
            test_data["valid_password"]
        )

        error_msg = auth_page.get_error_message()
        assert "Неверный логин или пароль" in error_msg, f"Неверное сообщение об ошибке: {error_msg}"
        assert auth_page.is_forgot_password_link_orange(), "Ссылка 'Забыл пароль' не оранжевая"
        print(f"\nОшибка авторизации. Указан неверный лицевой счет '{test_data['nonexistent_ls']}'")

    @pytest.mark.positive
    def test_tc010_input_with_spaces(self, driver, base_url, test_data):
        """TC-010: Проверка ввода с пробелами"""
        auth_page = AuthPage(driver)
        auth_page.open(base_url)
        auth_page.click_enter_with_password()
        auth_page.switch_to_email_tab()

        email_with_spaces = f" {test_data['valid_email']} "
        auth_page.enter_username(email_with_spaces)
        auth_page.enter_password(test_data["valid_password"])

        username_input = auth_page.get_element(auth_page.USERNAME_INPUT)
        value = username_input.get_attribute("value")
        assert " " not in value, f"Пробелы не обрезаны: {value}"
        auth_page.click_login()
        print(f"\nАвторизация прошла успешно")

    @pytest.mark.positive
    def test_tc011_password_toggle(self, driver, base_url):
        """TC-011: Проверка отображения/скрытия пароля"""
        auth_page = AuthPage(driver)
        auth_page.open(base_url)
        auth_page.click_enter_with_password()

        auth_page.enter_password("TestPassword123!")
        assert not auth_page.is_password_visible(), "Пароль виден до нажатия на глаз"

        auth_page.toggle_password()
        assert auth_page.is_password_visible(), "Пароль не отображается после нажатия на глаз"

        auth_page.toggle_password()
        assert not auth_page.is_password_visible(), "Пароль не скрывается после повторного нажатия"
        print(f"\nКнопка отображения пароля работает корректно")

    """2. Авторизация по временному коду"""

    @pytest.mark.positive
    def test_tc012_check_code_input_field(self, driver, base_url, test_data):
        """TC-012: Проверка поля ввода номера телефона или почты"""
        auth_page = AuthPage(driver)
        auth_page.open(base_url)
        auth_page.enter_code_username(test_data["valid_email"])

        code_input = auth_page.get_element(auth_page.USERNAME_CODE_INPUT)
        entered_value = code_input.get_attribute("value")

        assert entered_value == test_data["valid_email"], \
            f"Email введен неверно. Ожидалось: '{test_data['valid_email']}', Получено: '{entered_value}'"
        print(f"\nEmail введен верно '{test_data['valid_email']}'")

    @pytest.mark.positive
    def test_tc013_send_code_to_email(self, driver, base_url, test_data):
        """TC-013: Отправка кода на почту"""
        auth_page = AuthPage(driver)
        auth_page.open(base_url)

        auth_page.enter_code_username(test_data["valid_email"])
        auth_page.get_code()

        assert auth_page.is_element_visible(auth_page.CODE_INPUTS), \
            "Форма ввода кода не отображается"
        print(f"\nФорма ввода кода отображается корректно")

    @pytest.mark.positive
    def test_tc014_change_email(self, driver, base_url, test_data):
        """TC-014: Изменение почты"""
        auth_page = AuthPage(driver)
        auth_page.open(base_url)

        time.sleep(120)  #Для успешного последовательного прохождения тестов
        auth_page.enter_code_username(test_data["valid_email"])
        auth_page.get_code()
        auth_page.change_email()

        assert auth_page.is_element_visible(auth_page.USERNAME_CODE_INPUT), \
            "Форма ввода email не отображается после нажатия 'Изменить почту'"
        print(f"\nВозврат на форму ввода email выполнен успешно")