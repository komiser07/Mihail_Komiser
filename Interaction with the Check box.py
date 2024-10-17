from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/checkbox'
driver.get(base_url)
driver.set_window_size(1920,1080)

# Находим элемент check_box
check_box = driver.find_element(By.XPATH, "//span[@class='rct-checkbox']")
# нажимаем по check_box
check_box.click()
# Проверка - выбран ли элемент
check_box.is_selected()
print("Чек-бокс выбран")







