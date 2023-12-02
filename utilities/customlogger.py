# import logging
# class LogGen:
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename="C:\\Users\\heman\\PycharmProjects\\pythonProject1\\Logs/automation.log",
#                             format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
#         Logger=logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger
# import time
# import requests as requests
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
# from selenium.webdriver import ActionChains
# from selenium.webdriver import Keys
# import os
# import openpyxl
import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\logs\\automstion.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
    # r"C:\Users\heman\PycharmProjects\pythonProject1\Logs\automstion.log"