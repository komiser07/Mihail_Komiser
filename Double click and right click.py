from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/buttons'
driver.get(base_url)
driver.set_window_size(1920,1080)

# Создаём экземпляр класса ActionChains
action = ActionChains(driver)
# создаём переменную и находим элемент Double Click Me
double_click_button = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
# вызываеи метод двойного клика
action.double_click(double_click_button).perform()
print("Произвели двойной клик")

# создаём переменную и находим элемент Double Click Me
right_click_button = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
# вызываем метод клика по правой кнопке мыши
action.context_click(right_click_button).perform()
print("Произвели клик по правой клавише")