from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time
from utilities.teststatus import TestStatus
class JobPostingFlow(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    ###################locators##################################
    xpath_mobileNo = "//input[@formcontrolname='mobile_no']"
    xpath_otp = "//input[@formcontrolname='otp']"
    xpath_post_a_job_button="//button[@tabindex='0' ]/b[contains(text(),'+')]"
    xpath_industry_textbox="(//div[@class='ng-input']/input[@role='combobox'])[1]"
    xpath_industry_sales="//div[@role='option']/div/div/div[contains(text(),'Sales & Business Development')]"
    xpath_category_textbox="(//div[@class='ng-input']/input[@role='combobox'])[2]"
    xpath_category_retail="//div[@role='option']/span[contains(text(),'Retail')]"
    xpath_role_textbox="(//div[@class='ng-input']/input[@role='combobox'])[3]"
    xpath_role_area_sales="//div[@role='option']/div[contains(text(),'Area Sales Officer')]"
    xpath_location="//div/ngx-location/input[@class='mb-2 custom pl-0 ng-star-inserted']"
    xpath_location_bengaluru="//nb-list-item[@role='listitem']/div/b[contains(text(),'Bengaluru')]"
    xpath_next_button="//button[@status='danger' and @tabindex='0'  and contains(text(),'NEXT')]"
    xpath_publish_job="//button[@status='danger' and @tabindex='0'  and contains(text(),'Publish Job')]"
    xpath_post_job_success_popup="//nb-card-header/div/small"
    xpath_view_sug_can="//button[@tabindex='0' and contains(text(),'View suggested candidates for this job')]"
    xpath_call_now_button="(//button[@tabindex='0']/img[@src='assets/svgs/call-white.svg'])[1]"
    ############################# verification text ###########################################
    view_sug_candidates_popup="View suggested candidates for this job"
    def enterMobileNo(self, mobile):
        self.sendKeys(mobile, self.xpath_mobileNo, locatorType='xpath')
        self.pressEnter(self.xpath_mobileNo, locatorType='xpath')

    def enterOTP(self, otp):
        self.sendKeys(otp, self.xpath_otp, locatorType='xpath')
        self.pressEnter(self.xpath_otp, locatorType='xpath')

    def clickPostAJob(self):
        self.elementClick(self.xpath_post_a_job_button, locatorType='xpath')
    def clickIndustryTextBox(self):
        self.elementClick(self.xpath_industry_textbox, locatorType='xpath')
    def selectIndustry(self):
        self.elementClick(self.xpath_industry_sales, locatorType="xpath")
    def clickCategoryTextBox(self):
        self.elementClick(self.xpath_category_textbox, locatorType='xpath')
    def selectCategory(self):
        self.elementClick(self.xpath_category_retail, locatorType='xpath')
    def clickRoleTextBox(self):
        self.elementClick(self.xpath_role_textbox, locatorType='xpath')
    def selectRole(self):
        self.elementClick(self.xpath_role_area_sales, locatorType='xpath')
    def enterLocation(self):
        self.sendKeys("Bengaluru", self.xpath_location, locatorType='xpath')
        time.sleep(2)
        self.elementClick(self.xpath_location_bengaluru, locatorType='xpath')
    def clickNextButton(self):
        self.elementClick(self.xpath_next_button, locatorType='xpath')
    def clickPublishJob(self):
        self.elementClick(self.xpath_publish_job, locatorType='xpath')

    def login_Click_Post_Job_Btn(self, mobile_no, otp):
        time.sleep(2)
        self.enterMobileNo(mobile_no)
        time.sleep(2)
        self.enterOTP(otp)
        time.sleep(3)
        self.clickPostAJob()


    def postAJob(self):

        self.clickIndustryTextBox()
        time.sleep(1)
        self.selectIndustry()
        time.sleep(2)
        self.clickCategoryTextBox()
        self.selectCategory()
        time.sleep(2)
        self.clickRoleTextBox()
        time.sleep(2)
        self.selectRole()
        time.sleep(2)
        self.enterLocation()
        time.sleep(2)
        self.clickNextButton()
        time.sleep(2)
        self.clickNextButton()
        time.sleep(2)
        self.clickNextButton()
        time.sleep(4)
        self.clickNextButton()
        self.clickNextButton()
        time.sleep(4)
        self.screenShot("publish job")
        time.sleep(3)
        self.clickPublishJob()
        time.sleep(3)

    def verifyJobPostSuccessMessage(self):
        result=self.isElementPresent(self.xpath_post_job_success_popup, locatorType='xpath')
        return result

    def clickViewSugCan(self):
        self.elementClick(self.xpath_view_sug_can, locatorType='xpath')

    def verifyCallNowButton(self):
        result=self.isElementPresent(self.xpath_call_now_button, locatorType='xpath')
        return result

    def clickCallNowButton(self):
        self.elementClick(self.xpath_call_now_button, locatorType='xpath')
        time.sleep(3)
        self.screenShot("contact status")


