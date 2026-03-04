"""
Константы Allure Tag для мобильного фреймворка.

Теги — свободные метки для фильтрации тестов в Allure-отчёте.
Могут комбинироваться: тест может иметь REGRESSION + HOME + SMOKE одновременно.

Используются через @allure.tag(AllureTag.REGRESSION, AllureTag.HOME).
"""

from enum import Enum


class AllureTag(str, Enum):
    """Теги для фильтрации тестов в Allure-отчёте."""

    # Типы прогонов
    SMOKE = "SMOKE"
    REGRESSION = "REGRESSION"

    # Экраны
    HOME = "HOME"
    TALKS = "TALKS"
    CONTACTS = "CONTACTS"
    MEMES = "MEMES"
    CHAT = "CHAT"
    NAVIGATION = "NAVIGATION"
