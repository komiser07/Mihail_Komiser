import self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from edge_selenium import options, driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login_page import LoginPage

self.driver = webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))
self.driver.maximize_window()

# создаём класс для тестирования
class Test:

    # создаём конструктор для инициализации экземпляра теста с логином и паролем
    def __init__(self, login_name, login_password, base_url):
        self.driver = driver
        driver.get(base_url)
        self.login_name = login_name
        self.login_password = login_password
        self.run_test()

    # Добавляем модуль `login_page.py` с определением класса `LoginPage` и его методом `authorization()`.
    login = LoginPage(driver)
    login.authorization(self.login_name, self.login_password)

    # создаём метод для выбора товара
    def select_product(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']"))).click()
    print("Click Selected Product")

    # Переход на страницу Корзина
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
        self.select_product()
        self.cart_button()

    # Создаём метод для закрытия браузера
    def quit(self):
        self.driver.quit()
        print("Close Browser")


# создаём экземпляр класса и запускаем тест
start_test = Test('standard_user', 'secret_sauce', 'https://www.saucedemo.com/')
start_test.quit()
