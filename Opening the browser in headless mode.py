from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# Открытие браузера в headless режиме
options.add_argument("--headless")

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920, 1080)
user_name = driver.find_element(By.ID, "user-name")
user_name.send_keys('standard_user')
print("Inpyt Login")
password = driver.find_element(By.ID, 'password')
password.send_keys("secret_sauce")
print("Input Password")
button_login = driver.find_element(By.ID, 'login-button')
button_login.click()
print("Click Login Button")
print(driver.current_url)

# Проверка на корректность URL
get_url = driver.current_url
# Вывод фактического URL
url = 'https://www.saucedemo.com/inventory.html'
# Сравнение ожидаемого результата и фактического
assert url == get_url
# вывод сообщение что проверка удачна
print("URL корректен")

# Проверка что заголовок на странице каталога совпадает с ожидаемым результатом
text_products = driver.find_element(By.XPATH, "//span[@class='title']")
# Вывод текста заголовка по локатору
print(text_products.text)
value_text_products = text_products.text
# Проверка что заголовок соответствует слову "Products"
assert value_text_products == 'Products'
# вывод сообщение что проверка удачна
print("Заголовок корректен")