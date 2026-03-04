"""
Page Object: Экран деталей доклада (Talk Detail Screen) TalksApp.

Отображается при тапе на карточку доклада из списка.
Содержит полную информацию: заголовок, описание, формат, outline, кнопки действий.

Навигация: TalksList → тап на карточку → TalkDetail.
Возврат: кнопка "Назад" (btn_back).
"""

from appium.webdriver import Remote as AppiumDriver
from appium.webdriver.common.appiumby import AppiumBy

from elements.base_element import BaseElement
from elements.button import Button
from elements.text import Text
from pages.base_page import BasePage


class TalkDetailPage(BasePage):
    """
    Page Object экрана деталей доклада.

    На этом экране bottom navigation скрыт (detail screen).
    """

    def __init__(self, driver: AppiumDriver):
        super().__init__(driver)

        # === Экран ===
        self.screen = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "screen_talk_detail"),
            name="Экран 'Детали доклада'",
        )

        # === Навигация ===
        self.back_button = Button(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "btn_back"),
            name="Кнопка 'Назад'",
        )

        # === Метаданные доклада ===
        self.title = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "text_detail_title"),
            name="Заголовок доклада",
        )
        self.duration = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "text_detail_duration"),
            name="Длительность",
        )
        self.date = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "text_detail_date"),
            name="Дата доклада",
        )
        self.formats = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "text_detail_formats"),
            name="Форматы доклада",
        )
        self.summary = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "text_detail_summary"),
            name="Краткое описание",
        )

        # === Описание (аудитория, темы, takeaway) ===
        self.audience = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "text_audience"),
            name="Аудитория",
        )
        self.topics = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "text_topics"),
            name="Темы",
        )
        self.takeaway = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "text_takeaway"),
            name="Takeaway",
        )

        # === Outline (параметризованные элементы) ===
        # outline_item_{index} — индекс 1-based
        self.outline_item = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "outline_item_{index}"),
            name="Пункт плана доклада",
        )

        # === Кнопки действий ===
        self.open_viewer_button = Button(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "btn_open_viewer"),
            name="Кнопка 'Открыть просмотр'",
        )
        self.download_pdf_button = Button(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "btn_download_pdf"),
            name="Кнопка 'Скачать PDF'",
        )
        self.open_repo_button = Button(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "btn_open_repo"),
            name="Кнопка 'Открыть репозиторий'",
        )

        # === Состояния ===
        self.loading_progress = BaseElement(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "progress_detail_loading"),
            name="Индикатор загрузки",
        )
        self.not_found_text = Text(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "text_talk_not_found"),
            name="Сообщение 'доклад не найден'",
        )
