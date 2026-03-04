"""
Фикстура Allure: генерация environment.properties после завершения тестов.

Session-scoped, autouse=True — выполняется один раз за весь прогон.
Файл environment.properties создаётся ПОСЛЕ всех тестов (в teardown),
чтобы Allure-отчёт содержал информацию об окружении.

Паттерн аналогичен fixtures/allure.py из autotests-api и autotests-ui.
"""

import pytest

from tools.allure.environment import create_allure_environment_file


@pytest.fixture(scope="session", autouse=True)
def save_allure_environment_file():
    """
    Создаёт файл environment.properties после завершения всех тестов.

    autouse=True — фикстура активируется автоматически для каждой сессии.
    scope="session" — выполняется один раз за весь прогон.

    Жизненный цикл:
        1. yield → тесты выполняются
        2. Teardown → создаём environment.properties
    """
    # До начала тестов ничего не делаем
    yield  # Запускаются автотесты...
    # После завершения автотестов создаем файл environment.properties
    create_allure_environment_file()
