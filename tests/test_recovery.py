import pytest
from pages.recovery_page import RecoveryPage

class TestRecovery:

    """3. Восстановление пароля"""
    @pytest.mark.positive
    def test_tc018_forgot_password_link(self, driver, base_url):
        """TC-018: Проверка кнопки 'Забыл пароль'"""
        recovery_page = RecoveryPage(driver)
        recovery_page.open(base_url)

        current_url = driver.current_url.lower()
        assert "reset-credentials" in current_url or "forgot" in current_url or "recovery" in current_url, \
            f"Переход на форму восстановления не произошел. Текущий URL: {driver.current_url}"
        print(f"\nКнопка 'Забыл пароль' работает корректно")

    @pytest.mark.positive
    def test_tc019_check_email_field(self, driver, base_url, test_data):
        """TC-019: Проверка поля 'Почта'"""
        recovery_page = RecoveryPage(driver)
        recovery_page.open(base_url)

        recovery_page.select_recovery_by_email()
        recovery_page.enter_email(test_data["valid_email"])

        code_input = recovery_page.get_element(recovery_page.EMAIL_INPUT)
        entered_value = code_input.get_attribute("value")
        assert entered_value == test_data["valid_email"], \
            f"Email введен неверно. Ожидалось: '{test_data['valid_email']}', Получено: '{entered_value}'"
        print(f"\nВ поле 'Почта' введен email: '{test_data['valid_email']}'")

    @pytest.mark.positive
    def test_tc020_back_to_auth(self, driver, base_url, test_data):
        """TC-020: Возврат к форме авторизации"""
        recovery_page = RecoveryPage(driver)
        recovery_page.open(base_url)

        recovery_page.select_recovery_by_email()
        recovery_page.enter_email(test_data["valid_email"])
        recovery_page.back_to_auth()

        assert recovery_page.is_element_visible(recovery_page.EMAIL_INPUT), \
            "Возврат на форму авторизации не произошел"
        print(f"\nВозврат на форму авторизации выполнен успешно")