"""
Page Object: Экран контактов (Contacts Screen) TalksApp.

Содержит кнопки контактов (Telegram, LinkedIn, GitHub, Email)
и CAPTCHA-диалог для защиты от спама.

CAPTCHA — математическая задача (сложение/вычитание),
которую нужно решить для получения ссылки.
"""

from appium.webdriver import Remote as AppiumDriver
from appium.webdriver.common.appiumby import AppiumBy

from elements.button import Button
from elements.input import Input
from elements.text import Text
from pages.base_page import BasePage


class ContactsPage(BasePage):
    """
    Page Object экрана контактов.

    Навигация: bottom navigation → "Контакт" (nav_contacts).
    """

    def __init__(self, driver: AppiumDriver):
        super().__init__(driver)

        # === Экран ===
        self.screen = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "screen_contacts"),
            name="Экран 'Контакты'",
        )

        # === Заголовок ===
        self.title = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "text_contacts_title"),
            name="Заголовок 'Контакты'",
        )

        # === Кнопки контактов ===
        self.telegram_button = Button(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "btn_contact_telegram"),
            name="Кнопка 'Telegram'",
        )
        self.linkedin_button = Button(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "btn_contact_linkedin"),
            name="Кнопка 'LinkedIn'",
        )
        self.github_button = Button(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "btn_contact_github"),
            name="Кнопка 'GitHub'",
        )
        self.email_button = Button(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "btn_contact_email"),
            name="Кнопка 'Email'",
        )

        # === CAPTCHA-диалог ===
        self.captcha_title = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "text_captcha_title"),
            name="Заголовок CAPTCHA",
        )
        self.captcha_question = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "text_captcha_question"),
            name="Вопрос CAPTCHA",
        )
        self.captcha_input = Input(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "input_captcha_answer"),
            name="Поле ответа CAPTCHA",
        )
        self.captcha_submit = Button(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "btn_captcha_submit"),
            name="Кнопка 'Подтвердить' CAPTCHA",
        )
        self.captcha_refresh = Button(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "btn_captcha_refresh"),
            name="Кнопка 'Обновить' CAPTCHA",
        )
        self.captcha_error = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "text_captcha_error"),
            name="Ошибка CAPTCHA",
        )
