"""
Компонент: нижняя навигационная панель (Bottom Navigation Bar).

Присутствует на всех основных экранах TalksApp:
    Главная | Доклады | Мемы | Чат | Контакт

На detail-экранах (TalkDetail, TalkViewer) панель скрыта.

TestTags из TalksApp:
    nav_home, nav_talks, nav_memes, nav_chat, nav_contact
"""

from appium.webdriver import Remote as AppiumDriver
from appium.webdriver.common.appiumby import AppiumBy

from elements.button import Button


class BottomNavigation:
    """
    Компонент нижней навигации TalksApp.

    Используется из любого Page Object для перехода между экранами.
    """

    def __init__(self, driver: AppiumDriver):
        self.driver = driver

        self.home_tab = Button(
            driver=driver,
            locator=(AppiumBy.ID, "nav_home"),
            name="Таб 'Главная'",
        )
        self.talks_tab = Button(
            driver=driver,
            locator=(AppiumBy.ID, "nav_talks"),
            name="Таб 'Доклады'",
        )
        self.memes_tab = Button(
            driver=driver,
            locator=(AppiumBy.ID, "nav_memes"),
            name="Таб 'Мемы'",
        )
        self.chat_tab = Button(
            driver=driver,
            locator=(AppiumBy.ID, "nav_chat"),
            name="Таб 'Чат'",
        )
        self.contacts_tab = Button(
            driver=driver,
            locator=(AppiumBy.ID, "nav_contact"),
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
