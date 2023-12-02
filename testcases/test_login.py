import pytest
import pytest_html
from selenium import webdriver
from pageobjects.LoginPage import Loginpag
import os
from utilities.readproperties import Readconfig
from utilities.customlogger import LogGen


class Test_001_Login:

    baseURL= Readconfig.getapplicationurl()
    username=Readconfig.getuseremail()
    password=Readconfig.getpassword()

    logger=LogGen.loggen()

    def test_homepagetitle(self,setup):
        self.logger.info("**************Test_001_login*********")
        self.logger.info("******verifying home page title********")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("******verifying home page title pass title********")

        else:
            self.driver.save_screenshot("C:/Users/heman/PycharmProjects/pythonProject1/testcases")
            self.driver.close()
            self.logger.error("******verifying home page title fail title********")
            assert False


    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=Loginpag(self.driver)
        self.lp.setusername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        # self.lp.clicklogout()
        act_tit=self.driver.title
        if act_tit == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            # self.driver.save_screenshot("C:/Users/heman/PycharmProjects/pythonProject1/Screenshots")
            self.driver.close()
            assert False



    # def test_login(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.lp = Loginpag()
    #     self.lp.setuserName(self.username)
    #     self.lp.setPassword(self.password)  # Assuming you have separate methods for setting username and password
    #     self.lp.clicklogin()
    #     act_title = self.driver.title
    #     if act_title == "Dashboard / nopCommerce administration":
    #         assert True
    #         self.driver.close()
    #     else:
    #         self.driver.save_screenshot("C:/Users/heman/PycharmProjects/pythonProject1/Screenshots/screenshot.png")
    #         self.driver.close()
    #         assert False


