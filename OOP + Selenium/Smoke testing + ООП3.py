from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from edge_selenium import options, driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# создаём класс для тестирования
class Test:

    # создаём конструктор для инициализации экземпляра теста с логином и паролем
    def __init__(self):
        self.driver = driver
        self.run_test()

    # создаем метод для инициализации браузера
    def initialize_browser(self):
        self.driver = webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))
        base_url = 'https://www.saucedemo.com/'
        self.driver.get(base_url)
        self.driver.maximize_window()

    # создаём метод для авторизации в системе
    def authorization(self):
        self.driver.find_element(By.ID, "user-name").send_keys('standard_user')
        print("Input User Name")
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        print("Input Password")
        self.driver.find_element(By.ID, 'login-button').click()
        print("Click Login Button")

    # создаём метод для выбора товара
    def select_product(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']"))).click()
        print("Click Selected Product")

    # создаём метод для перехода на страницу Корзина
    def cart_button(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']"))).click()
        print("Enter Shopping Cart")

        # Проверка что находится текст "Your Cart" на странице Корзина
        success_test = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))
        value_success_test = success_test.text
        assert value_success_test == 'Your Cart'
        print("Test Success")

    # запускаем тест
    def run_test(self):
        self.initialize_browser()
        self.authorization()
        self.select_product()
        self.cart_button()

    # Создаём метод для закрытия браузера
    def quit(self):
        self.driver.quit()
        print("Close Browser")


# создаём экземпляр класса и запускаем тест
start_test = Test()
start_test.quit()