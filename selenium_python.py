# Импортируем необходимые библиотеки и модули
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()  # Создаем объект ChromeOptions для настройки браузера
options.add_experimental_option("detach", True)  # Включаем режим отсоединения окна браузера от консоли
# Устанавливаем соединение с браузером Chrome с использованием ChromeDriver
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'  # Устанавливаем базовый URL для доступа к сайту
driver.get(base_url) # Переходим на указанный URL
driver.maximize_window() # Максимизируем окно браузера
