"""
Модуль логирования фреймворка.

Предоставляет функцию get_logger() для создания настроенных логгеров.
Формат вывода: "2026-03-04 12:00:00 | APPIUM_DRIVER | INFO | Сообщение"

Паттерн идентичен autotests-api/tools/logger.py и autotests-ui/tools/logger.py.
"""

import logging


def get_logger(name: str) -> logging.Logger:
    """
    Создаёт и настраивает логгер с указанным именем.

    Каждый логгер выводит сообщения в консоль (StreamHandler) с форматом:
        %(asctime)s | %(name)s | %(levelname)s | %(message)s

    Args:
        name: Имя логгера (например, "APPIUM_DRIVER", "BASE_ELEMENT").
              Используется для идентификации источника сообщения в логе.

    Returns:
        Настроенный экземпляр logging.Logger.

    Example:
        >>> logger = get_logger("HOME_PAGE")
        >>> logger.info("Открываем главную страницу")
        2026-03-04 12:00:00 | HOME_PAGE | INFO | Открываем главную страницу
    """
    # Инициализация логгера с указанным именем
    logger = logging.getLogger(name)

    # Защита от дублирования: если logger уже настроен — возвращаем как есть.
    # Без этой проверки повторный вызов get_logger("X") добавит ещё один handler,
    # и каждое сообщение будет печататься 2, 3, ... раз.
    if not logger.handlers:
        # Устанавливаем уровень логирования DEBUG для логгера,
        # чтобы он обрабатывал все сообщения от DEBUG и выше
        logger.setLevel(logging.DEBUG)

        # Создаем обработчик, который будет выводить логи в консоль
        handler = logging.StreamHandler()
        # Устанавливаем уровень логирования DEBUG для обработчика,
        # чтобы он обрабатывал все сообщения от DEBUG и выше
        handler.setLevel(logging.DEBUG)

        # Задаем форматирование лог-сообщений: включаем время, имя логгера, уровень и сообщение
        formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")
        handler.setFormatter(formatter)  # Применяем форматтер к обработчику

        # Добавляем обработчик к логгеру
        logger.addHandler(handler)

    # Возвращаем настроенный логгер
    return logger
