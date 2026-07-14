**Проект: Автотесты для ЕЛК Web (Ростелеком ID)**
Автор проекта: Михеева Ирина Олеговна

*Автоматизация тестирования личного кабинета* `https://lk.rt.ru/`
Проект содержит автотесты для проверки ключевых сценариев:
- Стандартная авторизация (по телефону, почте, логину, лицевому счёту)
- Вход по временному коду
- Восстановление пароля
- Регистрация нового пользователя
- Адаптивность

*Структура проекта:*
В директории pages/ (Page Object Model — описание страниц и их элементов):
•	__init__.py –  инициализация пакета pages,
•	base_page.py – базовый класс с общими методами,
•	auth_page.py – страница авторизации,
•	registration_page.py – страница регистрации,
•	recovery_page.py – страница восстановления пароля.
В директории tests/ (Тестовые сценарии — автоматизированные тесты ):
•	__init__.py - инициализация пакета tests,
•	test_authorization.py – авторизация (TC-001...TC-014),
•	test_recovery.py – восстановление пароля (TC-018...TC-020),
•	test_registration.py – регистрация (TC-024...TC-034),
•	test_ui_adaptability.py – адаптивность (TC-036...TC-037).
Корневые файлы:
README.md – документация проекта,
.gitignore – игнорируемые файлы для Git,
conftest.py – фикстуры pytest,
env – переменные окружения,
requirements – список зависимостей.

**Установка и настройка**
Клонирование репозитория
bash
git clone https://github.com/irinakat1992-star/rt_project.git
cd rt_project
Создание и активация виртуального окружения
bash
python -m venv .venv
Для Linux/MacOS:
source .venv/bin/activate
Для Windows:
.venv\Scripts\activate
Установка зависимостей
bash
pip install -r requirements

**Запуск тестов**
*Все тесты (полный прогон)*
bash
pytest -v
*Конкретный файл с тестами и print() в консоли*
bash
pytest -v - s tests/test_authorization.py
pytest -v - s tests/test_registration.py
pytest -v - s tests/test_recovery.py
pytest -v - s tests/test_ui_adaptability.py
*Конкретный тест по имени*
bash
pytest -v tests/test_authorization.py::test_tc004_login_email_success
