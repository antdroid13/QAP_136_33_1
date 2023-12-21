from selenium.webdriver.chrome.service import Service
from pages.locators import Locators
from selenium import webdriver
from config import PATH
import pytest


@pytest.fixture()
def browser():
    """
    фикстура для инициализации браузера
    """
    # Тесты без открытия браузера Chrome
    service = Service(PATH)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture()
def auth(browser):
    """
    фикстура для авторизации пользователя
    """
    auth = Locators(browser)
    return auth
