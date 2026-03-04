"""
Генерация файла environment.properties для Allure-отчёта.

Файл environment.properties отображается на главной странице Allure-отчёта
и содержит информацию об окружении тестового запуска:
- Версия ОС, Python
- Настройки Appium (server URL, device, package)

Паттерн аналогичен autotests-api/tools/allure/environment.py.
"""

import platform
import sys

from config import settings


def create_allure_environment_file() -> None:
    """
    Создаёт файл environment.properties в папке allure-results.

    Этот файл читается Allure при генерации отчёта и показывает
    информацию об окружении на вкладке "Environment".

    Содержимое:
        - Все настройки из config.py (сериализованные через model_dump)
        - Информация об ОС (system, release)
        - Версия Python
    """
    # Собираем информацию об ОС и Python
    os_info = f"os_info={platform.system()}, {platform.release()}"
    python_version = f"python_version={sys.version}"

    # Сериализуем все настройки из Pydantic-модели в формат key=value
    items = [f"{key}={value}" for key, value in settings.model_dump().items()]
    items.extend([os_info, python_version])

    # Собираем все элементы в единую строку с переносами
    properties = "\n".join(items)

    # Записываем в файл ./allure-results/environment.properties
    env_file = settings.allure_results_dir / "environment.properties"
    with open(env_file, "w+", encoding="utf-8") as file:
        file.write(properties)
