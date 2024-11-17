import time
from os import times
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://the-internet.herokuapp.com/javascript_alerts'
driver.get(base_url)
driver.maximize_window()

# находим по локатору кнопку "Click for JS Alert" и нажимаем на неё
driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[1]/button").click()
print("Click for JS Alert")
time.sleep(2)
# подтверждаем наш Alert
driver.switch_to.alert.accept()

time.sleep(3)
# находим по локатору кнопку "Click for JS Confirm" и нажимаем на неё
driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[2]/button").click()
print("Click for JS Confirm")
time.sleep(2)
# нажимаем Отмена
driver.switch_to.alert.dismiss()

time.sleep(3)
# находим по локатору кнопку "Click for JS Prompt" и нажимаем на неё
driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[3]/button").click()
print("Click for JS Prompt")
time.sleep(2)
# вводим текст сообщения в поле и подтверждаем
driver.switch_to.alert.send_keys('Добрый день')
driver.switch_to.alert.accept()


