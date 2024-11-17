import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

user_name = driver.find_element(By.ID, "user-name")
user_name.send_keys('standard_user')
print('Input Login')

password = driver.find_element(By.ID, 'password')
password.send_keys("secret_sauce")
print('Input Password')

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
# button_login.click()
# print("Click Login Button")

time.sleep(3)
# Имитируем нажатие клавиш Ctrl + 'a' для выделения текста в поле user_name
user_name.send_keys(Keys.CONTROL + 'a')
# Имитируем нажатие клавиш DELETE для удаления текста в поле user_name
user_name.send_keys(Keys.DELETE)

# Имитируем нажатие клавиш Ctrl + 'a' для выделения текста в поле password
password.send_keys(Keys.CONTROL + 'a')
# Имитируем нажатие клавиш Ctrl + 'a' для выделения текста в поле password
password.send_keys(Keys.DELETE)

time.sleep(3)
# Имитируем нажатие клавиш ENTER на кнопку Login
button_login.send_keys(Keys.ENTER)