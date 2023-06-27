import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddCustomer:

    linkCustomer_menu_xpath = "//a[@href='#']//p[contains(text(), 'Customers')]"
    linkCustomer_menuitem_xpath = "(//a[@href='/Admin/Customer/List'])[1]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    textEmail_path = "//input[@id='Email']"
    textPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDOB_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    istaxExempt_check_xpath = "//input[@id='IsTaxExempt']"
    txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[normalize-space()='Guests']"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def ClickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.linkCustomer_menu_xpath).click()

    def ClickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.linkCustomer_menuitem_xpath).click()

    def ClickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.textEmail_path).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.textPassword_xpath).send_keys(password)

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def setGender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()

    def setDOB(self, dob):
        self.driver.find_element(By.XPATH, self.txtDOB_xpath).send_keys(dob)

    def setCompanyName(self, compname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(compname)

    def ClickOnCheckBox(self):
        self.driver.find_element(By.XPATH, self.istaxExempt_check_xpath).click()

    def setCustomerRole(self,role):
        self.driver.find_element(By.XPATH, self.txtcustomerRoles_xpath).click()
        time.sleep(5)
        if role =="Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        elif role == "Guests":
            time.sleep(5)
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)

        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)

        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self,value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setAdminContent(self,content):
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)

    def ClickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()