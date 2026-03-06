"""
Фикстура жизненного цикла Appium-драйвера.

Управляет созданием и закрытием драйвера для каждого теста.

Жизненный цикл:
    1. Перед тестом: create_appium_driver() → подключение к устройству
    2. yield driver → тест выполняется с драйвером
    3. После теста: driver.quit() → закрытие сессии

Scope: function (каждый тест получает свежий драйвер).
При noReset=false Appium сам сбрасывает состояние приложения
при создании новой сессии — ручная очистка не нужна.
"""

import pytest
from appium.webdriver import Remote as AppiumDriver

from tools.appium.driver import create_appium_driver
from tools.logger import get_logger

logger = get_logger("FIXTURE_DRIVER")


@pytest.fixture
def appium_driver() -> AppiumDriver:
    """
    Создаёт Appium-драйвер перед тестом и закрывает после.

    При noReset=false (default) каждая новая сессия стартует
    приложение с чистым состоянием на главном экране.
    """
    logger.info("Создаём Appium-драйвер для теста")
    driver = create_appium_driver()

    yield driver

    logger.info("Закрываем Appium-драйвер")
    driver.quit()
