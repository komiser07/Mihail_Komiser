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
base_url = 'https://html5css.ru/howto/howto_js_rangeslider.php'
driver.get(base_url)
driver.set_window_size(1920,1080)

# Создаём экземпляр класса для перемещения по окну браузера
actions = ActionChains(driver)
# Находим элемент на странице с указанием локатора
slider = driver.find_element(By.XPATH, "//input[@class='slider-color']")
# задержка в 2 секунды для визуального отслеживания
time.sleep(2)
# команда для перемещения выбранного элемента - влево на 500 пикселей
actions.click_and_hold(slider).move_by_offset(-500, 0).release().perform()
print("Ползунок перемещён")

