"""
Конфигурация тестового фреймворка.

Используем Pydantic BaseSettings для:
- Чтения настроек из .env файла
- Валидации типов конфигурации
- Автоматического создания необходимых директорий

Паттерн аналогичен autotests-api/config.py и autotests-ui/config.py.
"""

from pathlib import Path
from typing import Self

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppiumServerConfig(BaseModel):
    """
    Настройки подключения к Appium Server.

    Appium Server 3.2 по умолчанию слушает на http://127.0.0.1:4723.
    """

    url: str = "http://127.0.0.1:4723"


class AndroidConfig(BaseModel):
    """
    Desired Capabilities для Android-устройства.

    Эти параметры передаются через UiAutomator2Options при создании драйвера.

    Attributes:
        platform_name: Платформа — всегда "Android" для Android-тестов.
        automation_name: Драйвер автоматизации — "UiAutomator2" (стандарт для Android).
        device_name: Имя устройства/эмулятора (например, "emulator-5554").
        app_package: Пакет тестируемого приложения (например, "com.gzvyagintsev.talks").
        app_activity: Главная Activity приложения (например, ".MainActivity").
        no_reset: Если True — не сбрасывать состояние приложения между тестами.
    """

    platform_name: str = "Android"
    automation_name: str = "UiAutomator2"
    device_name: str = "emulator-5554"
    app_package: str = ""
    app_activity: str = ""
    no_reset: bool = True


class Settings(BaseSettings):
    """
    Главный класс настроек фреймворка.

    Читает конфигурацию из .env файла. Вложенные переменные разделяются точкой:
        APPIUM_SERVER.URL="http://127.0.0.1:4723"
        ANDROID.APP_PACKAGE="com.gzvyagintsev.talks"

    Attributes:
        appium_server: Настройки Appium Server.
        android: Capabilities для Android-устройства.
        screenshots_dir: Путь к папке со скриншотами.
        allure_results_dir: Путь к папке с результатами Allure.
    """

    model_config = SettingsConfigDict(
        extra="allow",
        env_file=".env",  # Указываем, из какого файла читать настройки
        env_file_encoding="utf-8",  # Указываем кодировку файла
        env_nested_delimiter=".",  # Разделитель для вложенных переменных (ANDROID.DEVICE_NAME)
    )

    appium_server: AppiumServerConfig = AppiumServerConfig()
    android: AndroidConfig = AndroidConfig()
    screenshots_dir: Path = Path("./screenshots")
    allure_results_dir: Path = Path("./allure-results")

    @classmethod
    def initialize(cls) -> Self:
        """
        Фабричный метод: создаёт экземпляр Settings и подготавливает директории.

        Создаёт папки screenshots/ и allure-results/, если они не существуют.
        Паттерн аналогичен autotests-api: Settings.initialize() вызывается один раз
        при импорте модуля.
        """
        # Создаём директории для артефактов тестов
        screenshots_dir = Path("./screenshots")
        screenshots_dir.mkdir(exist_ok=True)

        allure_results_dir = Path("./allure-results")
        allure_results_dir.mkdir(exist_ok=True)

        return cls(
            screenshots_dir=screenshots_dir,
            allure_results_dir=allure_results_dir,
        )


# Глобальный экземпляр настроек — импортируется во всех модулях
# Пример использования: from config import settings
settings = Settings.initialize()
