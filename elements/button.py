"""
Элемент: кнопка мобильного приложения.

Наследует BaseElement и переопределяет type_of → "button".
Добавляет специфичные для кнопок проверки (enabled/disabled).

Аналог elements/button.py из autotests-ui.
"""

import allure

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger("BUTTON")


class Button(BaseElement):
    """
    Кнопка в мобильном приложении.

    Помимо базовых действий (click, check_visible), добавляет:
    - check_enabled() — проверка, что кнопка активна
    - check_disabled() — проверка, что кнопка неактивна

    Example:
        talks_button = Button(
            driver=driver,
            locator=(AppiumBy.ACCESSIBILITY_ID, "btn_hero_talks"),
            name="Кнопка 'Все доклады'"
        )
        talks_button.check_enabled()
        talks_button.click()
    """

    @property
    def type_of(self) -> str:
        """Возвращает 'button' для читаемых логов и allure-шагов."""
        return "button"

    def check_enabled(self, **kwargs) -> None:
        """
        Проверяет, что кнопка активна (можно нажать).

        В Android: элемент имеет атрибут enabled=true.

        Args:
            **kwargs: Параметры для подстановки в шаблон локатора.
        """
        step = f'Проверка что {self.type_of} "{self.name}" активна'
        with allure.step(step):
            element = self.find(**kwargs)
            logger.info(step)
            assert element.is_enabled(), (
                f'{self.type_of} "{self.name}" неактивна (disabled)'
            )

    def check_disabled(self, **kwargs) -> None:
        """
        Проверяет, что кнопка неактивна (нельзя нажать).

        Args:
            **kwargs: Параметры для подстановки в шаблон локатора.
        """
        step = f'Проверка что {self.type_of} "{self.name}" неактивна'
        with allure.step(step):
            element = self.find(**kwargs)
            logger.info(step)
            assert not element.is_enabled(), (
                f'{self.type_of} "{self.name}" активна, ожидали disabled'
            )
