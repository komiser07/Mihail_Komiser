# Импортируем библиотеку для работы с датой и временем
import datetime


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
user_name.send_keys('standard_user')
print("Input Login")
password = driver.find_element(By.ID, 'password')
password.send_keys("secret_sauce")
print("Input Password")
button_login = driver.find_element(By.ID, 'login-button')
button_login.click()
print("Click Login Button")
print(driver.current_url)
# Скриншот создаётся со временем создания (год, месяц, день, час, минута, секунда)
now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
# создаём уникальное имя скриншота с датой и форматом png
name_screenshot = 'screenshot' + now_date + '.png'
# Делаем скриншот страницы каталога и сохраняем в директорию screen
driver.save_screenshot('D:\\Users\\komis\\PycharmProjects\\Selenium_python\\screen\\' + name_screenshot)