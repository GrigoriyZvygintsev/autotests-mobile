"""
Page Object: Экран списка докладов (Talks List Screen) TalksApp.

Содержит:
- Заголовок экрана
- Поле поиска
- Фильтры по формату, уровню и тегам
- Список карточек докладов (LazyColumn)
- Индикатор загрузки и сообщение "нет результатов"

Карточки докладов имеют параметризованные testTag'и:
    card_talk_{slug}, text_talk_title_{slug}, badge_level_{slug} и т.д.
"""

from appium.webdriver import Remote as AppiumDriver
from appium.webdriver.common.appiumby import AppiumBy

from elements.base_element import BaseElement
from elements.button import Button
from elements.input import Input
from elements.text import Text
from pages.base_page import BasePage


class TalksListPage(BasePage):
    """
    Page Object экрана списка докладов.

    Навигация: bottom navigation → "Доклады" (nav_talks).
    """

    def __init__(self, driver: AppiumDriver):
        super().__init__(driver)

        # === Экран ===
        self.screen = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "screen_talks_list"),
            name="Экран 'Список докладов'",
        )

        # === Заголовок ===
        self.title = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "text_talks_title"),
            name="Заголовок 'Доклады'",
        )

        # === Поиск ===
        self.search_input = Input(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "input_search_talks"),
            name="Поиск докладов",
        )

        # === Фильтры ===
        self.format_filters = BaseElement(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "row_format_filters"),
            name="Фильтры по формату",
        )
        self.level_filters = BaseElement(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "row_level_filters"),
            name="Фильтры по уровню",
        )
        self.tag_filters = BaseElement(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "row_tag_filters"),
            name="Фильтры по тегам",
        )

        # === Список докладов ===
        self.talks_list = BaseElement(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "list_talks"),
            name="Список докладов",
        )

        # === Состояния загрузки ===
        self.loading_progress = BaseElement(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "progress_loading"),
            name="Индикатор загрузки",
        )
        self.no_results_text = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "text_no_results"),
            name="Сообщение 'нет результатов'",
        )

        # === Параметризованные элементы карточек ===
        # Используют шаблон с {slug}: card_talk_{slug}
        # Вызов: self.talk_card.check_visible(slug="python-basics")
        self.talk_card = BaseElement(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "card_talk_{slug}"),
            name="Карточка доклада",
        )
        self.talk_title = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "text_talk_title_{slug}"),
            name="Заголовок доклада",
        )
        self.talk_summary = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "text_talk_summary_{slug}"),
            name="Описание доклада",
        )
        self.talk_level_badge = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "badge_level_{slug}"),
            name="Бейдж уровня доклада",
        )
        self.talk_duration = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "text_duration_{slug}"),
            name="Длительность доклада",
        )
