from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from edge_selenium import options


# создаём класс для тестирования
class Test:
    # создаём метод для инициализации драйвера и открытия сайта
    def _initialize_browser(self):
        self.driver = webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))
        base_url = 'https://www.saucedemo.com/'
        self.driver.get(base_url)
        self.driver.maximize_window()

    # создаём метод для закрытия окна браузера
    def quit(self):
        self.driver.quit()
        print("Close Browser")

    # создаём метод для авторизации на сайте
    def __init__(self, username, password):
        self._initialize_browser()
        self._authorize(username, password)

    def _authorize(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        print("Input User Name")
        self.driver.find_element(By.ID, 'password').send_keys(password)
        print("Input Password")
        self.driver.find_element(By.ID, 'login-button').click()
        print("Click Login Button")


# создаём экземпляр класса и запускаем тест
start_test = Test('standard_user', 'secret_sauce')
start_test.quit()
