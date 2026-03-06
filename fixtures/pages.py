"""
Фикстуры Page Object'ов.

Каждая фикстура принимает appium_driver и возвращает
экземпляр конкретного Page Object.

Паттерн аналогичен fixtures/pages.py из autotests-ui:
    - Фикстуры зарегистрированы через pytest_plugins в conftest.py
    - Pytest внедряет их по имени параметра теста
    - Scope: function (новый Page Object на каждый тест)

Пример использования в тесте:
    def test_home_visible(self, home_page: HomePage):
        home_page.screen.check_visible()
"""

import pytest
from appium.webdriver import Remote as AppiumDriver

from pages.home.home_page import HomePage
from pages.talks.talks_list_page import TalksListPage
from pages.talks.talk_detail_page import TalkDetailPage
from pages.contacts.contacts_page import ContactsPage
from components.navigation.bottom_nav import BottomNavigation


@pytest.fixture
def home_page(appium_driver: AppiumDriver) -> HomePage:
    """Фикстура: Page Object главного экрана."""
    return HomePage(driver=appium_driver)


@pytest.fixture
def talks_list_page(appium_driver: AppiumDriver) -> TalksListPage:
    """Фикстура: Page Object списка докладов."""
    return TalksListPage(driver=appium_driver)


@pytest.fixture
def talk_detail_page(appium_driver: AppiumDriver) -> TalkDetailPage:
    """Фикстура: Page Object деталей доклада."""
    return TalkDetailPage(driver=appium_driver)


@pytest.fixture
def contacts_page(appium_driver: AppiumDriver) -> ContactsPage:
    """Фикстура: Page Object контактов."""
    return ContactsPage(driver=appium_driver)


@pytest.fixture
def bottom_nav(appium_driver: AppiumDriver) -> BottomNavigation:
    """Фикстура: компонент нижней навигации."""
    return BottomNavigation(driver=appium_driver)
