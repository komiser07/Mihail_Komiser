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
# Авторизация на сайте
user_name = driver.find_element(By.ID, 'user-name')
user_name.send_keys("standard_user")
print("Input Login")
password = driver.find_element(By.ID, 'password')
password.send_keys("secret_sauce")
print("Input Password")
button_login = driver.find_element(By.ID, 'login-button')
button_login.click()
print("Click Login Button")

product_1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH,  "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print("Select product 1")

product_2 = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']")
value_product_2 = product_2.text
print(value_product_2)

price_product_2 = driver.find_element(By.XPATH,  "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
value_price_product_2 = price_product_2.text
print(value_price_product_2)

select_product_2 = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']")
select_product_2.click()
print("Select product 2")

curt = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']")
curt.click()
print("Enter Cart")

# задержка в 1 секунду для визуального отслеживания
time.sleep(1)
# перемещение на страницу каталога (назад)
driver.back()
print("Go Back")

# задержка в 1 секунду для визуального отслеживания
time.sleep(1)
# перемещение на страницу корзины (вперёд)
driver.forward()
print("Go Forward")



