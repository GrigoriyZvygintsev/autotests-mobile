"""
Page Object: Главная страница (Home Screen) TalksApp.

Содержит элементы главного экрана приложения:
- Карточка героя (hero) со слоганом и кнопками
- Карточка профиля с аватаром
- Секции: "Обо мне", "Стек", "Темы", "Контакты"
- Превью последних докладов

TestTags из TalksApp (Compose Modifier.testTag()):
    screen_home, card_hero, text_hero_role, text_hero_slogan,
    text_hero_subtitle, text_hero_description, btn_hero_talks,
    card_profile, btn_all_talks, text_about_header, text_stack_header,
    text_topics_header, text_latest_talks_header, text_contacts_header
"""

from appium.webdriver import Remote as AppiumDriver
from appium.webdriver.common.appiumby import AppiumBy

from elements.button import Button
from elements.text import Text
from pages.base_page import BasePage


class HomePage(BasePage):
    """Page Object главного экрана TalksApp."""

    def __init__(self, driver: AppiumDriver):
        super().__init__(driver)

        # === Экран ===
        self.screen = Text(
            driver=driver,
            locator=(AppiumBy.ID, "screen_home"),
            name="Экран 'Главная'",
        )

        # === Карточка героя (Hero) ===
        self.hero_role = Text(
            driver=driver,
            locator=(AppiumBy.ID, "text_hero_role"),
            name="Роль в hero-карточке",
        )
        self.hero_slogan = Text(
            driver=driver,
            locator=(AppiumBy.ID, "text_hero_slogan"),
            name="Слоган",
        )
        self.hero_subtitle = Text(
            driver=driver,
            locator=(AppiumBy.ID, "text_hero_subtitle"),
            name="Подзаголовок hero",
        )
        self.hero_description = Text(
            driver=driver,
            locator=(AppiumBy.ID, "text_hero_description"),
            name="Описание в hero",
        )
        self.hero_talks_button = Button(
            driver=driver,
            locator=(AppiumBy.ID, "btn_hero_talks"),
            name="Кнопка 'Все доклады' в hero",
        )

        # === Карточка профиля ===
        self.all_talks_button = Button(
            driver=driver,
            locator=(AppiumBy.ID, "btn_all_talks"),
            name="Кнопка 'Все доклады' в профиле",
        )

        # === Заголовки секций ===
        self.about_header = Text(
            driver=driver,
            locator=(AppiumBy.ID, "text_about_header"),
            name="Заголовок 'Обо мне'",
        )
        self.stack_header = Text(
            driver=driver,
            locator=(AppiumBy.ID, "text_stack_header"),
            name="Заголовок 'Стек'",
        )
        self.topics_header = Text(
            driver=driver,
            locator=(AppiumBy.ID, "text_topics_header"),
            name="Заголовок 'Темы'",
        )
        self.latest_talks_header = Text(
            driver=driver,
            locator=(AppiumBy.ID, "text_latest_talks_header"),
            name="Заголовок 'Последние доклады'",
        )
        self.contacts_header = Text(
            driver=driver,
            locator=(AppiumBy.ID, "text_contacts_header"),
            name="Заголовок 'Контакты'",
        )
