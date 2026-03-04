"""
Тесты главного экрана (Home Screen) TalksApp.

Проверяют, что:
- Главный экран загружается и отображается
- Hero-карточка содержит правильный слоган
- Секции "Обо мне", "Стек", "Темы" видимы
- Кнопки навигации работают

Запуск:
    pytest tests/home/ -m regression --alluredir=allure-results
"""

import allure
import pytest
from allure_commons.types import Severity

from pages.home.home_page import HomePage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag


@allure.epic(AllureEpic.TALKS_APP)
@allure.feature(AllureFeature.HOME)
@allure.tag(AllureTag.REGRESSION, AllureTag.HOME)
@pytest.mark.regression
@pytest.mark.home
class TestHomeScreen:
    """Тесты элементов главного экрана."""

    @allure.story(AllureStory.CHECK_ELEMENTS)
    @allure.severity(Severity.BLOCKER)
    @allure.title("Главный экран загружается")
    def test_home_screen_visible(self, home_page: HomePage):
        """
        Проверяем, что главный экран отображается после запуска приложения.

        Это базовый smoke-тест: если главный экран не загрузился —
        всё остальное тоже не будет работать.
        """
        home_page.screen.check_visible()

    @allure.story(AllureStory.CHECK_TEXT)
    @allure.severity(Severity.CRITICAL)
    @allure.title("Слоган отображается на главной")
    def test_hero_slogan_displayed(self, home_page: HomePage):
        """
        Проверяем, что слоган "Превращаю хаос в стабильные релизы"
        отображается в hero-карточке.
        """
        home_page.hero_slogan.check_visible()

    @allure.story(AllureStory.CHECK_ELEMENTS)
    @allure.severity(Severity.NORMAL)
    @allure.title("Роль QA отображается в hero-карточке")
    def test_hero_role_visible(self, home_page: HomePage):
        """Проверяем видимость роли (Automation QA Engineer) в hero."""
        home_page.hero_role.check_visible()

    @allure.story(AllureStory.CHECK_ELEMENTS)
    @allure.severity(Severity.NORMAL)
    @allure.title("Кнопка 'Все доклады' видима в hero")
    def test_hero_talks_button_visible(self, home_page: HomePage):
        """Проверяем, что кнопка перехода к докладам отображается."""
        home_page.hero_talks_button.check_visible()

    @allure.story(AllureStory.CHECK_ELEMENTS)
    @allure.severity(Severity.NORMAL)
    @allure.title("Секции главной страницы видимы после скролла")
    def test_sections_visible_after_scroll(self, home_page: HomePage):
        """
        Проверяем видимость секций "Обо мне", "Стек", "Темы".

        Секции расположены ниже viewport'а — нужен свайп вверх.
        """
        home_page.about_header.check_visible()
        home_page.swipe_up()
        home_page.stack_header.check_visible()
