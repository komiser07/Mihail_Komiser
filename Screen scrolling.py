from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# имортируем класс ActionChains
from selenium.webdriver.common.action_chains import ActionChains


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

user_name = driver.find_element(By.ID, "user-name")
user_name.send_keys('standard_user')
print("Input Login")

password = driver.find_element(By.ID, 'password')
password.send_keys("secret_sauce")
print("Input Password")

button_login = driver.find_element(By.ID, 'login-button')
button_login.click()
print("Click Login Button")
# Добавляем все товары в корзину
button_add_backpack = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
button_add_bike = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
button_add_t_shirt = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
button_add_jacket = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
button_add_onesie = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']").click()
button_add_t_shirt_red = driver.find_element(By.XPATH,"//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']").click()
# Переходим в корзину
button_cart_link = driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']").click()
# Создаём экземпляр класса для перемещения по окну браузера
actions = ActionChains(driver)
# поиск на странце по локатору
element = driver.find_element(By.ID, 'checkout')
# наводимся на требуемый объект страницы по локатору используя метод move_to_element
actions.move_to_element(element).perform()
