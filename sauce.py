from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Test_Data import data
from Test_Locator import locator


class demo():

    def __init__(self,url):
        self.url= url
        self.driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    def login(self):
        self.driver.find_element(by=By.ID, value=locator.Locator().username).send_keys(data.Data().user)
        self.driver.find_element(by=By.ID, value=locator.Locator().password).send_keys(data.Data().pass_word)
        self.driver.find_element(by=By.ID,value=locator.Locator().login).click()
        print("login_successfully")
    def product(self):
        if self.driver.current_url == "https://www.saucedemo.com/inventory.html":
            product1= self.driver.find_element(by=By.ID, value=locator.Locator().prod_1)
            product1.click()
            product2= self.driver.find_element(by=By.ID, value=locator.Locator().prod_2)
            act = ActionChains(self.driver)
            act.click(on_element= product2).perform()
            print("successfully product added to the cart")
    def verify_two_in_cart(self):
        if self.driver.current_url == "https://www.saucedemo.com/inventory.html":
            val=self.driver.find_element(by=By.XPATH, value=locator.Locator().two).text
            print(val)
            if val == "2":
                print("two products in cart")
            else:
                print("can't validate")
            self.driver.find_element(by=By.XPATH, value=locator.Locator().two).click()
    def remove_item(self):
        if self.driver.current_url=="https://www.saucedemo.com/cart.html":
            self.driver.find_element(by=By.ID, value=locator.Locator().remove).click()
            print("one item removed from cart")

    def exist_item(self):
        if self.driver.current_url == "https://www.saucedemo.com/cart.html":
            item=self.driver.find_element(by=By.XPATH, value=locator.Locator().exist).text
            if item == "Sauce Labs Backpack":
                print("present item is "+item)

    def checkout(self):
        if self.driver.current_url == "https://www.saucedemo.com/cart.html":
            self.driver.find_element(by=By.ID, value=locator.Locator().check).click()
            print("checkout process")
    def checkout_info(self):
        if self.driver.current_url == "https://www.saucedemo.com/checkout-step-one.html":
            self.driver.find_element(by=By.ID, value=locator.Locator().firstname).send_keys(data.Data().first)
            self.driver.find_element(by=By.ID, value=locator.Locator().lastname).send_keys(data.Data().last)
            self.driver.find_element(by=By.ID, value=locator.Locator().zip).send_keys(data.Data().zipcode)
            self.driver.find_element(by=By.ID, value=locator.Locator().continue_button).click()
            print("Information filled: firstname:",data.Data().first +" lastname:",data.Data().last +" zip:",data.Data().zipcode)
    def overview(self):
        if self.driver.current_url == "https://www.saucedemo.com/checkout-step-two.html":
            self.driver.find_element(by=By.ID, value=locator.Locator().finish).click()
            print("Finish button clicked")

    def complete_screenshot(self):
        if self.driver.current_url == "https://www.saucedemo.com/checkout-complete.html":
            self.driver.get_screenshot_as_file("order_complete.png")
            print("screenshot taken")
            self.driver.find_element(by=By.ID, value=locator.Locator().back).click()
            if self.driver.current_url=="https://www.saucedemo.com/inventory.html":
                print("Back to products")

    def cancel(self):
        if self.driver.current_url == "https://www.saucedemo.com/checkout-step-two.html":
            self.driver.find_element(by=By.ID, value=locator.Locator().cancel).click()
            print("canceled order")

o=demo("https://www.saucedemo.com/")
o.login()
o.product()
o.verify_two_in_cart()
o.remove_item()
o.exist_item()
o.checkout()
o.checkout_info()
o.cancel()
#o.overview()
#o.complete_screenshot()
