"""
Page Object: Главная страница (Home Screen) TalksApp.

Содержит элементы главного экрана приложения:
- Карточка героя (hero) со слоганом и кнопками
- Карточка профиля с аватаром
- Секции: "Обо мне", "Стек", "Темы", "Контакты"
- Превью последних докладов

Все testTag'и берутся из TalksApp/ui/TestTags.kt.
Они маппятся на Accessibility ID в Appium.
"""

from appium.webdriver import Remote as AppiumDriver
from appium.webdriver.common.appiumby import AppiumBy

from elements.button import Button
from elements.text import Text
from pages.base_page import BasePage


class HomePage(BasePage):
    """
    Page Object главного экрана TalksApp.

    Экран содержит bento-сетку карточек с информацией о пользователе,
    его стеке, темах докладов и контактах.

    TestTag'и из TalksApp (Compose Modifier.testTag()):
        - screen_home — корневой контейнер экрана
        - text_hero_slogan — слоган "Превращаю хаос в стабильные релизы"
        - btn_hero_talks — кнопка перехода к докладам
        - и т.д. (см. TalksApp/ui/TestTags.kt)
    """

    def __init__(self, driver: AppiumDriver):
        super().__init__(driver)

        # === Экран ===
        # Корневой контейнер — проверяем, что экран загрузился
        self.screen = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "screen_home"),
            name="Экран 'Главная'",
        )

        # === Карточка героя (Hero) ===
        self.hero_role = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "text_hero_role"),
            name="Роль в hero-карточке",
        )
        self.hero_slogan = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "text_hero_slogan"),
            name="Слоган",
        )
        self.hero_subtitle = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "text_hero_subtitle"),
            name="Подзаголовок hero",
        )
        self.hero_description = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "text_hero_description"),
            name="Описание в hero",
        )
        self.hero_talks_button = Button(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "btn_hero_talks"),
            name="Кнопка 'Все доклады' в hero",
        )

        # === Карточка профиля ===
        self.all_talks_button = Button(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "btn_all_talks"),
            name="Кнопка 'Все доклады' в профиле",
        )
        self.profile_contact_button = Button(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "btn_profile_contact"),
            name="Кнопка 'Контакты' в профиле",
        )

        # === Заголовки секций ===
        self.about_header = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "text_about_header"),
            name="Заголовок 'Обо мне'",
        )
        self.stack_header = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "text_stack_header"),
            name="Заголовок 'Стек'",
        )
        self.topics_header = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "text_topics_header"),
            name="Заголовок 'Темы'",
        )
        self.latest_talks_header = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "text_latest_talks_header"),
            name="Заголовок 'Последние доклады'",
        )
        self.contacts_header = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "text_contacts_header"),
            name="Заголовок 'Контакты'",
        )

        # === Кнопка открытия контактов ===
        self.contacts_open_button = Button(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "btn_contacts_open"),
            name="Кнопка 'Открыть контакты'",
        )
