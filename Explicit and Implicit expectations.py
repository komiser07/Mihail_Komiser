import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
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
    4: "sauce-labs-bleece-jacket",
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
selected_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, f"add-to-cart-{products[choice]}")))
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
cart_product = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='item_3_title_link']/div")))
value_cart_product = cart_product.text
print(value_cart_product)
assert selected_product == value_cart_product
print("Info Cart Product good")
#
# # Проверка цены товара в корзине
# price_cart_product_1 = driver.find_element(By.XPATH,"//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
# value_cart_price_product_1 = price_cart_product_1.text
# print(value_cart_price_product_1)
# assert selected_price == value_cart_price_product_1
# print("Info Price Cart Product 1 good")
#
#
#


# //*[@id="item_4_title_link"]/div
