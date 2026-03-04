"""
Элемент: поле ввода мобильного приложения.

Наследует BaseElement и переопределяет type_of → "input".
Добавляет методы для ввода текста (send_keys, clear).

Аналог elements/input.py из autotests-ui, где используется Playwright fill().
В Appium вместо fill() используем send_keys() — это нативный метод Selenium/Appium.
"""

import allure

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger("INPUT")


class Input(BaseElement):
    """
    Поле ввода в мобильном приложении.

    Добавляет:
    - fill(value) — ввод текста в поле
    - clear() — очистка поля
    - check_have_value(value) — проверка значения

    Example:
        search_input = Input(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "input_search_talks"),
            name="Поиск докладов"
        )
        search_input.fill("Python")
        search_input.check_have_value("Python")
    """

    @property
    def type_of(self) -> str:
        """Возвращает 'input' для читаемых логов и allure-шагов."""
        return "input"

    def fill(self, value: str, **kwargs) -> None:
        """
        Очищает поле и вводит новое значение.

        Процесс:
        1. Находит элемент
        2. Очищает текущее значение (element.clear())
        3. Вводит новый текст (element.send_keys(value))

        Args:
            value: Текст для ввода.
            **kwargs: Параметры для подстановки в шаблон локатора.
        """
        step = f'Ввод "{value}" в {self.type_of} "{self.name}"'
        with allure.step(step):
            element = self.find(**kwargs)
            logger.info(step)
            element.clear()
            element.send_keys(value)

    def clear(self, **kwargs) -> None:
        """
        Очищает поле ввода.

        Args:
            **kwargs: Параметры для подстановки в шаблон локатора.
        """
        step = f'Очистка {self.type_of} "{self.name}"'
        with allure.step(step):
            element = self.find(**kwargs)
            logger.info(step)
            element.clear()

    def check_have_value(self, expected_value: str, **kwargs) -> None:
        """
        Проверяет, что поле содержит ожидаемое значение.

        В Android текстовые поля возвращают значение через .text.

        Args:
            expected_value: Ожидаемый текст в поле.
            **kwargs: Параметры для подстановки в шаблон локатора.
        """
        step = f'Проверка значения {self.type_of} "{self.name}" == "{expected_value}"'
        with allure.step(step):
            element = self.find(**kwargs)
            actual_value = element.text
            logger.info(f'{step} → фактическое: "{actual_value}"')
            assert actual_value == expected_value, (
                f'Ожидали значение "{expected_value}", '
                f'получили "{actual_value}"'
            )
