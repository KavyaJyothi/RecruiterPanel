from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time
class LoginFlow(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    xpath_mobileNo = "//input[@formcontrolname='mobile_no']"
    xpath_otp = "//input[@formcontrolname='otp']"

    def enterMobileNo(self,mobile):
        self.sendKeys(mobile, self.xpath_mobileNo, locatorType='xpath')
        self.pressEnter( self.xpath_mobileNo, locatorType='xpath')
    def enterOTP(self,otp):
        self.sendKeys(otp,self.xpath_otp, locatorType='xpath')
        self.pressEnter(self.xpath_otp, locatorType='xpath')
    def loginFlow(self,mobile, otp):
        self.enterMobileNo(mobile)
        time.sleep(3)
        self.enterOTP(otp)
        time.sleep(2)

