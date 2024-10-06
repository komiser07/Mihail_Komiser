from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.lambdatest.com/selenium-playground/iframe-demo/'
driver.get(base_url)
driver.maximize_window()

# Находим нужный iframe на странице ипереключаемся на него с помощью метода .switch_to.frame
iframe = driver.find_element(By.XPATH, "//iframe[@id='iFrame1']")
driver.switch_to.frame(iframe)

# Находим по локатору поле текста
input_pole = driver.find_element(By.XPATH, "//*[@id='__next']/div/div[2]")
value_pole = input_pole.text
print(value_pole)
# выделяем текст
input_pole.send_keys(Keys.CONTROL + 'a')

# нажимаем на все кнопки изменения текста
click_editing_panel_bold = driver.find_element(By.XPATH, "//button[@title='Bold']").click()
click_editing_panel_italic = driver.find_element(By.XPATH, "//button[@title='Italic']").click()
click_editing_panel_align_center = driver.find_element(By.XPATH, "//button[@title='Align center']").click()
click_editing_panel_strike_through = driver.find_element(By.XPATH, "//button[@title='Strike through']").click()
click_editing_panel_underline = driver.find_element(By.XPATH, "//button[@title='Underline']").click()
print("Click editing panel")

# находим изменённый элемент
new_input_pole = driver.find_element(By.XPATH,"//*[@id='__next']/div/div[2]/div/b/i/u/strike")
value_input_pole = new_input_pole.text
print(value_input_pole)

# Сравнение строк - до изменения и после
assert  value_pole == value_input_pole
print("Редактирование успешно")





