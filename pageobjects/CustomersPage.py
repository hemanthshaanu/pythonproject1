from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class Customers:
    linkcustomers_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    linkcustomers_menuitem_xpath="//a[@href='/Admin/Customer/List']"
    addnew_xpath="//a[@class='btn btn-primary']"
    txt_Email_id="Email"
    txt_Password_id="Password"
    txt_First_name_id="FirstName"
    txt_Last_name_id="LastName"
    rd_Malegender_id="Gender_Male"
    rd_Femalegender_id = "Gender_Female"
    txt_cale_dob_id="DateOfBirth"
    txt_companyname_id="Company"
    checkbox_istaxattempt_id="IsTaxExempt"
    text_newsletter_xpath="//div[@role='listbox']"
    text_newsletter_xpath_ist="//ul[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[@data-offset-index='0']"
    news_letter_dropdown_xpath="//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div"
    customerroles_dropdown_xpath="//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    managerofwindow_dropdown_id="VendorId"
    checkbox_active_xpath="//*[@id='Active']"
    save_xpath="//*[@name='save']/i"

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def Clickoncuctumermenu(self):
        self.driver.find_element("xpath",self.linkcustomers_menu_xpath).click()

    def Clickoncuctumermenuitem(self):
        self.driver.find_element("xpath", self. linkcustomers_menuitem_xpath).click()

    def Clickonaddnew(self):
        self.driver.find_element("xpath", self. addnew_xpath).click()

    def Setemailid(self,email):
        self.driver.find_element("id", self.txt_Email_id).send_keys(email)

    def Setpassword(self,password):
        self.driver.find_element("id", self. txt_Password_id).send_keys(password)

    def Setfirstname(self,firstname):
        self.driver.find_element("id", self.txt_First_name_id).send_keys(firstname)

    def Setlastname(self,lastname):
        self.driver.find_element("id", self. txt_Last_name_id).send_keys(lastname)

    def Selectgende(self):
        self.driver.find_element("id", self.rd_Malegender_id).clich()
    def SetDOB(self, DOB):
        self.driver.find_element("id", self.txt_cale_dob_id).send_keys(DOB)

    def Setcompanyname(self,comname):
        self.driver.find_element("id",self.txt_companyname_id).send_keys(comname)
    def Setnewsletter(self):
        self.driver.find_element("xpath",self.text_newsletter_xpath).click()
        self.driver.find_element("xpath",self. text_newsletter_xpath_ist).click()

    def Selectsave(self):
        self.driver.find_element("xpath",self. save_xpath).click()







