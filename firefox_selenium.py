# Импортируем необходимые библиотеки и модули
import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# Устанавливаем соединение с браузером Firefox с использованием Geckodriver
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
# Устанавливаем базовый URL для доступа к сайту
base_url = 'https://www.saucedemo.com/'
# Переходим на указанный URL
driver.get(base_url)
# Максимизируем окно браузера
driver.maximize_window()
# Ждем 3 секунды перед закрытием окна браузера
time.sleep(3)
# Закрываем окно браузера
driver.close()
