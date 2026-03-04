"""
Константы Allure Story для мобильного фреймворка.

Story — нижний уровень группировки тестов.
Описывает конкретные пользовательские сценарии.

Иерархия: Epic → Feature → Story
Пример: TALKS_APP → HOME → CHECK_ELEMENTS
"""

from enum import Enum


class AllureStory(str, Enum):
    """User stories для Allure-отчёта — конкретные сценарии."""

    # Общие действия
    CHECK_ELEMENTS = "Check elements visibility"
    CHECK_TEXT = "Check text content"
    TAP_ELEMENT = "Tap element"
    SCROLL = "Scroll content"

    # Навигация
    BOTTOM_BAR = "Bottom navigation bar"
    NAVIGATE_BACK = "Navigate back"

    # Доклады
    OPEN_TALK = "Open talk detail"
    SEARCH_TALKS = "Search talks"
    FILTER_TALKS = "Filter talks"

    # Контакты
    OPEN_CONTACT = "Open contact"
    SOLVE_CAPTCHA = "Solve captcha"
