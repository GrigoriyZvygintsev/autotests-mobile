# autotests-mobile

Тестовый фреймворк для мобильного тестирования приложения **TalksApp** на Appium 3.2.

## Стек

- **Appium Server 3.2** + UiAutomator2 (Android)
- **Appium Python Client 4.x** (W3C WebDriver Protocol)
- **pytest** — тестовый раннер
- **allure-pytest** — отчёты с скриншотами
- **Pydantic** — конфигурация через `.env`
- **GitHub Actions** — CI/CD с Android-эмулятором

## Структура проекта

```
autotests-mobile/
├── config.py                # Pydantic BaseSettings конфигурация
├── conftest.py              # Регистрация фикстур + hook скриншотов
├── pytest.ini               # Маркеры pytest
├── requirements.txt         # Зависимости Python
├── .env.example             # Шаблон переменных окружения
│
├── elements/                # Абстракция UI-элементов
│   ├── base_element.py      # BaseElement (find, click, check_visible)
│   ├── button.py            # Button (check_enabled/disabled)
│   ├── input.py             # Input (fill, clear, check_value)
│   └── text.py              # Text (get_text, check_have_text)
│
├── pages/                   # Page Object Model
│   ├── base_page.py         # BasePage (swipe, screenshot)
│   ├── home/home_page.py    # Главный экран
│   ├── talks/               # Доклады (список + детали)
│   └── contacts/            # Контакты + CAPTCHA
│
├── components/              # Переиспользуемые UI-компоненты
│   └── navigation/          # Bottom Navigation Bar
│
├── fixtures/                # pytest фикстуры
│   ├── driver.py            # Appium-драйвер (yield + quit)
│   ├── pages.py             # Page Object фикстуры
│   └── allure.py            # environment.properties
│
├── tools/                   # Утилиты
│   ├── logger.py            # Логгер с форматом "time | name | level | msg"
│   ├── appium/driver.py     # Фабрика Appium-драйвера
│   ├── appium/screenshot.py # Скриншоты → Allure
│   ├── allure/              # Epic, Feature, Story, Tag enums
│   └── assertions/base.py   # Ассерты с @allure.step
│
├── tests/                   # Тесты по экранам
│   ├── smoke/               # Smoke: подключение к устройству
│   ├── home/                # Главный экран
│   ├── navigation/          # Bottom navigation
│   ├── talks/               # Список и детали докладов
│   └── contacts/            # Контакты и CAPTCHA
│
└── .github/workflows/       # CI/CD
    └── tests.yml            # GitHub Actions: эмулятор + Allure → Pages
```

## Быстрый старт

### Предварительные условия

1. **Python 3.12+**
2. **Node.js 20+** (для Appium Server)
3. **Android SDK** + эмулятор
4. **Java 17+** (для Android SDK)

### Установка

```bash
# 1. Клонируем репозиторий
git clone https://github.com/GrigoriyZvygintsev/autotests-mobile.git
cd autotests-mobile

# 2. Создаём виртуальное окружение
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Устанавливаем зависимости
pip install -r requirements.txt

# 4. Устанавливаем Appium Server
npm install -g appium
appium driver install uiautomator2

# 5. Копируем конфигурацию
cp .env.example .env
# Редактируем .env при необходимости
```

### Запуск тестов

```bash
# Запускаем Appium Server (в отдельном терминале)
appium

# Запускаем Android-эмулятор (в отдельном терминале)
emulator -avd <имя_avd>

# Запускаем тесты
pytest -m smoke --alluredir=allure-results     # Smoke-тесты
pytest -m regression --alluredir=allure-results # Все регрессионные тесты

# Открываем Allure-отчёт
allure serve allure-results
```

## CI/CD

GitHub Actions автоматически:
1. Запускает Android-эмулятор
2. Устанавливает Appium Server 3.2
3. Прогоняет тесты с генерацией Allure results
4. Публикует Allure-отчёт на GitHub Pages

## Связанные проекты

- [TalksApp](https://github.com/GrigoriyZvygintsev/TalksApp) — тестируемое Android-приложение
- [autotests-api](https://github.com/GrigoriyZvygintsev/autotests-api) — API тестовый фреймворк
- [autotests-ui](https://github.com/GrigoriyZvygintsev/autotests-ui) — UI тестовый фреймворк
- [site_qa_expert](https://github.com/GrigoriyZvygintsev/site_qa_expert) — портфолио-сайт
