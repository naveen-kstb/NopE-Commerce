import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_HomePageTitle(self, setup):

        self.logger.info("************Test_001_Login**************")
        self.logger.info("*************Verifying Home Page Title***********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.logger.info("*************Home Page Title is Passed***********")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_HomePageTitle.png" )
            self.logger.error("*************Home Page Title is Failed***********")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_Login(self, setup):
        self.logger.info("*************Verifying Login Test***********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("*************Login Test is Passed***********")
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.logger.error("*************Login Test is Failed***********")
            assert False
            self.driver.close()

