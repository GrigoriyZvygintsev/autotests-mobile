"""
Элемент: текстовый блок мобильного приложения.

Наследует BaseElement и переопределяет type_of → "text".
Текстовый элемент — это любой UI-компонент, отображающий текст
(заголовки, описания, бейджи, метки).

Аналог elements/text.py из autotests-ui.
Не добавляет новых методов — все действия (get_text, check_have_text)
наследуются от BaseElement.
"""

from elements.base_element import BaseElement


class Text(BaseElement):
    """
    Текстовый элемент в мобильном приложении.

    Используется для заголовков, описаний, бейджей и любых текстовых блоков.
    Все методы наследуются от BaseElement: check_visible, get_text, check_have_text.

    Example:
        hero_title = Text(
            driver=driver,
            locator=(AppiumBy.ID, "text_hero_slogan"),
            name="Слоган на главной"
        )
        hero_title.check_have_text("Превращаю хаос в стабильные релизы")
    """

    @property
    def type_of(self) -> str:
        """Возвращает 'text' для читаемых логов и allure-шагов."""
        return "text"
