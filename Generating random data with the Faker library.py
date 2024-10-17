from faker import Faker
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

# указываем язык генерирования данных
fake = Faker("en_US")
# генерируем имя
name = fake.first_name()
# находим поле user_name по локатору
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
# вставляем в поле сгенерированное имя
user_name.send_keys(name)
print("Input Login")
