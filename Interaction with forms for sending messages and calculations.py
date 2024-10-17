import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://lambdatest.com/selenium-playground/simple-form-demo'
driver.get(base_url)
driver.set_window_size(1920,1080)

# создаём переменные и производим их сложение
first_value = 357
second_value = 159
sum_result = first_value + second_value
print(sum_result)

# заполняем найденные по локатору поля числовыми значениями и нажимаем Get Sum
input_first_value = driver.find_element(By.XPATH, "//*[@id='sum1']")
input_first_value.send_keys(first_value)
input_second_value = driver.find_element(By.XPATH, "//*[@id='sum2']")
input_second_value.send_keys(second_value)
click_button = driver.find_element(By.XPATH, "//*[@id='gettotal']/button")
click_button.click()

time.sleep(2)

# Сравнение суммы двух чисел и значения которое выдала нам система
result = driver.find_element(By.XPATH, "//*[@id='addmessage']")
value_result = result.text
print(value_result)
assert value_result == str(sum_result)
print("Значения верны")
















