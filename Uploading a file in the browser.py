from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.lambdatest.com/selenium-playground/upload-file-demo'
driver.get(base_url)
driver.maximize_window()

# прописываем в переменную путь до файла
path_upload = "D:\\Users\\komis\\PycharmProjects\\Selenium_python\\files_upload\\screenshot2024.10.03-16.27.02.png"

# находим локатор для кнопки "Выберите файл" и использум метод "send_keys"
click_button = driver.find_element(By.XPATH, "//*[@id='file']")

# используем метод "send_keys" для загрузки файла
click_button.send_keys(path_upload)
print("Файл успешно загружен")






















