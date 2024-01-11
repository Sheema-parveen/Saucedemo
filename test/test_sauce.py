from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Test_Data import data
from Test_Locator import locator
import pytest


class Test_demo():
    @pytest.fixture
    def startup(self):
        self.driver= webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close()
    def test_login(self,startup):
        self.driver.get(locator.Locator().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.ID, value=locator.Locator().username).send_keys(data.Data().user)
        self.driver.find_element(by=By.ID, value=locator.Locator().password).send_keys(data.Data().pass_word)
        self.driver.find_element(by=By.ID,value=locator.Locator().login).click()
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"
        print("login successfully")

    def test_product(self,startup):
        self.driver.get(locator.Locator().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        if self.driver.current_url == "https://www.saucedemo.com/inventory.html":
            product1= self.driver.find_element(by=By.ID, value=locator.Locator().prod_1)
            product1.click()
            product2= self.driver.find_element(by=By.ID, value=locator.Locator().prod_2)
            act = ActionChains(self.driver)
            assert act.click(on_element= product2).perform()
            print("successfully product added to the cart")
    def test_verify_two_in_cart(self,startup):
        self.driver.get(locator.Locator().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        if self.driver.current_url == "https://www.saucedemo.com/inventory.html":
            val=self.driver.find_element(by=By.XPATH, value=locator.Locator().two).text
            print(val)
            assert val == "2"
            print("two products in cart")
            self.driver.find_element(by=By.XPATH, value=locator.Locator().two).click()
    def test_remove_item(self,startup):
        self.driver.get(locator.Locator().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        if self.driver.current_url=="https://www.saucedemo.com/cart.html":
            assert self.driver.find_element(by=By.ID, value=locator.Locator().remove).click()
            print("one item removed from cart")

    def test_exist_item(self,startup):
        self.driver.get(locator.Locator().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        if self.driver.current_url == "https://www.saucedemo.com/cart.html":
            item=self.driver.find_element(by=By.XPATH, value=locator.Locator().exist).text
            assert item == "Sauce Labs Backpack"
            print("present item is "+item)

    def test_checkout(self,startup):
        self.driver.get(locator.Locator().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        if self.driver.current_url == "https://www.saucedemo.com/cart.html":
            assert self.driver.find_element(by=By.ID, value=locator.Locator().check).click()
            print("checkout process")
    def test_checkout_info(self,startup):
        self.driver.get(locator.Locator().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        if self.driver.current_url == "https://www.saucedemo.com/checkout-step-one.html":
            self.driver.find_element(by=By.ID, value=locator.Locator().firstname).send_keys(data.Data().first)
            self.driver.find_element(by=By.ID, value=locator.Locator().lastname).send_keys(data.Data().last)
            self.driver.find_element(by=By.ID, value=locator.Locator().zip).send_keys(data.Data().zipcode)
            assert self.driver.find_element(by=By.ID, value=locator.Locator().continue_button).click()
            print("Information filled: firstname:",data.Data().first +" lastname:",data.Data().last +" zip:",data.Data().zipcode)
    def test_overview(self,startup):
        self.driver.get(locator.Locator().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        if self.driver.current_url == "https://www.saucedemo.com/checkout-step-two.html":
            assert self.driver.find_element(by=By.ID, value=locator.Locator().finish).click()
            print("Finish button clicked")

    def test_complete_screenshot(self,startup):
        self.driver.get(locator.Locator().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        if self.driver.current_url == "https://www.saucedemo.com/checkout-complete.html":
            self.driver.get_screenshot_as_file("order_complete.png")
            print("screenshot taken")
            self.driver.find_element(by=By.ID, value=locator.Locator().back).click()
            assert self.driver.current_url=="https://www.saucedemo.com/inventory.html"
            print("Back to products")

    def test_cancel(self,startup):
        self.driver.get(locator.Locator().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.saucedemo.com/checkout-step-two.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        if self.driver.current_url == "https://www.saucedemo.com/checkout-step-two.html":
            assert self.driver.find_element(by=By.ID, value=locator.Locator().cancel).click()
            print("canceled order")


