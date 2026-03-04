"""
Тесты экрана контактов (Contacts Screen) TalksApp.

Проверяют:
- Отображение кнопок контактов (Telegram, LinkedIn, GitHub, Email)
- Открытие CAPTCHA-диалога при нажатии на контакт
- Видимость элементов CAPTCHA

Запуск:
    pytest tests/contacts/ -m regression --alluredir=allure-results
"""

import allure
import pytest
from allure_commons.types import Severity

from components.navigation.bottom_nav import BottomNavigation
from pages.home.home_page import HomePage
from pages.contacts.contacts_page import ContactsPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag


@allure.epic(AllureEpic.TALKS_APP)
@allure.feature(AllureFeature.CONTACTS)
@allure.tag(AllureTag.REGRESSION, AllureTag.CONTACTS)
@pytest.mark.regression
@pytest.mark.contacts
class TestContactsScreen:
    """Тесты экрана контактов."""

    @allure.story(AllureStory.CHECK_ELEMENTS)
    @allure.severity(Severity.CRITICAL)
    @allure.title("Экран контактов загружается")
    def test_contacts_screen_visible(
        self,
        home_page: HomePage,
        contacts_page: ContactsPage,
    ):
        """Проверяем, что экран контактов отображается."""
        bottom_nav = BottomNavigation(home_page.driver)
        bottom_nav.go_to_contacts()

        contacts_page.screen.check_visible()
        contacts_page.title.check_visible()

    @allure.story(AllureStory.CHECK_ELEMENTS)
    @allure.severity(Severity.CRITICAL)
    @allure.title("Кнопки контактов видимы")
    def test_contact_buttons_visible(
        self,
        home_page: HomePage,
        contacts_page: ContactsPage,
    ):
        """
        Проверяем, что все 4 кнопки контактов отображаются:
        Telegram, LinkedIn, GitHub, Email.
        """
        bottom_nav = BottomNavigation(home_page.driver)
        bottom_nav.go_to_contacts()

        contacts_page.telegram_button.check_visible()
        contacts_page.linkedin_button.check_visible()
        contacts_page.github_button.check_visible()
        contacts_page.email_button.check_visible()

    @allure.story(AllureStory.OPEN_CONTACT)
    @allure.severity(Severity.NORMAL)
    @allure.title("CAPTCHA открывается при нажатии на Telegram")
    def test_captcha_opens_on_telegram_click(
        self,
        home_page: HomePage,
        contacts_page: ContactsPage,
    ):
        """
        Проверяем, что при нажатии на кнопку Telegram
        открывается CAPTCHA-диалог с математической задачей.

        CAPTCHA защищает контакты от спам-ботов.
        """
        bottom_nav = BottomNavigation(home_page.driver)
        bottom_nav.go_to_contacts()

        # Тапаем на кнопку Telegram
        contacts_page.telegram_button.click()

        # Проверяем, что CAPTCHA-диалог открылся
        contacts_page.captcha_title.check_visible()
        contacts_page.captcha_question.check_visible()
        contacts_page.captcha_input.check_visible()
        contacts_page.captcha_submit.check_visible()
