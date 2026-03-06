"""
Page Object: Экран контактов (Contacts Screen) TalksApp.

Содержит кнопки контактов (Telegram, LinkedIn, GitHub, Email)
и CAPTCHA-диалог для защиты от спама.

TestTags из TalksApp:
    screen_contacts, text_contacts_title,
    btn_contact_telegram, btn_contact_linkedin, btn_contact_github, btn_contact_email

CAPTCHA-диалог в текущей версии рендерится без testTag/resource-id,
поэтому для него используем text-локаторы через UiSelector.
"""

from appium.webdriver import Remote as AppiumDriver
from appium.webdriver.common.appiumby import AppiumBy

from elements.button import Button
from elements.input import Input
from elements.text import Text
from pages.base_page import BasePage


class ContactsPage(BasePage):
    """Page Object экрана контактов."""

    def __init__(self, driver: AppiumDriver):
        super().__init__(driver)

        # === Экран ===
        self.screen = Text(
            driver=driver,
            locator=(AppiumBy.ID, "screen_contacts"),
            name="Экран 'Контакты'",
        )

        # === Заголовок ===
        self.title = Text(
            driver=driver,
            locator=(AppiumBy.ID, "text_contacts_title"),
            name="Заголовок 'Контакты'",
        )

        # === Кнопки контактов ===
        self.telegram_button = Button(
            driver=driver,
            locator=(AppiumBy.ID, "btn_contact_telegram"),
            name="Кнопка 'Telegram'",
        )
        self.linkedin_button = Button(
            driver=driver,
            locator=(AppiumBy.ID, "btn_contact_linkedin"),
            name="Кнопка 'LinkedIn'",
        )
        self.github_button = Button(
            driver=driver,
            locator=(AppiumBy.ID, "btn_contact_github"),
            name="Кнопка 'GitHub'",
        )
        self.email_button = Button(
            driver=driver,
            locator=(AppiumBy.ID, "btn_contact_email"),
            name="Кнопка 'Email'",
        )

        # === CAPTCHA-диалог ===
        self.captcha_dialog = Text(
            driver=driver,
            locator=(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().text("Проверка контакта")',
            ),
            name="Диалог CAPTCHA",
        )
        self.captcha_title = Text(
            driver=driver,
            locator=(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().text("Проверка контакта")',
            ),
            name="Заголовок CAPTCHA",
        )
        self.captcha_question = Text(
            driver=driver,
            locator=(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().textContains("Решите пример")',
            ),
            name="Вопрос CAPTCHA",
        )
        self.captcha_input = Input(
            driver=driver,
            locator=(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().text("Ваш ответ")',
            ),
            name="Поле ответа CAPTCHA",
        )
        self.captcha_submit = Button(
            driver=driver,
            locator=(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().textContains("Показать")',
            ),
            name="Кнопка 'Подтвердить' CAPTCHA",
        )
        self.captcha_refresh = Button(
            driver=driver,
            locator=(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().text("Другой пример")',
            ),
            name="Кнопка 'Обновить' CAPTCHA",
        )
        self.captcha_error = Text(
            driver=driver,
            locator=(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().textContains("Невер")',
            ),
            name="Ошибка CAPTCHA",
        )
