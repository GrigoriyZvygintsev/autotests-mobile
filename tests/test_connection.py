"""
Smoke-тест: проверка подключения к устройству через Appium.

Этот тест проверяет, что:
1. Appium Server запущен и доступен
2. Устройство/эмулятор подключён
3. Приложение TalksApp установлено и запускается
4. Драйвер успешно создаёт сессию

Запуск:
    pytest -m smoke --alluredir=allure-results

Предварительные условия:
    1. Запущен Appium Server: appium
    2. Запущен Android-эмулятор: emulator -avd <имя_avd>
    3. Установлено приложение TalksApp на эмуляторе
    4. Создан .env файл по образцу .env.example
"""

import allure
import pytest
from allure_commons.types import Severity
from appium.webdriver import Remote as AppiumDriver

from config import settings
from tools.allure.epics import AllureEpic
from tools.allure.tags import AllureTag


@allure.epic(AllureEpic.TALKS_APP)
@allure.tag(AllureTag.SMOKE)
@pytest.mark.smoke
class TestConnection:
    """Проверка базового подключения к Appium и устройству."""

    @allure.severity(Severity.BLOCKER)
    @allure.title("Appium-сессия создана успешно")
    def test_driver_session_created(self, appium_driver: AppiumDriver):
        """
        Проверяем, что Appium-драйвер создал сессию.

        Если этот тест проходит — значит вся цепочка работает:
        Тест → Appium Python Client → Appium Server 3.2 → UiAutomator2 → Android
        """
        # Проверяем, что драйвер не None и имеет session_id
        assert appium_driver is not None, "Appium-драйвер не создан"
        assert appium_driver.session_id is not None, "Сессия Appium не создана"

    @allure.severity(Severity.BLOCKER)
    @allure.title("Запущено правильное приложение (TalksApp)")
    def test_app_package_matches(self, appium_driver: AppiumDriver):
        """
        Проверяем, что запущено правильное приложение (TalksApp).

        current_package возвращает имя пакета активного приложения на устройстве.
        Должно совпадать с ANDROID.APP_PACKAGE из .env.
        """
        current_package = appium_driver.current_package
        assert current_package == settings.android.app_package, (
            f"Ожидали пакет '{settings.android.app_package}', "
            f"но активен '{current_package}'"
        )

    @allure.severity(Severity.BLOCKER)
    @allure.title("Открыта главная Activity приложения")
    def test_app_activity_is_main(self, appium_driver: AppiumDriver):
        """
        Проверяем, что открыта главная Activity приложения.

        current_activity возвращает имя текущей Activity.
        После запуска должна быть .MainActivity.
        """
        current_activity = appium_driver.current_activity
        assert ".MainActivity" in current_activity, (
            f"Ожидали MainActivity, но активна '{current_activity}'"
        )
