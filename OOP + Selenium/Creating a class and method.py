from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

# создаём класс для тестирования
class Test():
# создаём метод для авторизации
    def test_authoization(self):

        driver = webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()

        driver.find_element(By.ID, "user-name").send_keys('standard_user')
        print("Input Login")
        driver.find_element(By.ID, 'password').send_keys("secret_sauce")
        print("Input Password")
        driver.find_element(By.ID, 'login-button').click()
        print("Click Login Button")

# создаём экземпляр класса и запускаем тест
start_test = Test()
start_test.test_authoization()