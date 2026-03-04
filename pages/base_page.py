"""
Базовый Page Object для мобильного приложения.

Аналог pages/base_page.py из autotests-ui, адаптированный под Appium.

Ключевые отличия от UI-фреймворка:
    - Вместо page.goto(url) — нет прямой навигации по URL в нативном приложении.
    - Вместо page.reload() — мобильные жесты: swipe, scroll.
    - Добавлен метод take_screenshot() для Allure-вложений.
    - Навигация через элементы приложения (bottom navigation bar).

Каждая конкретная страница (HomePage, TalksPage и т.д.) наследует BasePage
и объявляет свои элементы как атрибуты класса.
"""

import allure
from appium.webdriver import Remote as AppiumDriver

from tools.logger import get_logger

logger = get_logger("BASE_PAGE")


class BasePage:
    """
    Базовый класс для всех Page Object'ов мобильного приложения.

    Содержит общие методы для работы с экранами:
    - Жесты (swipe up/down)
    - Скриншоты
    - Ожидание загрузки экрана

    Attributes:
        driver: Appium-драйвер, подключённый к устройству.
    """

    def __init__(self, driver: AppiumDriver):
        """
        Инициализирует Page Object с Appium-драйвером.

        Args:
            driver: Активный Appium-драйвер.
        """
        self.driver = driver

    def swipe_up(self, duration: int = 800) -> None:
        """
        Свайп вверх — прокрутка контента вниз.

        Свайп от 80% высоты экрана до 20% высоты экрана.
        Используется для прокрутки длинных списков и страниц.

        Args:
            duration: Длительность свайпа в миллисекундах.
                     Чем больше — тем медленнее и стабильнее.
        """
        step = "Свайп вверх (прокрутка вниз)"
        with allure.step(step):
            logger.info(step)
            size = self.driver.get_window_size()
            start_x = size["width"] // 2
            start_y = int(size["height"] * 0.8)
            end_y = int(size["height"] * 0.2)
            self.driver.swipe(start_x, start_y, start_x, end_y, duration)

    def swipe_down(self, duration: int = 800) -> None:
        """
        Свайп вниз — прокрутка контента вверх.

        Свайп от 20% высоты экрана до 80% высоты экрана.
        Используется для возврата к началу страницы или pull-to-refresh.

        Args:
            duration: Длительность свайпа в миллисекундах.
        """
        step = "Свайп вниз (прокрутка вверх)"
        with allure.step(step):
            logger.info(step)
            size = self.driver.get_window_size()
            start_x = size["width"] // 2
            start_y = int(size["height"] * 0.2)
            end_y = int(size["height"] * 0.8)
            self.driver.swipe(start_x, start_y, start_x, end_y, duration)

    def take_screenshot(self, name: str = "screenshot") -> None:
        """
        Делает скриншот текущего экрана и прикрепляет к Allure-отчёту.

        Args:
            name: Имя скриншота в отчёте (например, "главная_страница").
        """
        step = f'Скриншот: "{name}"'
        with allure.step(step):
            logger.info(step)
            png = self.driver.get_screenshot_as_png()
            allure.attach(
                png,
                name=name,
                attachment_type=allure.attachment_type.PNG,
            )

    def get_page_source(self) -> str:
        """
        Возвращает XML-дерево текущего экрана.

        Полезно для отладки — показывает все элементы с их атрибутами.
        Аналог DevTools → Elements в браузере.

        Returns:
            XML-строка с деревом элементов экрана.
        """
        step = "Получение page source (XML-дерево экрана)"
        with allure.step(step):
            logger.info(step)
            return self.driver.page_source
