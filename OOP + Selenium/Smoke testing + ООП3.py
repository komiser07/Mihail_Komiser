from selenium import webdriver
from login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup_driver():
    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.maximize_window()
    return driver


# создаём класс для тестирования
class Test:

    # создаём конструктор для инициализации экземпляра теста с логином и паролем
    def __init__(self, login_name, login_password, base_url):
        self.driver = setup_driver()
        self.base_url = base_url
        self.driver.get(self.base_url)
        self.login_name = login_name
        self.login_password = login_password
        self.login = LoginPage(self.driver)
        self.run_test()

    # создаём метод для выбора товара и перехода на страницу Корзина
    def select_product(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']"))).click()
        print("Click Selected Product")
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']"))).click()
        print("Enter Shopping Cart")

    def checking_cart(self):
        success_test = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))
        value_success_test = success_test.text
        assert value_success_test == 'Your Cart'
        print("Test Success")

    # запускаем тест
    def run_test(self):
        self.login.authorization(self.login_name, self.login_password)
        self.select_product()
        self.checking_cart()

    # Создаём метод для закрытия браузера
    def quit(self):
        self.driver.quit()
        print("Close Browser")


# создаём экземпляр класса и запускаем тест
start_test = Test('standard_user', 'secret_sauce', 'https://www.saucedemo.com/')
start_test.quit()
