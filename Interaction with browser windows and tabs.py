import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/browser-windows'
driver.get(base_url)
driver.maximize_window()

# находим по локатору элемент New Tab и делаем по нему клик
new_tab = driver.find_element(By.XPATH, "//*[@id='tabButton']")
new_tab.click()
print("Click Tab")
# переходим на 2 вкладку
driver.switch_to.window(driver.window_handles[1])
print("переключение на 2 вкладку")
time.sleep(2)
# переходим на 1 вкладку
driver.switch_to.window(driver.window_handles[0])

time.sleep(3)
# находим по локатору элемент New Window и делаем по нему клик
new_window = driver.find_element(By.XPATH, "//*[@id='windowButton']")
new_window.click()
print("Click  New Window")
# переходим на 2 окно
driver.switch_to.window(driver.window_handles[-1])
print("переключение на 2 окно")
time.sleep(4)
# закрываем 2 окно
driver.close()
# переходим на 1 окно
driver.switch_to.window(driver.window_handles[0])





