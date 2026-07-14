**Проект: Автотесты для ЕЛК Web (Ростелеком ID)**
Автор проекта: Михеева Ирина Олеговна

*Автоматизация тестирования личного кабинета* `https://lk.rt.ru/`
Проект содержит автотесты для проверки ключевых сценариев:
- Стандартная авторизация (по телефону, почте, логину, лицевому счёту)
- Вход по временному коду
- Восстановление пароля
- Регистрация нового пользователя
- Адаптивность

**Структура проекта:**
├── pages/                            # Page Object Model (POM)
│   ├── __init__.py
│   ├── base_page.py                  # Базовый класс с общими методами
│   ├── auth_page.py                  # Страница авторизации
│   ├── registration_page.py          # Страница регистрации
│   └── recovery_page.py              # Страница восстановления пароля
│
├── tests/                            # Тестовые сценарии
│   ├── __init__.py
│   ├── test_authorization.py         # TC-001...TC-014 (авторизация)
│   ├── test_recovery.py              # TC-018...TC-020 (восстановление пароля)
│   ├── test_registration.py          # TC-024...TC-034 (регистрация)
│   └── test_ui_adaptability.py       # TC-036...TC-037 (адаптивность)
│
├── .gitignore                        # Игнорируемые файлы для Git
├── README.md                         # Документация проекта (этот файл)
├── conftest.py                       # Фикстуры pytest
├── env                               # Переменные окружения
└── requirements                      # Список зависимостей

**Установка и настройка**
1.	Клонирование репозитория
bash
git clone https://github.com/irinakat1992-star/rt_project.git
cd rt_project
2.	Создание и активация виртуального окружения
bash
python -m venv .venv
Для Linux/MacOS:
source .venv/bin/activate
Для Windows:
.venv\Scripts\activate
3.	Установка зависимостей
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
pytest -v tests/test_authorization.py::test_tc004_successful_email_login
*Показать все print() в консоли*
bash
pytest -v -s
