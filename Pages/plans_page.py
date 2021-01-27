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
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

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
    def enterPlansContactNo(self, mobile_no1):
        self.driver.switch_to.frame(self.driver.find_element_by_class_name("razorpay-checkout-frame"))
        self.log.info("switched to frame")
        self.sendKeys(mobile_no1,self.id_plans_contact_no, locatorType='id')
        self.elementClick(self.id_proceed, locatorType='id')
        time.sleep(2)
        self.elementClick(self.xpath_internet_banking, locatorType='xpath')
        time.sleep(2)
        self.elementClick(self.xpath_HDFC, locatorType='xpath')
        time.sleep(2)


    def switch_to_window(self):
        parent_handle=self.getParentWindowHandle()
        self.getAllWindowHandle(self.id_pay, locatorType='id')
        self.elementClick(self.xpath_success_button, locatorType='xpath')



        # before_window = self.driver.current_window_handle
        # self.log.info(before_window)
        #
        # self.elementClick(self.id_pay, locatorType='id')
        # time.sleep(4)
        # handles = self.driver.window_handles
        #
        # for handle in handles:
        #     self.log.info("inside for loop")
        #     if handle not in  before_window:
        #         self.log.info(handle)
        #         after_window = handle
        #         time.sleep(2)
        #         self.driver.switch_to.window(after_window)
        #
        #         self.log.info("switched window")
        #         self.elementClick(self.xpath_success_button, locatorType='xpath')
        #
        #         time.sleep(4)


        # self.switchWindow(self.xpath_success_button, loctorType='xpath')
        self.driver.switch_to.window(parent_handle)


