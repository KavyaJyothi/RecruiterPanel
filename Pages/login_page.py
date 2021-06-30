from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time
class LoginFlow(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    xpath_mobileNo = ("//input[@formcontrolname='mobile_no']","xpath")
    xpath_otp =( "//input[@formcontrolname='otp']","xpath")

    def enterMobileNo(self,mobile):
        self.sendKeys(mobile, self.xpath_mobileNo)
        self.pressEnter( self.xpath_mobileNo)
    def enterOTP(self,otp):
        self.sendKeys(otp,self.xpath_otp)
        
        self.pressEnter(self.xpath_otp)
        
    def login_flow(self,mobile, otp):
        self.enterMobileNo(mobile)      
        self.enterOTP(otp)
        


