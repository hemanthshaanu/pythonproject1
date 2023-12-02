import time

import pytest
import pytest_html
from selenium import webdriver
from pageobjects.LoginPage import Loginpag
from pageobjects.CustomersPage import Customers
import os
from utilities.readproperties import Readconfig
from utilities.customlogger import LogGen

class Test_003_Addcustomer:
    baseURL = Readconfig.getapplicationurl()
    username = Readconfig.getuseremail()
    password = Readconfig.getpassword()
    logger = LogGen.loggen()
    def test_addcustomer(self,setup):
        self.logger.info("**************Test_001_login*********")
        self.logger.info("******verifying home page title********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Loginpag(self.driver)
        self.lp.setusername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        self.cus= Customers(self.driver)
        self.cus.Clickoncuctumermenu()
        self.cus.Clickoncuctumermenuitem()
        self.cus.Clickonaddnew()
        time.sleep(5)
        self.cus.Setemailid("heasdr@gmail.com")
        self.cus.Setpassword("123qwe")
        self.cus.Setfirstname("Hemanth")
        self.cus.Setlastname("sg")
        self.cus.SetDOB("02/11/1996")
        self.cus.Setnewsletter()
        self.cus.Selectsave()
        time.sleep(10)



