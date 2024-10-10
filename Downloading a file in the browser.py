import glob
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# директория хранения файлов
path_download = "D:\\Users\\komis\\PycharmProjects\\Selenium_python\\files_download\\"

options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : path_download}
options.add_experimental_option('prefs', prefs)
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.lambdatest.com/selenium-playground/download-file-demo'
driver.get(base_url)
driver.maximize_window()

# производим клик по кнопке скачивания файла
driver.find_element(By.XPATH, "//*[@id='__next']/div/section[2]/div/div/div/div/a/button").click()
time.sleep(3)
# проверка что файл скачался в нужную нам директорию
file_name = "LambdaTest.pdf"
file_path = path_download + file_name
assert os.access(file_path, os.F_OK) == True
print("Файл в директории")

# Проверка, что файл не пуст
files = glob.glob(os.path.join(path_download,"*.*"))
for file in files:
    a = os.path.getsize(file)
    if a > 10:
        print("Файл не пуст")
    else:
        print("Файл пуст")

# удаление скаченного файла из диерктории
files = glob.glob(os.path.join(path_download, "*.*"))
for file in files:
    os.remove(file)
    print("Файл удалён")













