"""
Фикстура жизненного цикла Appium-драйвера.

Управляет созданием и закрытием драйвера для каждого теста.
Аналог fixtures/browsers.py из autotests-ui, где Playwright browser
создаётся/закрывается для каждого теста.

Жизненный цикл:
    1. Перед тестом: create_appium_driver() → подключение к устройству
    2. yield driver → тест выполняется с драйвером
    3. После теста: driver.quit() → закрытие сессии

Scope: function (каждый тест получает свежий драйвер).
Это изолирует тесты друг от друга — падение одного теста
не влияет на состояние драйвера для следующего.
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

    Yields:
        AppiumDriver: Активный драйвер, подключённый к устройству.

    Example:
        def test_home_screen(self, appium_driver: AppiumDriver):
            # appium_driver уже подключён к устройству
            element = appium_driver.find_element(...)
    """
    logger.info("Создаём Appium-драйвер для теста")
    driver = create_appium_driver()

    # yield передаёт драйвер в тест; после завершения теста
    # выполнение продолжается ниже (teardown)
    yield driver

    # Teardown: закрываем сессию и освобождаем ресурсы
    logger.info("Закрываем Appium-драйвер")
    driver.quit()
