import pytest
import time
from PageObjects.LoginPage import LoginPage
from PageObjects.AddCustomerPage import AddCustomer
from PageObjects.SearchCustomerPage import SearchCustomer
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from selenium.webdriver.common.by import By

class Test_004_SearchCustomerByEmail:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_serachCustomerByEmail(self, setup):
        self.logger.info("******** Test_004_SearchCustomerByEmail *********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******* Login Sucessful ********")

        self.logger.info("********** Starting Search Customer By Email ***********")
        self.addcust = AddCustomer(self.driver)
        self.addcust.ClickOnCustomersMenu()
        self.addcust.ClickOnCustomerMenuItem()


        self.logger.info("*********** Searching Customer By EmailID ***************")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("brenda_lindgren@nopCommerce.com")
        searchcust.clickOnSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByEmail("brenda_lindgren@nopCommerce.com")
        self.driver.close()
        assert True == status
        self.logger.info("********** Test_004_SearchCustomerByEmail is Passed ***********")
