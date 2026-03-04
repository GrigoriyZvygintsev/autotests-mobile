"""
Константы Allure Epic для мобильного фреймворка.

Epic — верхний уровень группировки тестов в Allure-отчёте.
Обычно соответствует крупным модулям или приложениям.

Иерархия: Epic → Feature → Story
Пример: TALKS_APP → NAVIGATION → BOTTOM_BAR
"""

from enum import Enum


class AllureEpic(str, Enum):
    """Эпики для Allure-отчёта."""

    TALKS_APP = "TalksApp"
