from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login_page import LoginPage

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)


class Test():

    def test_select_product(self):
        driver = webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()

# Добавляем модуль `login_page.py` с определением класса `LoginPage` и его методом `authorization()`.
        login = LoginPage(driver)
        login.authorization(login_name='standard_user', login_password='secret_sauce')

        print("Start Test")

        # выбор товара
        WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']"))).click()
        print("Click Selected Product")
        # Переход на страницу Корзина
        WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']"))).click()
        print("Enter Shopping Cart")
        # Проверка что находится текст "Your Cart" на странице Корзина
        success_test = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))
        value_success_test = success_test.text
        assert value_success_test == 'Your Cart'
        print("Test Success")


# создаём экземпляр класса и запускаем тест
start_test = Test()
start_test.test_select_product()
