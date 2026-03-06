"""
Фабрика Appium-драйвера.

Создаёт и настраивает экземпляр Appium WebDriver для подключения
к Android-устройству/эмулятору через Appium Server 3.2.

Аналог tools/playwright/pages.py из autotests-ui:
    - В UI-фреймворке: Playwright → Browser → Context → Page
    - В мобильном фреймворке: Appium Server → UiAutomator2Options → Remote Driver

Appium использует W3C WebDriver Protocol для общения с устройством.
Цепочка: Тест → Appium Python Client → Appium Server → UIAutomator2 → Android Device.
"""

from appium import webdriver
from appium.options.android import UiAutomator2Options

from config import settings
from tools.logger import get_logger

# Логгер для отслеживания жизненного цикла драйвера
logger = get_logger("APPIUM_DRIVER")


def create_appium_driver() -> webdriver.Remote:
    """
    Создаёт и возвращает Appium-драйвер с настройками из config.

    Процесс создания:
    1. Создаём UiAutomator2Options с capabilities из config.py
    2. Подключаемся к Appium Server по URL из config.py
    3. Возвращаем готовый драйвер для взаимодействия с приложением

    UiAutomator2Options — это типизированная обёртка над Desired Capabilities.
    В Appium 3.x / Python Client 4.x используем Options вместо словаря capabilities.

    Returns:
        webdriver.Remote: Appium-драйвер, подключённый к устройству.

    Raises:
        WebDriverException: Если не удалось подключиться к Appium Server
                           или устройство недоступно.

    Example:
        >>> driver = create_appium_driver()
        >>> driver.find_element(AppiumBy.ID, "screen_home")
    """
    # Создаём объект опций для UIAutomator2 (Android)
    # Это аналог Desired Capabilities, но с типизацией и автодополнением
    options = UiAutomator2Options()

    # Указываем платформу (Android) и драйвер автоматизации (UiAutomator2)
    options.platform_name = settings.android.platform_name
    options.automation_name = settings.android.automation_name

    # Имя устройства — для эмулятора обычно "emulator-5554"
    options.device_name = settings.android.device_name

    # Пакет и Activity тестируемого приложения
    # app_package — уникальный идентификатор приложения (com.gzvyagintsev.talks)
    # app_activity — точка входа в приложение (.MainActivity)
    options.app_package = settings.android.app_package
    options.app_activity = settings.android.app_activity

    # no_reset=True — не сбрасывать данные приложения между сессиями
    # Это ускоряет тесты, т.к. не нужно заново устанавливать/настраивать приложение
    options.no_reset = settings.android.no_reset

    # Jetpack Compose testTag() маппится на resource-id без префикса пакета.
    # По умолчанию UiAutomator2 добавляет пакет к id-запросам (com.pkg:id/value).
    # Отключаем это, чтобы AppiumBy.ID находил Compose testTag напрямую.
    options.set_capability("appium:disableIdLocatorAutocompletion", True)

    logger.info(
        f"Создаём Appium-драйвер: "
        f"server={settings.appium_server.url}, "
        f"device={settings.android.device_name}, "
        f"package={settings.android.app_package}"
    )

    # Подключаемся к Appium Server и создаём сессию
    # command_executor — URL Appium Server (по умолчанию http://127.0.0.1:4723)
    # options — настройки подключения к устройству
    driver = webdriver.Remote(
        command_executor=settings.appium_server.url,
        options=options,
    )

    logger.info(
        f"Appium-драйвер создан. Session ID: {driver.session_id}"
    )

    return driver
