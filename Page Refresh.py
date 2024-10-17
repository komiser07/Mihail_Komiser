import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument("--headless")

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
# Вводится неверное имя пользователя для возникновения ошибки
user_name.send_keys('standard_u')
print("Inpyt Login")

password = driver.find_element(By.XPATH, "//input[@data-test='password']")
password.send_keys("secret_sauce")
print("Input Password")

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("Click Login Button")

# обновление страницы через 4 секунды
time.sleep(4)
driver.refresh()