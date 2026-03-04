"""
Компонент: нижняя навигационная панель (Bottom Navigation Bar).

Присутствует на всех основных экранах TalksApp:
    Главная | Доклады | Мемы | Чат | Контакт

На detail-экранах (TalkDetail, TalkViewer) панель скрыта.

TestTag'и: nav_home, nav_talks, nav_memes, nav_chat, nav_contacts.
"""

from appium.webdriver import Remote as AppiumDriver
from appium.webdriver.common.appiumby import AppiumBy

from elements.base_element import BaseElement
from elements.button import Button


class BottomNavigation:
    """
    Компонент нижней навигации TalksApp.

    Используется из любого Page Object для перехода между экранами.

    Example:
        class HomePage(BasePage):
            def __init__(self, driver):
                super().__init__(driver)
                self.bottom_nav = BottomNavigation(driver)

        # В тесте:
        home_page.bottom_nav.go_to_talks()
    """

    def __init__(self, driver: AppiumDriver):
        self.driver = driver

        # Контейнер всей навигации
        self.bar = BaseElement(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "bottom_navigation"),
            name="Нижняя навигация",
        )

        # Кнопки навигации
        self.home_tab = Button(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "nav_home"),
            name="Таб 'Главная'",
        )
        self.talks_tab = Button(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "nav_talks"),
            name="Таб 'Доклады'",
        )
        self.memes_tab = Button(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "nav_memes"),
            name="Таб 'Мемы'",
        )
        self.chat_tab = Button(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "nav_chat"),
            name="Таб 'Чат'",
        )
        self.contacts_tab = Button(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "nav_contacts"),
            name="Таб 'Контакт'",
        )

    def go_to_home(self) -> None:
        """Переход на главный экран."""
        self.home_tab.click()

    def go_to_talks(self) -> None:
        """Переход на экран докладов."""
        self.talks_tab.click()

    def go_to_memes(self) -> None:
        """Переход на экран мемов."""
        self.memes_tab.click()

    def go_to_chat(self) -> None:
        """Переход на экран чата."""
        self.chat_tab.click()

    def go_to_contacts(self) -> None:
        """Переход на экран контактов."""
        self.contacts_tab.click()
