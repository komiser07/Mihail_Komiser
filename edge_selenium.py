import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# Импортируем необходимые пакеты

options = webdriver.EdgeOptions()
# Создаем объект EdgeOptions для настройки браузера
options.add_experimental_option("detach", True)
# Включаем режим отсоединения окна браузера от консоли
driver = webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))
# Устанавливаем соединение с браузером Edge с использованием EdgeDriver
base_url = 'https://www.saucedemo.com/'
# Устанавливаем базовый URL для доступа к сайту
driver.get(base_url)
# Переходим на указанный URL
driver.maximize_window()
# Максимизируем окно браузера
time.sleep(3)
# Ждем 3 секунды перед закрытием окна браузера
driver.close()
# Закрываем окно браузера