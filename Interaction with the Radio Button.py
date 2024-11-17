from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/radio-button'
driver.get(base_url)
driver.set_window_size(1920,1080)

# Находим элемент radio_button
radio_button = driver.find_element(By.XPATH , "(//label[@class='custom-control-label'])[1]")
# нажимаем по на выбранный элемент
radio_button.click()
# Проверка - выбран ли элемент
not radio_button.is_selected()
print("Radio Butten Active")
