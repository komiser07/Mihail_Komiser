from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless")

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
user_name = driver.find_element(By.ID, "user-name")
user_name.send_keys('standard_user')
print("Inpyt Login")
password = driver.find_element(By.ID, 'password')
# вводится неверный пароль
password.send_keys("secret_s")
print("Input Password")
button_login = driver.find_element(By.ID, 'login-button')
button_login.click()
print("Click Login Button")

# проверку, что текст ошибки авторизации отображается
warning_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warning_text = warning_text.text
# проверка на текст ошибки, который возникает при неправильном введение логина или пароля
assert value_warning_text == 'Epic sadface: Username and password do not match any user in this service'
print("Сообщение корректно")

# Кликнуть на элемент закрытия ошибки авторизации
error_button = driver.find_element(By.XPATH, "//button[@class='error-button']")
error_button.click()
print("Click Error Buton")
