"""
Базовые assertion-функции с логированием и allure-шагами.

Каждый assert оборачивается в @allure.step и логирует результат.
Это обеспечивает:
- Читаемые шаги в Allure-отчёте
- Трейс в консоли для отладки
- Единообразные сообщения об ошибках

Паттерн аналогичен autotests-api/tools/assertions/base.py.
"""

from typing import Any

import allure

from tools.logger import get_logger

logger = get_logger("ASSERTIONS")


@allure.step('Проверка что "{name}" равно "{expected}"')
def assert_equal(actual: Any, expected: Any, name: str) -> None:
    """
    Проверяет, что фактическое значение равно ожидаемому.

    Args:
        actual: Фактическое значение.
        expected: Ожидаемое значение.
        name: Название проверяемого значения (для логов).

    Raises:
        AssertionError: Если значения не совпадают.
    """
    logger.info(f'Проверка что "{name}" равно "{expected}"')
    assert actual == expected, (
        f'Некорректное значение: "{name}". '
        f'Ожидали: {expected}. '
        f'Получили: {actual}'
    )


@allure.step('Проверка что "{name}" содержит "{substring}"')
def assert_contains(actual: str, substring: str, name: str) -> None:
    """
    Проверяет, что строка содержит подстроку.

    Args:
        actual: Фактическая строка.
        substring: Ожидаемая подстрока.
        name: Название проверяемого значения.

    Raises:
        AssertionError: Если подстрока не найдена.
    """
    logger.info(f'Проверка что "{name}" содержит "{substring}"')
    assert substring in actual, (
        f'Подстрока не найдена в "{name}". '
        f'Ожидали подстроку: "{substring}". '
        f'Фактическое значение: "{actual}"'
    )


@allure.step('Проверка что "{name}" истинно')
def assert_is_true(actual: Any, name: str) -> None:
    """
    Проверяет, что значение истинно (truthy).

    Args:
        actual: Проверяемое значение.
        name: Название проверяемого значения.

    Raises:
        AssertionError: Если значение ложно.
    """
    logger.info(f'Проверка что "{name}" истинно')
    assert actual, (
        f'Ожидали истинное значение для "{name}", '
        f'получили: {actual}'
    )


@allure.step('Проверка что "{name}" ложно')
def assert_is_false(actual: Any, name: str) -> None:
    """
    Проверяет, что значение ложно (falsy).

    Args:
        actual: Проверяемое значение.
        name: Название проверяемого значения.

    Raises:
        AssertionError: Если значение истинно.
    """
    logger.info(f'Проверка что "{name}" ложно')
    assert not actual, (
        f'Ожидали ложное значение для "{name}", '
        f'получили: {actual}'
    )
