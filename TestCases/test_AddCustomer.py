import pytest
import time
from PageObjects.LoginPage import LoginPage
from PageObjects.AddCustomerPage import AddCustomer
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from selenium.webdriver.common.by import By
import string
import random

class Test_003_AddCustomer:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("******** Test_003_AddCustomer********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******* Login Sucessful ********")

        self.logger.info("******* Starting AddCustomer Test******")

        self.addcust = AddCustomer(self.driver)
        self.addcust.ClickOnCustomersMenu()
        self.addcust.ClickOnCustomerMenuItem()
        self.addcust.ClickOnAddNew()

        self.logger.info("****** Providing Customer info *********")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test@123")
        self.addcust.setFirstName("Naveen")
        self.addcust.setLastName("Kumar")
        self.addcust.setGender("Male")
        self.addcust.setDOB("11/23/1995")
        self.addcust.setCompanyName("GenQALimited")
        self.addcust.ClickOnCheckBox()
        self.addcust.setCustomerRole("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setAdminContent("This is for Testing.......")
        self.addcust.ClickOnSave()
        time.sleep(10)
        self.logger.info("********* Saving Customer Info *********")

        self.logger.info("****** Add Customer Validation Started ********")

        self.msg = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissable']").text
        print(self.msg)

        if "The new customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("******** Add Customer Test is Passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_AddCustomer_scr.png")
            self.logger.info("****** Add Customer Test is Failed")
            assert True == False

        self.driver.close()
        self.logger.info("****** Ending Add Customer Test *******")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for x in range(size))

