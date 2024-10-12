from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from edge_selenium import options


# создаём класс для тестирования
class Test:
    # создаём метод для инициализации драйвера и открытия сайта
    def __init__(self):
        self.driver = webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))
        self.base_url = 'https://www.saucedemo.com/'
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.driver.find_element(By.ID, "user-name").send_keys('standard_user')
        print("Input Login")
        self.driver.find_element(By.ID, 'password').send_keys("secret_sauce")
        print("Input Password")
        self.driver.find_element(By.ID, 'login-button').click()
        print("Click Login Button")

    # создаём метод для закрытия окна браузера
    def quit(self):
        self.driver.quit()


# создаём экземпляр класса и запускаем тест
start_test = Test()
start_test.quit()
