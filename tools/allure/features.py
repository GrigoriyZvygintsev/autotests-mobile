"""
Константы Allure Feature для мобильного фреймворка.

Feature — средний уровень группировки тестов.
Обычно соответствует экранам или функциональным модулям приложения.

Иерархия: Epic → Feature → Story
Пример: TALKS_APP → HOME → CHECK_ELEMENTS
"""

from enum import Enum


class AllureFeature(str, Enum):
    """Фичи для Allure-отчёта — соответствуют экранам TalksApp."""

    HOME = "Home Screen"
    TALKS_LIST = "Talks List Screen"
    TALK_DETAIL = "Talk Detail Screen"
    CONTACTS = "Contacts Screen"
    MEMES = "Memes Screen"
    CHAT = "Chat Screen"
    NAVIGATION = "Navigation"
