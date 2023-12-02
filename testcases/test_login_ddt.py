import time

import pytest
import pytest_html
from selenium import webdriver
from pageobjects.LoginPage import Loginpag
from utilities import xlutility
import os
from utilities.readproperties import Readconfig
from utilities.customlogger import LogGen


class Test_002_DDT_Login:

    baseURL= Readconfig.getapplicationurl()
    path=".//Testdata/LoginData.xlsx"
    logger=LogGen.loggen()


    def test_login_ddt(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=Loginpag(self.driver)

        self.rows=xlutility.getRowCount(self.path,'Sheet1')

        print("numbrr of rows in excel", self.rows)
        # lst status=[] # empty test variable
        for r in range(2, self.rows):   ##### 2 means 2 nd column because started from 2nd 1st row is discription
            print("numbrr of rows ", r)
            self.user = xlutility.readData(self.path,'Sheet1', r, 1)
            print("numbrr of rows ", self.user)
            self.password = xlutility.readData(self.path,'Sheet1', r, 2)
            self.exp = xlutility.readData(self.path,'Sheet1', r, 3)
            self.lp.setusername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clicklogin()
            time.sleep(5)
            # self.lp.clicklogout()
            act_tit = self.driver.title
            exp_tit = "Dashboard / nopCommerce administration"
            print(self.rows)
            if act_tit==exp_tit:
                if self.exp=="Pass":
                    self.lp.clicklogout();
                    print("pass")
                elif self.exp=="Fail":
                    self.lp.clicklogout();
                    print("fail")
            elif act_tit!=exp_tit:
                if self.exp=="Pass":
                    print("pass")
                elif self.exp=="Fail":
                    print("fail")


# class Test_002_DDT_Login:
#     baseURL = Readconfig.getapplicationurl()
#
#     path=".//Testdata/LoginData.xlsx"
#     logger=LogGen.loggen()
#     # (other class attributes remain the same)
#
#     def test_login_ddt(self, setup):
#         self.driver = setup
#         self.driver.get(self.baseURL)
#         self.lp = Loginpag(self.driver)
#
#         self.rows = xlutility.getRowCount(self.path, 'Sheet1')
#         print("number of rows in Excel:", self.rows)
#
#         for r in range(2, self.rows + 1):
#             self.user = xlutility.readData(self.path, 'Sheet1', r, 1)
#             self.password = xlutility.readData(self.path, 'Sheet1', r, 2)
#             self.exp = xlutility.readData(self.path, 'Sheet1', r, 3)
#             self.lp.setusername(self.user)
#             self.lp.setPassword(self.password)
#             self.lp.clicklogin()
#             time.sleep(5)
#
#             act_tit = self.driver.title
#             exp_tit = "Dashboard / nopCommerce administration"
#
#             if act_tit == exp_tit:
#                 if self.exp == "Pass":
#                     self.lp.clicklogout()
#                     print(f"Test passed for user: {self.user}")
#                 elif self.exp == "Fail":
#                     self.lp.clicklogout()
#                     print(f"Test failed for user: {self.user}")
#             else:
#                 if self.exp == "Pass":
#                     print(f"Test failed for user: {self.user}")
#                 elif self.exp == "Fail":
#                     print(f"Test passed for user: {self.user}")``
#




