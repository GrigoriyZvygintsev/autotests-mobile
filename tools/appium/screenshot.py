"""
Утилита для создания скриншотов и прикрепления к Allure.

Используется:
1. Вручную через BasePage.take_screenshot()
2. Автоматически при падении теста (hook pytest_runtest_makereport)
"""

import allure
from appium.webdriver import Remote as AppiumDriver

from tools.logger import get_logger

logger = get_logger("SCREENSHOT")


def attach_screenshot(driver: AppiumDriver, name: str = "screenshot") -> None:
    """
    Делает скриншот текущего экрана и прикрепляет к Allure-отчёту.

    Скриншот сохраняется в формате PNG и добавляется как вложение (attachment)
    к текущему шагу или тесту в Allure.

    Args:
        driver: Appium-драйвер (должен быть активен).
        name: Имя скриншота в отчёте (например, "FAIL-test_home_visible").
    """
    try:
        png = driver.get_screenshot_as_png()
        allure.attach(
            png,
            name=name,
            attachment_type=allure.attachment_type.PNG,
        )
        logger.info(f'Скриншот "{name}" прикреплён к Allure')
    except Exception as e:
        # Если драйвер уже закрыт или не отвечает — логируем ошибку,
        # но не падаем (скриншот — вспомогательная функция)
        logger.warning(f'Не удалось сделать скриншот "{name}": {e}')
