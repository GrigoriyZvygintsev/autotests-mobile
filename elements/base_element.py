"""
Базовый элемент мобильного приложения.

Аналог elements/base_element.py из autotests-ui, адаптированный под Appium.

Ключевые отличия от UI-фреймворка (Playwright):
    - Вместо Playwright Page + CSS-локатор используем AppiumDriver + tuple-локатор.
    - Tuple-локатор: (AppiumBy.ID, "screen_home") — стратегия + значение.
    - В TalksApp элементы имеют testTag — это маппится на resource-id в Appium.
    - Вместо expect(locator).to_be_visible() используем WebElement.is_displayed().
    - Нет coverage tracking (ui-coverage-tool специфичен для web).

Иерархия элементов:
    BaseElement → Button, Input, Text (и другие)
    Каждый наследник переопределяет type_of для читаемых логов.
"""

import allure
from appium.webdriver import Remote as AppiumDriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tools.logger import get_logger

logger = get_logger("BASE_ELEMENT")

# Таймаут ожидания элемента по умолчанию (секунды)
DEFAULT_WAIT_TIMEOUT: int = 20


class BaseElement:
    """
    Базовый класс для всех UI-элементов мобильного приложения.

    Инкапсулирует:
    - Поиск элемента на экране через Appium-локатор
    - Ожидание появления элемента (explicit wait)
    - Базовые действия: клик, проверка видимости, получение текста
    - Логирование каждого действия через logger + allure.step

    Attributes:
        driver: Appium-драйвер, подключённый к устройству.
        locator: Tuple из (стратегия_поиска, значение).
                 Пример: (AppiumBy.ID, "btn_hero_talks")
        name: Человекочитаемое имя элемента для логов и отчётов.

    Example:
        hero_button = BaseElement(
            driver=driver,
            locator=(AppiumBy.ID, "btn_hero_talks"),
            name="Кнопка 'Все доклады'"
        )
        hero_button.click()
        hero_button.check_visible()
    """

    def __init__(
        self,
        driver: AppiumDriver,
        locator: tuple[str, str],
        name: str,
    ):
        self.driver = driver
        self.locator = locator  # (AppiumBy.ID, "value")
        self.name = name

    @property
    def type_of(self) -> str:
        """
        Тип элемента для логов. Переопределяется в наследниках.

        Returns:
            "base element" по умолчанию; "button", "input", "text" в наследниках.
        """
        return "base element"

    def _format_locator(self, **kwargs) -> tuple[str, str]:
        """
        Форматирует значение локатора, подставляя динамические параметры.

        Это нужно для параметризованных testTag'ов в TalksApp.
        Пример: ("ID", "card_talk_{slug}") → ("ID", "card_talk_python-basics")

        Args:
            **kwargs: Параметры для подстановки в шаблон локатора.

        Returns:
            Tuple (стратегия, отформатированное_значение).
        """
        by, value = self.locator
        return by, value.format(**kwargs)

    def find(self, timeout: int = DEFAULT_WAIT_TIMEOUT, **kwargs) -> WebElement:
        """
        Находит элемент на экране с явным ожиданием (explicit wait).

        Использует WebDriverWait + expected_conditions.presence_of_element_located.
        Это надёжнее, чем driver.find_element(), т.к. ожидает появления элемента
        в DOM до timeout секунд.

        Args:
            timeout: Максимальное время ожидания в секундах.
            **kwargs: Параметры для подстановки в шаблон локатора.

        Returns:
            WebElement: Найденный элемент.

        Raises:
            TimeoutException: Если элемент не появился за timeout секунд.
        """
        by, value = self._format_locator(**kwargs)
        step = f'Поиск {self.type_of} "{self.name}" ({by}="{value}")'
        with allure.step(step):
            logger.info(step)
            try:
                # WebDriverWait опрашивает DOM каждые 0.5 секунд до timeout
                element = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((by, value))
                )
                return element
            except TimeoutException:
                logger.error(
                    f'Элемент не найден за {timeout}с: '
                    f'{self.type_of} "{self.name}" ({by}="{value}")'
                )
                # Дамп page source для диагностики (какие элементы реально есть на экране)
                try:
                    page_src = self.driver.page_source
                    logger.error(f"Page source на момент падения:\n{page_src}")
                    allure.attach(
                        page_src,
                        name=f"page_source_{self.name}",
                        attachment_type=allure.attachment_type.XML,
                    )
                except Exception:
                    logger.error("Не удалось получить page source")
                raise

    def click(self, **kwargs) -> None:
        """
        Кликает (тапает) по элементу.

        Сначала ищет элемент с ожиданием, затем выполняет tap.

        Args:
            **kwargs: Параметры для подстановки в шаблон локатора.
        """
        step = f'Клик по {self.type_of} "{self.name}"'
        with allure.step(step):
            element = self.find(**kwargs)
            logger.info(step)
            element.click()

    def check_visible(self, timeout: int = DEFAULT_WAIT_TIMEOUT, **kwargs) -> None:
        """
        Проверяет, что элемент отображается на экране.

        Использует WebDriverWait + visibility_of_element_located
        (элемент не только в DOM, но и виден пользователю).

        Args:
            timeout: Максимальное время ожидания видимости.
            **kwargs: Параметры для подстановки в шаблон локатора.

        Raises:
            TimeoutException: Если элемент не стал видимым за timeout секунд.
        """
        by, value = self._format_locator(**kwargs)
        step = f'Проверка видимости {self.type_of} "{self.name}"'
        with allure.step(step):
            logger.info(step)
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )

    def check_not_visible(self, timeout: int = DEFAULT_WAIT_TIMEOUT, **kwargs) -> None:
        """
        Проверяет, что элемент НЕ отображается на экране.

        Args:
            timeout: Максимальное время ожидания исчезновения.
            **kwargs: Параметры для подстановки в шаблон локатора.
        """
        by, value = self._format_locator(**kwargs)
        step = f'Проверка невидимости {self.type_of} "{self.name}"'
        with allure.step(step):
            logger.info(step)
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located((by, value))
            )

    def get_text(self, **kwargs) -> str:
        """
        Возвращает текст элемента.

        В Android/Appium текст берётся из атрибута `text` элемента.

        Args:
            **kwargs: Параметры для подстановки в шаблон локатора.

        Returns:
            Текстовое содержимое элемента.
        """
        step = f'Получение текста {self.type_of} "{self.name}"'
        with allure.step(step):
            element = self.find(**kwargs)
            text = element.text
            logger.info(f'{step} → "{text}"')
            return text

    def check_have_text(self, expected_text: str, **kwargs) -> None:
        """
        Проверяет, что элемент содержит ожидаемый текст.

        Args:
            expected_text: Ожидаемый текст элемента.
            **kwargs: Параметры для подстановки в шаблон локатора.

        Raises:
            AssertionError: Если текст не совпадает.
        """
        step = f'Проверка текста {self.type_of} "{self.name}" == "{expected_text}"'
        with allure.step(step):
            actual_text = self.get_text(**kwargs)
            logger.info(step)
            assert actual_text == expected_text, (
                f'Ожидали текст "{expected_text}", '
                f'получили "{actual_text}"'
            )

    def check_text_contains(self, substring: str, **kwargs) -> None:
        """
        Проверяет, что текст элемента содержит подстроку.

        Полезно, когда точный текст может меняться (даты, счётчики),
        но ключевое слово должно присутствовать.

        Args:
            substring: Подстрока, которая должна быть в тексте.
            **kwargs: Параметры для подстановки в шаблон локатора.
        """
        step = f'Проверка что текст {self.type_of} "{self.name}" содержит "{substring}"'
        with allure.step(step):
            actual_text = self.get_text(**kwargs)
            logger.info(step)
            assert substring in actual_text, (
                f'Ожидали подстроку "{substring}" в тексте, '
                f'получили "{actual_text}"'
            )
