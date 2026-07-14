import pytest
from pages.registration_page import RegistrationPage
import time


class TestRegistration:
    """4. Регистрация"""
    @pytest.mark.positive
    def test_tc024_go_to_registration_form(self, driver, base_url):
        """TC-024: Переход на форму регистрации"""
        registration_page = RegistrationPage(driver)
        registration_page.open(base_url)

        current_url = driver.current_url.lower()
        assert "registration" in current_url or "register" in current_url, \
            f"Переход на форму регистрации не произошел. Текущий URL: {driver.current_url}"
        print(f"\nПереход на форму регистрации выполнен успешно")

    @pytest.mark.smoke
    def test_tc025_registration_form(self, driver, base_url):
        """TC-025: Отображение формы регистрации"""
        registration_page = RegistrationPage(driver)
        registration_page.open(base_url)

        assert registration_page.is_element_visible(registration_page.FIRST_NAME_INPUT), \
            "Поле ввода имени не отображается"
        assert registration_page.is_element_visible(registration_page.LAST_NAME_INPUT), \
            "Поле ввода фамилии не отображается"
        assert registration_page.is_element_visible(registration_page.REGION_SELECT), \
            "Поле выбора региона не отображается"
        assert registration_page.is_element_visible(registration_page.EMAIL_INPUT), \
            "Поле ввода email не отображается"
        assert registration_page.is_element_visible(registration_page.PASSWORD_INPUT), \
            "Поле ввода пароля не отображается"
        assert registration_page.is_element_visible(registration_page.CONFIRM_PASSWORD_INPUT), \
            "Поле подтверждения пароля не отображается"
        assert registration_page.is_element_visible(registration_page.REGISTER_BTN), \
            "Кнопка 'Зарегистрироваться' не отображается"
        assert registration_page.is_element_visible(registration_page.PDN_LINK), \
            "Ссылка на политику обработки персональных данных не отображается"
        assert registration_page.is_element_visible(registration_page.USER_AGREEMENT_LINK), \
            "Ссылка на пользовательское соглашение не отображается"
        print(f"\nФорма регистрации отображается корректно")

    @pytest.mark.negative
    def test_tc026_name_min_length(self, driver, base_url):
        """TC-026: Валидация имени (минимальная длина)"""
        registration_page = RegistrationPage(driver)
        registration_page.open(base_url)

        min_name = "А"
        registration_page.enter_first_name(min_name)
        registration_page.click_register()

        error_msg = registration_page.get_name_error()
        assert "Необходимо заполнить поле кириллицей. От 2 до 30 символов." in error_msg, \
            f"Неверное сообщение об ошибке: {error_msg}"
        print(f"\nПоле 'Имя' не прошло валидацию. Имя {min_name} содержит менее 2 символов")

    @pytest.mark.negative
    def test_tc027_validation_name_special_characters(self, driver, base_url):
        """TC-027: Валидация имени (спецсимволы)"""
        registration_page = RegistrationPage(driver)
        registration_page.open(base_url)

        name_special_symbols = "!@#$%"
        registration_page.enter_first_name(name_special_symbols)
        registration_page.click_register()

        error_msg = registration_page.get_name_error()
        assert "Необходимо заполнить поле кириллицей. От 2 до 30 символов." in error_msg, \
            f"Неверное сообщение об ошибке: {error_msg}"
        print(f"\nПоле 'Имя' не прошло валидацию. Имя {name_special_symbols} содержит спецсимволы")

    @pytest.mark.negative
    def test_tc028_validation_name_max_length(self, driver, base_url):
        """TC-028: Валидация имени (максимальная длина)"""
        registration_page = RegistrationPage(driver)
        registration_page.open(base_url)

        long_name = "А" * 31
        registration_page.enter_first_name(long_name)
        registration_page.click_register()

        error_msg = registration_page.get_name_error()
        assert "Необходимо заполнить поле кириллицей. От 2 до 30 символов." in error_msg, \
            f"Неверное сообщение об ошибке: {error_msg}"
        print(f"\nПоле 'Имя' не прошло валидацию. Имя {long_name} содержит больше 30 символов")

    @pytest.mark.positive
    def test_tc029_validation_name_correct(self, driver, base_url):
        """TC-029: Валидация имени (корректное имя)"""
        registration_page = RegistrationPage(driver)
        registration_page.open(base_url)

        correct_name = "Александр"
        registration_page.enter_first_name(correct_name)

        registration_page.click_register()

        name_input = registration_page.get_element(registration_page.FIRST_NAME_INPUT)
        entered_value = name_input.get_attribute("value")
        assert entered_value == correct_name, \
            f"Имя введено неверно. Ожидалось: '{correct_name}', Получено: '{entered_value}'"
        print(f"Поле 'Имя' содержит: '{entered_value}'")

        try:
            error_msg = registration_page.get_name_error()
            if error_msg:
                assert "необходимо заполнить поле кириллицей" not in error_msg.lower() and \
                       "от 2 до 30" not in error_msg.lower(), \
                    f"Неожиданная ошибка для имени '{correct_name}': {error_msg}"
                print(f"Другая ошибка (не связанная с именем): {error_msg}")
            else:
                print(f"Имя '{correct_name}' прошло валидацию (ошибки нет)")
        except:
            print(f"Имя '{correct_name}' прошло валидацию (ошибки нет)")

    @pytest.mark.negative
    def test_tc030_surname_english(self, driver, base_url):
        """TC-030: Валидация фамилии (английский язык)"""
        registration_page = RegistrationPage(driver)
        registration_page.open(base_url)

        en_surname = "Re"
        registration_page.enter_last_name(en_surname)
        registration_page.click_register()

        error_msg = registration_page.get_name_error()
        assert "Необходимо заполнить поле кириллицей. От 2 до 30 символов." in error_msg, \
            f"Неверное сообщение об ошибке: {error_msg}"
        print(f"\nПоле 'Фамилия' не прошло валидацию. Фамилия {en_surname} не содержит кириллицу")

    @pytest.mark.negative
    def test_tc031_surname_empty(self, driver, base_url):
        """TC-031: Валидация фамилии (пустое поле)"""
        registration_page = RegistrationPage(driver)
        registration_page.open(base_url)

        empty_surname = ""
        registration_page.enter_last_name(empty_surname)
        registration_page.click_register()

        error_msg = registration_page.get_name_error()
        assert "Необходимо заполнить поле кириллицей. От 2 до 30 символов." in error_msg, \
            f"Неверное сообщение об ошибке: {error_msg}"
        print(f"\nПоле 'Фамилия' не прошло валидацию. Значение отсутствует")

    @pytest.mark.negative
    def test_tc032_validation_surname_boundary_values(self, driver, base_url):
        """TC-032: Валидация фамилии (граничные значения)"""
        registration_page = RegistrationPage(driver)
        registration_page.open(base_url)

        test_cases = [
            {"surname": "А", "expect_error": True, "description": "1 символ"},
            {"surname": "Ан", "expect_error": False, "description": "2 символа"},
            {"surname": "А" * 30, "expect_error": False, "description": "30 символов"},
            {"surname": "А" * 31, "expect_error": True, "description": "31 символ"},
        ]

        results = []
        passed = 0
        failed = 0

        for tc in test_cases:
            print(f"\n{'=' * 60}")
            print(f"Проверка: {tc['description']}")
            print(f"Фамилия: '{tc['surname']}' (длина: {len(tc['surname'])} символов)")
            print(f"Ожидаемый результат: {'ОШИБКА' if tc['expect_error'] else 'УСПЕХ'}")

        last_name_input = registration_page.get_element(registration_page.LAST_NAME_INPUT)
        last_name_input.clear()

        registration_page.enter_last_name(tc['surname'])
        registration_page.click_register()

        try:
            error_msg = registration_page.get_name_error()

            if tc['expect_error']:
                assert error_msg is not None and len(error_msg) > 0, \
                    f"Ошибка не отображается для '{tc['surname']}'"

                expected_texts = [
                    "необходимо заполнить поле кириллицей",
                    "от 2 до 30",
                    "2 до 30 символов"
                ]

                is_correct_error = any(text in error_msg.lower() for text in expected_texts)
                assert is_correct_error, \
                    f"Неверное сообщение об ошибке. Получено: '{error_msg}'"

                print(f"Ошибка отображается корректно")
                print(f"   Сообщение: {error_msg}")
                results.append({"description": tc['description'], "status": "PASS"})
                passed += 1

            else:
                if error_msg:
                    assert "необходимо заполнить поле кириллицей" not in error_msg.lower(), \
                        f"Неожиданная ошибка: {error_msg}"
                    print(f"Другая ошибка (не про фамилию): {error_msg}")
                    results.append({"description": tc['description'], "status": "PASS"})
                    passed += 1
                else:
                    print(f"Фамилия прошла валидацию")
                    results.append({"description": tc['description'], "status": "PASS"})
                    passed += 1

        except AssertionError as e:
            print(f"{str(e)}")
            results.append({"description": tc['description'], "status": "FAIL"})
            failed += 1

            assert passed == len(test_cases), \
                f"\n TC-032: НЕ ВСЕ ТЕСТЫ ПРОШЛИ УСПЕШНО!\n" \
                f"   Пройдено: {passed}/{len(test_cases)}\n" \
                f"   Провалено: {failed}/{len(test_cases)}"

    @pytest.mark.negative
    def test_tc033_validation_invalid_email(self, driver, base_url):
        """TC-033: Валидация почты (некорректные данные)"""
        registration_page = RegistrationPage(driver)
        registration_page.open(base_url)

        wrong_email = "аааааааааа"
        registration_page.enter_email(wrong_email)
        registration_page.click_register()

        error_msg = registration_page.get_email_error()
        assert "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru" in error_msg, \
            f"Неверное сообщение об ошибке: {error_msg}"
        print(f"\nПоле 'Почта' не прошло валидацию. Email: '{wrong_email}' не соответствует формату example@email.ru")

    @pytest.mark.positive
    def test_tc034_back_to_auth_form(self, driver, base_url):
        """TC-034: Возврат к форме авторизации"""
        registration_page = RegistrationPage(driver)
        registration_page.open(base_url)

        registration_page.click_register_back()
        time.sleep(5)
        current_url = driver.current_url.lower()
        assert "registration" not in current_url and "register" not in current_url, \
            f"Переход на форму авторизации не произошел. Текущий URL: {driver.current_url}"
        print(f"\nПереход на форму авторизации прошел успешно")