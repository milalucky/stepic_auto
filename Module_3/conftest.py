from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest

# для корректного отображения кириллицы в параметризаторах
def pytest_make_parametrize_id(config, val):
    return repr(val)

# добавляем параметр запуска тестов в командной строке (чем запускать, хромом или фаерфоксом) По умолчанию хром
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")

# Запуск браузера (для каждой функции)
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart Chrome browser for test..")
        service = ChromeService(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        print("\nstart Firefox browser for test..")
        service = FirefoxService(GeckoDriverManager().install())
        browser = webdriver.Firefox(service=service)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
