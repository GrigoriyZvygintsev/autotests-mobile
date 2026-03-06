"""
Тесты экрана списка докладов (Talks List Screen) TalksApp.

Проверяют:
- Отображение списка докладов
- Поиск по названию
- Видимость карточек с правильными данными

Запуск:
    pytest tests/talks/ -m regression --alluredir=allure-results
"""

import allure
import pytest
from allure_commons.types import Severity

from components.navigation.bottom_nav import BottomNavigation
from pages.home.home_page import HomePage
from pages.talks.talks_list_page import TalksListPage
from pages.talks.talk_detail_page import TalkDetailPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag


@allure.epic(AllureEpic.TALKS_APP)
@allure.feature(AllureFeature.TALKS_LIST)
@allure.tag(AllureTag.REGRESSION, AllureTag.TALKS)
@pytest.mark.regression
@pytest.mark.talks
class TestTalksList:
    """Тесты списка докладов."""

    @allure.story(AllureStory.CHECK_ELEMENTS)
    @allure.severity(Severity.CRITICAL)
    @allure.title("Список докладов отображается")
    def test_talks_list_visible(
        self,
        home_page: HomePage,
        talks_list_page: TalksListPage,
    ):
        """
        Проверяем, что список докладов загружается и отображает карточки.

        1. Переходим на экран докладов через bottom nav
        2. Проверяем видимость заголовка и списка
        """
        bottom_nav = BottomNavigation(home_page.driver)
        bottom_nav.go_to_talks()

        talks_list_page.screen.check_visible()
        talks_list_page.title.check_visible()
        talks_list_page.talks_list.check_visible()

    @allure.story(AllureStory.CHECK_ELEMENTS)
    @allure.severity(Severity.NORMAL)
    @allure.title("Поле поиска докладов видимо")
    def test_search_input_visible(
        self,
        home_page: HomePage,
        talks_list_page: TalksListPage,
    ):
        """Проверяем, что поле поиска отображается на экране докладов."""
        bottom_nav = BottomNavigation(home_page.driver)
        bottom_nav.go_to_talks()

        talks_list_page.search_input.check_visible()

    @allure.story(AllureStory.SEARCH_TALKS)
    @allure.severity(Severity.CRITICAL)
    @allure.title("Поиск доклада по названию")
    def test_search_talk_by_name(
        self,
        home_page: HomePage,
        talks_list_page: TalksListPage,
    ):
        """
        Проверяем, что поиск фильтрует список докладов.

        1. Переходим на экран докладов
        2. Вводим "Python" в поле поиска
        3. Проверяем, что карточка доклада про Python видна
        """
        bottom_nav = BottomNavigation(home_page.driver)
        bottom_nav.go_to_talks()

        talks_list_page.search_input.fill("Python")
        # Карточка с slug "python-basics" должна быть видна
        talks_list_page.talk_card.check_visible(slug="python-basics")

    @allure.story(AllureStory.OPEN_TALK)
    @allure.severity(Severity.CRITICAL)
    @allure.title("Открытие деталей доклада из списка")
    def test_open_talk_detail(
        self,
        home_page: HomePage,
        talks_list_page: TalksListPage,
        talk_detail_page: TalkDetailPage,
    ):
        """
        Проверяем переход к деталям доклада.

        1. Переходим на экран докладов
        2. Тапаем на карточку доклада
        3. Проверяем, что открылся экран деталей с заголовком
        """
        bottom_nav = BottomNavigation(home_page.driver)
        bottom_nav.go_to_talks()

        # Тапаем на карточку доклада, которая гарантированно видна на старте списка
        talks_list_page.talk_card.click(slug="algorithms-grokking")

        # Проверяем, что экран деталей загрузился
        talk_detail_page.screen.check_visible()
        talk_detail_page.title.check_visible()
        talk_detail_page.summary.check_visible()

    @allure.story(AllureStory.NAVIGATE_BACK)
    @allure.severity(Severity.NORMAL)
    @allure.title("Возврат из деталей доклада в список")
    def test_back_from_detail_to_list(
        self,
        home_page: HomePage,
        talks_list_page: TalksListPage,
        talk_detail_page: TalkDetailPage,
    ):
        """
        Проверяем кнопку "Назад" на экране деталей доклада.

        1. Открываем детали доклада
        2. Нажимаем "Назад"
        3. Проверяем, что вернулись к списку докладов
        """
        bottom_nav = BottomNavigation(home_page.driver)
        bottom_nav.go_to_talks()

        # Открываем детали
        talks_list_page.talk_card.click(slug="algorithms-grokking")
        talk_detail_page.screen.check_visible()

        # Возвращаемся назад
        talk_detail_page.back_button.click()
        talks_list_page.screen.check_visible()
