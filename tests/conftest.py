import pytest
from playwright.sync_api import sync_playwright
from config import BROWSERS


@pytest.fixture(scope="session", params=[(browser, version) for browser in BROWSERS for version in BROWSERS[browser]])
def browser_config(request):
    return request.param


@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright, browser_config):
    browser_name, browser_version = browser_config
    browser_type = getattr(playwright, browser_name)

    if browser_version == "latest":
        browser = browser_type.launch(headless=False)
    else:
        # Запуск браузера с указанной версией
        # (необходимо установить браузеры этих версий вручную и прописать путь к ним)
        executable_path = f'/path/to/{browser_name}-{browser_version}'
        browser = browser_type.launch(headless=False, executable_path=executable_path)

    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()
