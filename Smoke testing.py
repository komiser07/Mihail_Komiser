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
# Выбор товаров
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
# Переход на страницу Корзина - нажатие на кнопку Curt
curt = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']")
curt.click()
print("Enter Cart")
# Проверка товаров в корзине
cart_product_1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']")
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print("Info Cart Product 1 good")

cart_product_2 = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']")
value_cart_product_2 = cart_product_2.text
print(value_cart_product_2)
assert value_product_2 == value_cart_product_2
print("Info Cart Product 2 good")
# Проверка цен на товары в корзине
price_cart_product_1 = driver.find_element(By.XPATH,"//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_cart_price_product_1 = price_cart_product_1.text
print(value_cart_price_product_1)
assert value_price_product_1 == value_cart_price_product_1
print("Info Price Cart Product 1 good")

price_cart_product_2 = driver.find_element(By.XPATH,"//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_cart_price_product_2 = price_cart_product_2.text
print(value_cart_price_product_2)
assert value_price_product_2 == value_cart_price_product_2
print("Info Price Cart Product 2 good")
# Переход на страницу Информация о доставке
checkout = driver.find_element(By.XPATH, "//*[@id='checkout']")
checkout.click()
print("Click Checkout")
# Ввод информации о доставке
first_name = driver.find_element(By.XPATH, "//*[@id='first-name']")
first_name.send_keys("Roman")
print("Input First Name")

last_name = driver.find_element(By.XPATH, "//*[@id='last-name']")
last_name.send_keys("Romanov")
print("Input Last Name")

postal_code = driver.find_element(By.XPATH, "//*[@id='postal-code']")
postal_code.send_keys(4002)
print("Input Postal Code")
# Переход на страницу оформления заказа - нажатие на кнопку Continue
button_continue =driver.find_element(By.XPATH, "//*[@id='continue']")
button_continue.click()
print("Click Continue")
# Проверка товаров в оформлении заказа
finish_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1
print('Info Finish Product 1 good')

finish_product_2 = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
value_finish_product_2 = finish_product_2.text
print(value_finish_product_2)
assert value_product_2 == value_finish_product_2
print('Info Finish Product 2 good')
# Проверка цен в оформлении заказа
price_finish_product_1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_finish_price_product_1 = price_finish_product_1.text
print(value_finish_price_product_1)
assert value_price_product_1 == value_finish_price_product_1
print('Info Finish Price Product 1 good')

price_finish_product_2 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_finish_price_product_2 = price_finish_product_2.text
print(value_finish_price_product_1)
assert value_price_product_2 == value_finish_price_product_2
print('Info Finish Price Product 2 good')
# Удаление символа "$" из цены
value_finish_price_product_1 = value_finish_price_product_1.replace("$", "")

value_finish_price_product_2 = value_finish_price_product_2.replace("$", "")
# Сумма цен обоих товаров
total_sum = float(value_finish_price_product_1) + float(value_finish_price_product_2)
# Округление суммы до двух знаков после запятой
total_sum = round(total_sum, 2)
print(f"Total sum: ${total_sum}")
# Проверка что сумма обоих товаров соответствует тому, что отображается в Item_total
summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
value_summary_price = summary_price.text
print(value_summary_price)
item_total = f"Item total: ${total_sum}"
print(item_total)
assert value_summary_price == item_total
print('Total Summary Price good')
# Переход на страницу Ордер готов - нажатие на кнопку Finish
button_finish = driver.find_element(By.XPATH, "//*[@id='finish']")
button_finish.click()
print("Enter Button Finish")
# Проверка что на страницу ест сообщение: "Thank you for your order!"
checkout_complete = driver.find_element(By.XPATH, "//*[contains(text(), 'Thank you for your order!')]")
value_checkout_complete = checkout_complete.text
print(value_checkout_complete)
assert value_checkout_complete == 'Thank you for your order!'
print('Info Order Complete')







