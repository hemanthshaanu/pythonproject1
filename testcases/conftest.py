from selenium import webdriver
import pytest
import configparser
@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver



# @pytest.fixture()
# def setup(browser):
#     if browser=='chrome':
#         driver = webdriver.Chrome()
#     elif browser=='edge':
#         driver = webdriver.Edge()
#     return driver
#
# def pytest_adoption(parser):
#     parser.adoption("--browser")
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")