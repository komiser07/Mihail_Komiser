from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
# Находим элемент поля Username с идентификатором "user-name"
user_name = driver.find_element(By.ID, "user-name")
# помещаем текст "standard_user" в найденный элемент
user_name.send_keys('standard_user')
# Находим элемент поля Password с идентификатором "password"
password = driver.find_element(By.ID, 'password')
# помещаем текст "secret_sauce" в найденный элемент
password.send_keys("secret_sauce")
