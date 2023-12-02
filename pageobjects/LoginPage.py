from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class Loginpag:
    textbox_username_xpath = "//input[@id='Email']"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@type='submit']"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)


    def setusername(self, username):
        self.driver.find_element("xpath",self.textbox_username_xpath).clear()
        self.driver.find_element("xpath",self.textbox_username_xpath).send_keys(username)


    def setPassword(self, password):
        self.driver.find_element("id",self.textbox_password_id).clear()
        self.driver.find_element("id",self.textbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element("xpath",self.button_login_xpath).click()

    def clicklogout(self):
        #self.driver.find_element("link_text",self.link_logout_linktext).click()
        logout_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.link_logout_linktext)))
        logout_link.click()

# class Login_pag:
#     textbox_username_id = "Email"
#     textbox_password_id = "Password"
#     button_login_xpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
#     link_logout_linktext = "Logout"
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def setuser_Name(self, username):
#         username_element = self.driver.find_element_by_id(self.textbox_username_id)
#         username_element.clear()
#         username_element.send_keys(username)

#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class LoginPage:
#     textbox_username_xpath = "//input[@id='Email']"
#     textbox_password_id = "Password"
#     button_login_xpath = "//button[@id='Login']"  # Update with correct login button XPath
#     link_logout_linktext = "Logout"
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.driver.implicitly_wait(10)
#         self.wait = WebDriverWait(self.driver, 10)
#
#     def set_username(self, username):
#         username_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.textbox_username_xpath)))
#         username_field.clear()
#         username_field.send_keys(username)
#
#     def set_password(self, password):
#         password_field = self.wait.until(EC.presence_of_element_located((By.ID, self.textbox_password_id)))
#         password_field.clear()
#         password_field.send_keys(password)
#
#     def click_login(self):
#         login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_login_xpath)))
#         login_button.click()
#
#     def click_logout(self):
#         logout_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.link_logout_linktext)))
#         logout_link.click()


