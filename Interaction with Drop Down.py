import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://lambdatest.com/selenium-playground/jquery-dropdown-search-demo'
driver.get(base_url)
driver.set_window_size(1920,1080)

# открытие поля Dropdown по найденному локатору
click_drop = driver.find_element(By.XPATH, "//*[@id='__next']/div/section[2]/div/div/div/div[1]/div[2]/span/span[1]/span")
click_drop.click()
# input_country = driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input")
# input_country.send_keys('Hong Kong')
# input_country.send_keys(Keys.RETURN)
time.sleep(2)
# выбираем по локатору 5 значение 'Hong Kong'
select_contry = driver.find_element(By.XPATH, "//*[@id='select2-country-results']/li[5]")
select_contry.click()
print("Значение страны выбрано")








