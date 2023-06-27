import pytest
import time
from PageObjects.LoginPage import LoginPage
from PageObjects.AddCustomerPage import AddCustomer
from PageObjects.SearchCustomerPage import SearchCustomer
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from selenium.webdriver.common.by import By

class Test_005_SearchCustomerByName:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_serachCustomerByName(self, setup):
        self.logger.info("******** Test_005_SearchCustomerByName *********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******* Login Sucessful ********")

        self.logger.info("********** Starting Search Customer By Name ***********")
        self.addcust = AddCustomer(self.driver)
        self.addcust.ClickOnCustomersMenu()
        self.addcust.ClickOnCustomerMenuItem()

        self.logger.info("*********** Searching Customer By Name ***************")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Brenda")
        searchcust.setLastName("Lindgren")
        searchcust.clickOnSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName("Brenda Lindgren")
        self.driver.close()
        assert True == status
        self.logger.info("********** Test_005_SearchCustomerByName is Passed ***********")
