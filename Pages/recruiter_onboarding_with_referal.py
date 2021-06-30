from base.selenium_driver import SeleniumDriver
import time
import utilities.custom_logger as cl
from Pages.job_posting_flow_page import JobPostingFlow
import logging
class RecruiterOnboardReferal(JobPostingFlow):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver


    xpath_mob_no_field = "//input[@formcontrolname='mobile_no']"
    xpath_otp_field = "//input[@formcontrolname='otp']"
    xpath_email_selection = "//input[@id='identifierId']"
    xpath_nxt_btn = "//*[@id='identifierNext']/div/button/div[2]"
    xpath_email_password_field = "//input[@type='password']"
    xpath_password_nxt_btn = "//div[@id='passwordNext']/div/button/div[2]"
    xpath_location="//ngx-location/input"
    xpath_select_location="//nb-card/nb-list/nb-list-item[1]/div[1]/b"
    xpath_company_field="//div/input[@role='combobox']"
    xpath_select_company="//ng-dropdown-panel/div/div/div[1]"
    xpath_designation_field="//ng-select/div/div/div[2]/input"
    xpath_select_designation="//ng-dropdown-panel/div/div/div[1]"
    xpath_referal_link="//a[@class='ng-star-inserted' and contains(text(),'I have a Referral Code')]"
    xpath_referal_field="//input[@formcontrolname='referral_code']"
    xpath_continue_button="//button[contains(text(),'Continue')]"
    xpath_toast="//nb-toast[@class='title subtitle']"
    xpath_referal_success_msg="//div/small[@class='refcode-label']"
    expected_referal_verified_msg="Referral Code Applied Successfully"
    xpath_register_btn1="(//button[@tabindex='0'])[1]"
    xpath_post_a_job_btn="//button[contains(text(),'Post a Job')]"
    xpath_freemium_popup="//nb-dialog-container/nb-card/nb-card-body/div"
    xpath_view_candidates="//button[contains(text(),'View Top Candidates')]"


    def enterMobileNo(self, mobile):
        self.sendKeys(mobile, self.xpath_mob_no_field, locatorType='xpath')
        self.pressEnter(self.xpath_mob_no_field, locatorType='xpath')

    def enterOTP(self, otp):
        self.sendKeys(otp, self.xpath_otp_field, locatorType='xpath')
        self.pressEnter(self.xpath_otp_field, locatorType='xpath')

    def enterEmail(self, email, password):
        before_window = self.driver.current_window_handle
        self.log.info(before_window)

        handles = self.driver.window_handles

        for handle in handles:
            self.log.info("inside for loop")
            if handle not in before_window:
                self.log.info(handle)
                after_window = handle
                time.sleep(2)
                self.driver.switch_to.window(after_window)

                self.log.info("switched window")
                self.sendKeys(email, self.xpath_email_selection, locatorType='xpath')
                time.sleep(2)
                self.elementClick(self.xpath_nxt_btn, locatorType='xpath')
                time.sleep(2)
                self.sendKeys(password, self.xpath_email_password_field, locatorType='xpath')
                time.sleep(2)
                self.elementClick(self.xpath_password_nxt_btn, locatorType='xpath')
                time.sleep(2)
        self.driver.switch_to.window(before_window)
        time.sleep(2)
    def select_location(self):
        self.sendKeys("j", self.xpath_location, locatorType="xpath")
        # time.sleep(2)
        self.elementClick(self.xpath_select_location, locatorType="xpath")
    def select_company(self):

        self.elementClick(self.xpath_company_field, locatorType="xpath")
        self.log.info("selected company field")
        time.sleep(2)
        self.elementClick(self.xpath_select_company, locatorType="xpath")
    def select_designation(self):
        self.elementClick(self.xpath_designation_field, locatorType="xpath")
        # time.sleep(2)
        self.elementClick(self.xpath_select_designation, locatorType="xpath")
    def enter_referal(self, referal_code):
        self.elementClick(self.xpath_referal_link, locatorType="xpath")
        # time.sleep(2)
        self.sendKeys(referal_code,self.xpath_referal_field, locatorType="xpath")
        time.sleep(1)
        self.elementClick(self.xpath_continue_button, locatorType="xpath")
        time.sleep(5)
        self.screenShot('referal_code_added')
        self.elementClick(self.xpath_register_btn1, locatorType="xpath")
        # time.sleep(2)
        
    def verifyToastMessage(self):
        actual_message=self.getTextOnElement(self.xpath_referal_success_msg, locatorType="xpath")
        self.log.info(actual_message)
        result=self.verifyText(self.expected_referal_verified_msg,actual_message)
        return result


    def recruiter_login(self, mobile_no, otp):
        self.enterMobileNo(mobile_no)
        # time.sleep(3)
        self.enterOTP(otp)
    def recruiter_details(self,email, password,referal_code):
        self.enterEmail(email, password)
        time.sleep(2)
        self.select_location()
        time.sleep(4)
        self.select_company()
        time.sleep(4)
        self.select_designation()
        # time.sleep(4)
        self.enter_referal(referal_code)
        # time.sleep(3)
        # self.verifyToastMessage()

    def verify_onboard_succesful(self):
        self.screenShot('onboard successful')
        # time.sleep(2)
        result = self.isElementPresent(self.xpath_post_a_job_btn, locatorType="xpath")
        return result

    def verifyFreeJobPost(self):
        self.elementClick(self.xpath_post_a_job_btn, locatorType='xpath')
        # time.sleep(2)
        self.postAJob()
        # time.sleep(3)

    def verifyFreemiumPopup(self):
       result= self.isElementPresent(self.xpath_freemium_popup, locatorType="xpath")
       # time.sleep(2)
       self.elementClick(self.xpath_view_candidates, locatorType='xpath')
       # time.sleep(5)
       return result
