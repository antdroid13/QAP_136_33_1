from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import URL


class BasePage:
    """
    Этот класс содержит общие методы, используемые на разных страницах.
    """

    def __init__(self, driver):
        """
        Конструктор класса BasePage.

        """
        self.driver = driver
        self.base_url = URL

    def go_to_site(self):
        """
        Переход на базовый URL веб-сайта.

        """
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        """
        Находит элемент на странице.

        :locator: кортеж с стратегией и значением локатора
        :time: максимальное время ожидания элемента (по умолчанию 10 секунд)
        """
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator), message=f"Не найден элемент по локатору {locator}"
        )

    def click_element(self, locator):
        """
        Нажимает на элемент, по локатору.

        :locator: кортеж с стратегией и значением локатора
        """
        self.find_element(locator).click()

    def input_data(self, locator, text):
        """
        Вводит заданный текст в поле ввода, по локатору.

        :locator: кортеж с стратегией и значением локатора
        :text: текст для ввода в поле ввода
        """
        self.find_element(locator).send_keys(text)

    def out(self, driver):
        return self.driver.switch_to.window(driver.window_handles[1])
