import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)
driver.maximize_window()

# в блоке try пробуем найти нужную нам кнопку и нажать на неё и получаем ошибку NoSuchElementException
try:
    driver.find_element(By.XPATH, "//*[@id='visibleAfter']").click()
# указываем ожидаемое исключение
except NoSuchElementException:
    print("получили NoSuchElementException")
# прописываем метод который нажмёт на кнопку  "Visible After 5 Seconds"
    time.sleep(3)
    driver.refresh()
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@id='visibleAfter']").click()
    print("Visible After 5 Seconds")











