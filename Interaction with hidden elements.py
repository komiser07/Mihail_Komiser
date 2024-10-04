import time

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

user_name = driver.find_element(By.ID, "user-name")
user_name.send_keys("standard_user")
print("Input Login")

password = driver.find_element(By.ID, 'password')
password.send_keys("secret_sauce")
print("Input Password")

button_login = driver.find_element(By.ID, 'login-button').click()
print("Click Login Button")
# открываем скрытое меню по локатору
menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
print("Click Menu")
# ставим задержку времени на открытие скрытого меню
time.sleep(1)
# нажимаем на кнопку logaut по локатору, чтобы разлогиниться на сайте
logout_button = driver.find_element(By.ID, 'logout_sidebar_link').click()
print("Click Logout")

