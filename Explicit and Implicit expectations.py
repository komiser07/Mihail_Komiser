import time

from faker import Faker
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options: Options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
# Открытие браузера в headless режиме
options.add_argument("--headless")

driver = webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

# авторизируемся на сайте
driver.find_element(By.ID, "user-name").send_keys('standard_user')
print("Input Login")
driver.find_element(By.ID, 'password').send_keys("secret_sauce")
print("Input Password")
driver.find_element(By.ID, 'login-button').click()
print("Click Login Button")

# список товаров
item_name = {
    1: "//*[@id='item_4_title_link']/div",
    2: "//*[@id='item_0_title_link']/div",
    3: "//*[@id='item_1_title_link']/div",
    4: "//*[@id='item_5_title_link']/div",
    5: "//*[@id='item_2_title_link']/div",
    6: "//*[@id='item_3_title_link']/div"
}
products = {
    1: "sauce-labs-backpack",
    2: "sauce-labs-bike-light",
    3: "sauce-labs-bolt-t-shirt",
    4: "sauce-labs-fleece-jacket",
    5: "sauce-labs-onesie",
    6: "test.allthethings()-t-shirt-(red)"
}
prices = {
    1: "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div",
    2: "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div",
    3: "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div",
    4: "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div",
    5: "//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div",
    6: "//*[@id='inventory_container']/div/div[6]/div[2]/div[2]/div"
}
choices = list(products.keys())

# Варианты выбора для пользователя
print("Приветствую тебя в нашем интернет - магазине")
print("Выбери один из следующих товаров и укажи его номер:")
for key in choices:
    print(f"{key}: {products[key]}")

# выбор товара пользователем
while True:
    choice = int(input("Выберите товар: "))
    if 1 <= choice <= 6:
        break
    else:
        print("Товар должен быть выбран из списка от 1 до 6.")
print(f"Выбранный товар: {products[choice]}")

# Находим выбранный товар
selected_button = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, f"add-to-cart-{products[choice]}")))
selected_button.click()
selected_product = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, f"{item_name[choice]}")))
value_selected_product = selected_product.text
print(value_selected_product)
selected_price = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, f"{prices[choice]}")))
value_selected_price = selected_price.text
print(value_selected_price)
time.sleep(5)
# Переход на страницу Корзина - нажатие на кнопку Curt
curt = driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']")
curt.click()
print("Enter Cart")

# Проверка товара в корзине
cart_product = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//*[@class='inventory_item_name']")))
value_cart_product = cart_product.text
print(value_cart_product)
assert value_selected_product == value_cart_product
print("Info Cart Product good")

# # Проверка цены товара в корзине
price_cart_product = WebDriverWait(driver, 20).until(EC.presence_of_element_located(
    (By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")))
value_cart_price_product = price_cart_product.text
print(value_cart_price_product)
assert value_selected_price == value_cart_price_product
print("Info Price Cart Product 1 good")

# Переход на страницу Информация о доставке
checkout = driver.find_element(By.XPATH, "//*[@id='checkout']")
checkout.click()
print("Click Checkout")

# генерация данных о покупателе
fake = Faker("en_US")

name_first = fake.first_name()
first_name = driver.find_element(By.XPATH, "//input[@class='input_error form_input']")
first_name.send_keys(name_first)
print("Input first_name")

name_last = fake.last_name()
last_name = driver.find_element(By.XPATH, "//*[@id='last-name']")
last_name.send_keys(name_last)
print(f"Input last_name")

zip = fake.postcode()
postal_code = driver.find_element(By.XPATH, "//*[@id='postal-code']")
postal_code.send_keys(zip)
print("Input postal_code")

# Переход на страницу оформления заказа - нажатие на кнопку Continue
driver.find_element(By.XPATH, "//*[@id='continue']").click()
print("Click Continue")

# Проверка товаров в оформлении заказа
finish_product = driver.find_element(By.XPATH, "//*[@class='inventory_item_name']")
value_finish_product = finish_product.text
print(value_finish_product)
assert value_selected_product == value_finish_product
print("Info Finish Product good")

# Проверка цен в оформлении заказа
price_finish_product = driver.find_element(By.XPATH,
                                           "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_finish_price_product = price_finish_product.text
print(value_finish_price_product)
assert value_selected_price == value_finish_price_product
print("Info Finish Price Product good")

summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
value_summary_price = summary_price.text
print(value_summary_price)
item_total = "Item total: " + value_finish_price_product
print(item_total)
assert value_summary_price == item_total
print("Total Summary Price good")

# Переход на страницу Ордер готов - нажатие на кнопку Finish
driver.find_element(By.XPATH, "//*[@id='finish']").click()
print("Enter Button Finish")

# Проверка что на странице есть сообщение: "Thank you for your order!"
checkout_complete = driver.find_element(By.XPATH, "//*[contains(text(), 'Thank you for your order!')]")
value_checkout_complete = checkout_complete.text
print(value_checkout_complete)
assert value_checkout_complete == 'Thank you for your order!'
print("Info Order Complete")
