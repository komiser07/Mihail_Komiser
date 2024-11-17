import time

from selenium import webdriver
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
# команда для перемещения выбранного элемента - влево на 400 пикселей
actions.click_and_hold(slider).move_by_offset(-400, 0).release().perform()
slider_now = driver.find_element(By.XPATH, "//span[@style='font-weight:bold;color:red']")
value_slider_now = slider_now.text
print("Ползунок перемещён")
print(f"Value: {value_slider_now}")
# проверка что ползунок двигается и значение value изменяется
field = driver.find_element(By.XPATH,"//span[@id='f']")
value_field = field.text
print(f"Value: {value_field}")
assert value_field == value_slider_now
print("Info slider good")