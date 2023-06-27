import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLutils

class Test_002_DDT_Login:
    baseUrl = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginDetails.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_Login(self, setup):
        self.logger.info("*************Test_002_DDT_Login*************")
        self.logger.info("*************Verifying Login DDT Test***********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.rows = XLutils.getRowCount(self.path,"Sheet1")
        print("Number of rowes in Excel:", self.rows)

        lst_status =[]
        for r in range(2, self.rows+1):
            self.user = XLutils.readData(self.path, "Sheet1", r, 1)
            self.password = XLutils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLutils.readData(self.path, "Sheet1", r, 3)


            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*******PASSED**********")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*******Failed**********")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*******Failed**********")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*******Passed**********")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("**** Login DDT Test Passed****")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** Login DDT Test Failed****")
            self.driver.close()
            assert False

        self.logger.info("***** End of LOgin DDT Test*****")
        self.logger.info("****** Completed Test_002_DDT_Login ****** ")



