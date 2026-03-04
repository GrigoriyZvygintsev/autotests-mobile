"""
Корневой conftest.py — точка регистрации всех pytest-плагинов (фикстур).

Pytest автоматически находит этот файл в корне проекта и загружает
указанные модули как плагины. Каждый модуль в fixtures/ содержит
набор связанных фикстур.

Паттерн аналогичен autotests-api/conftest.py и autotests-ui/conftest.py:
    - Вместо импорта фикстур в каждом тесте, регистрируем их централизованно.
    - Это позволяет pytest автоматически внедрять фикстуры по имени параметра.

Дополнительно содержит hook pytest_runtest_makereport для автоскриншотов
при падении тестов (аналог Playwright tracing в autotests-ui).
"""

import pytest

from tools.appium.screenshot import attach_screenshot

pytest_plugins = (
    "fixtures.driver",
    "fixtures.pages",
    "fixtures.allure",
)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook: автоматический скриншот при падении теста.

    Срабатывает после каждой фазы теста (setup, call, teardown).
    Если фаза "call" (выполнение тела теста) завершилась с ошибкой —
    делаем скриншот и прикрепляем к Allure-отчёту.

    Это аналог автоматического tracing в autotests-ui:
    - В UI: сохраняется Playwright trace + видео
    - В mobile: сохраняется скриншот экрана

    Скриншот именуется "FAIL-<имя_теста>" для лёгкого поиска в отчёте.
    """
    outcome = yield
    report = outcome.get_result()

    # Проверяем, что это фаза выполнения теста (не setup/teardown)
    # и что тест упал
    if report.when == "call" and report.failed:
        # Пытаемся получить драйвер из фикстур теста
        driver = item.funcargs.get("appium_driver")
        if driver:
            attach_screenshot(driver, name=f"FAIL-{item.name}")
