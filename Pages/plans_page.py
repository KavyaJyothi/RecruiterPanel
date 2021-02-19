from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time
class PlansPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    xpath_mobileNo="//input[@formcontrolname='mobile_no']"
    xpath_otp="//input[@formcontrolname='otp']"
    xpath_plans="//span[@class='menu-title' and contains(text(),'Plans')]"
    xpath_BuyNow="(//button[contains(text(),'BUY NOW')])[1]"
    id_plans_contact_no="contact"
    id_proceed='footer-cta'
    xpath_internet_banking="//div[@class='svelte-13rsokc']/div[@slot='title' and contains(text(),'Netbanking')]"
    xpath_HDFC="//div[@class='mchild item-inner svelte-xjs2xa']/div[contains(text(),'HDFC')]"
    id_pay="footer"
    xpath_success_button="//button[@class='success' and contains(text(),'Success')]"
    ######################## GST Details Popup ######################################
    id_gst_field="gst"
    xpath_check="//nb-checkbox/label/span[2]"
    id_state="state"
    id_address_field="address"
    id_email_field="email"


    def printCookies(self):
        c=self.getCookies()
        print(c)
    def enterMobileNo(self,mobile):
        self.sendKeys(mobile, self.xpath_mobileNo, locatorType='xpath')
        self.pressEnter( self.xpath_mobileNo, locatorType='xpath')
    def enterOTP(self,otp):
        self.sendKeys(otp,self.xpath_otp, locatorType='xpath')
        self.pressEnter(self.xpath_otp, locatorType='xpath')

    def clickPlansIcon(self):
        self.elementClick(self.xpath_plans, locatorType='xpath')
    def clickBuyNow(self):
        self.elementClick(self.xpath_BuyNow, locatorType='xpath')
    def enterPlansContactNo(self, mobile_no1,email):
        self.driver.switch_to.frame(self.driver.find_element_by_class_name("razorpay-checkout-frame"))
        self.log.info("switched to frame")
        self.sendKeys(mobile_no1,self.id_plans_contact_no)
        time.sleep(3)
        self.clearField(self.id_email_field)
        time.sleep(2)
        self.sendKeys(email, self.id_email_field)
        self.elementClick(self.id_proceed, locatorType='id')
        time.sleep(2)
        self.elementClick(self.xpath_internet_banking, locatorType='xpath')
        time.sleep(2)
        self.elementClick(self.xpath_HDFC, locatorType='xpath')
        time.sleep(2)
        self.screenShot("payment window")

    def switch_to_window(self):
        parent_handle=self.getParentWindowHandle()
        self.getAllWindowHandle(self.id_pay, locatorType='id')
        self.screenShot("razor pay popup")
        self.elementClick(self.xpath_success_button, locatorType='xpath')
        self.driver.switch_to.window(parent_handle)
        time.sleep(2)
        self.screenShot("payment successful popup")
        time.sleep(2)
    def enter_GST_Details(self,gst_no,address, email):
        self.sendKeys(gst_no, self.id_gst_field)
        time.sleep(7)
        # self.elementClick(self.xpath_check, locatorType="xpath")
        # time.sleep(2)
        # self.sendKeys("karnataka",self.id_state)
        # time.sleep(2)
        self.sendKeys(address, self.id_address_field)
        time.sleep(3)
        self.sendKeys(email, self.id_email_field)
        time.sleep(3)
        self.screenShot("GST details")

    def login(self, mobile_no, otp):
        time.sleep(2)
        self.enterMobileNo(mobile_no)
        time.sleep(2)
        self.enterOTP(otp)
    def navigate_to_buy_plan(self, mobile_no, email):
        time.sleep(2)
        self.clickPlansIcon()
        time.sleep(2)
        self.clickBuyNow()
        time.sleep(2)
        self.enterPlansContactNo(mobile_no, email)
        self.switch_to_window()

