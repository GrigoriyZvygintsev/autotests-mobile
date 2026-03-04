"""
Тесты навигации TalksApp.

Проверяют, что bottom navigation bar работает:
- Переход между экранами (Home → Talks → Memes → Chat → Contacts)
- Каждый экран загружается корректно

Запуск:
    pytest tests/navigation/ -m regression --alluredir=allure-results
"""

import allure
import pytest
from allure_commons.types import Severity

from components.navigation.bottom_nav import BottomNavigation
from pages.home.home_page import HomePage
from pages.talks.talks_list_page import TalksListPage
from pages.contacts.contacts_page import ContactsPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag


@allure.epic(AllureEpic.TALKS_APP)
@allure.feature(AllureFeature.NAVIGATION)
@allure.tag(AllureTag.REGRESSION, AllureTag.NAVIGATION)
@pytest.mark.regression
@pytest.mark.navigation
class TestBottomNavigation:
    """Тесты навигации через нижнюю панель."""

    @allure.story(AllureStory.BOTTOM_BAR)
    @allure.severity(Severity.BLOCKER)
    @allure.title("Навигация: Главная → Доклады")
    def test_navigate_home_to_talks(
        self,
        home_page: HomePage,
        talks_list_page: TalksListPage,
    ):
        """
        Проверяем переход с главной на экран докладов.

        1. Убеждаемся, что мы на главной (screen_home видим)
        2. Тапаем на таб "Доклады" в bottom navigation
        3. Проверяем, что экран докладов загрузился (screen_talks_list видим)
        """
        # Проверяем начальное состояние
        home_page.screen.check_visible()

        # Создаём компонент навигации и переходим на Доклады
        bottom_nav = BottomNavigation(home_page.driver)
        bottom_nav.go_to_talks()

        # Проверяем, что экран докладов загрузился
        talks_list_page.screen.check_visible()
        talks_list_page.title.check_visible()

    @allure.story(AllureStory.BOTTOM_BAR)
    @allure.severity(Severity.CRITICAL)
    @allure.title("Навигация: Главная → Контакты")
    def test_navigate_home_to_contacts(
        self,
        home_page: HomePage,
        contacts_page: ContactsPage,
    ):
        """Проверяем переход с главной на экран контактов."""
        home_page.screen.check_visible()

        bottom_nav = BottomNavigation(home_page.driver)
        bottom_nav.go_to_contacts()

        contacts_page.screen.check_visible()
        contacts_page.title.check_visible()

    @allure.story(AllureStory.BOTTOM_BAR)
    @allure.severity(Severity.CRITICAL)
    @allure.title("Навигация: Доклады → Главная (возврат)")
    def test_navigate_talks_back_to_home(
        self,
        home_page: HomePage,
        talks_list_page: TalksListPage,
    ):
        """
        Проверяем, что можно вернуться на главную после перехода на доклады.

        1. Переходим на Доклады
        2. Возвращаемся на Главную
        3. Проверяем, что главный экран снова видим
        """
        bottom_nav = BottomNavigation(home_page.driver)

        # Переходим на Доклады
        bottom_nav.go_to_talks()
        talks_list_page.screen.check_visible()

        # Возвращаемся на Главную
        bottom_nav.go_to_home()
        home_page.screen.check_visible()
