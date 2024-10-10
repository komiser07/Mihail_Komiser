import time
from datetime import datetime, timedelta

import days
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.set_window_size(1920,1080)

# создаём переменную и находим поле ввода даты
date_input = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")

# Имитируем нажатие клавиш Ctrl + 'a' и DELETE для выделения и очистки текста в поле
date_input.send_keys(Keys.CONTROL + 'a')
date_input.send_keys(Keys. DELETE)

# задержка в 1 секунду для визуального отслеживания
time.sleep(1)

# создаём дату, которая на 10 дней (+10 дней) позже текущей
current_date = datetime.now()
future_date = current_date + timedelta(days=10)
future_date_str = future_date.strftime("%d.%m.%Y")
date_input.send_keys(future_date_str)