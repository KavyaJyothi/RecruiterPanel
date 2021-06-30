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
    xpath_mobileNo =( "//input[@formcontrolname='mobile_no']", "xpath")
    xpath_otp = ("//input[@formcontrolname='otp']", "xpath")
    xpath_post_a_job_button=("//button[contains(text(),' JOB')]","xpath")
    xpath_industry_textbox=("(//div[@class='ng-input']/input[@role='combobox'])[1]","xpath")
    xpath_industry_selection=("//div/div/div[@class='font-weight-bold']", "xpath")

    xpath_category_textbox=("(//div[@class='ng-input']/input[@role='combobox'])[2]","xpath")
    xpath_category_selection=("//span[@class='ng-option-label ng-star-inserted']", "xpath")

    xpath_role_textbox=("(//div[@class='ng-input']/input[@role='combobox'])[3]","xpath")
    xpath_add_item=("//span[contains(text(),'Add item')]","xpath")

    xpath_location=("//ngx-location/input[@type='text']","xpath")
    def select_location(self, loc):
        xpath_location="(//b[contains(text(),'{0}')])[1]"
        location_xp=xpath_location.format(loc)
        location=(location_xp,"xpath")
        return location
    skill_1=("//ngx-search-add-chip/div[1]/div[2]","xpath")
    skill_2=("//ngx-search-add-chip/div[1]/div[3]","xpath")
    skill_3=("//ngx-search-add-chip/div[1]/div[4]","xpath")
    skill_4=("//ngx-search-add-chip/div[1]/div[5]","xpath")
    xpath_next_button=("//button[@status='danger' and @tabindex='0'  and contains(text(),'NEXT')]","xpath")
    xpath_publish_job=("//button[@status='danger' and @tabindex='0'  and contains(text(),'Publish Job')]","xpath")
    xpath_post_job_success_popup=("//nb-card-header/div/small","xpath")
    xpath_view_sug_can=("//button[@tabindex='0' and contains(text(),'View suggested candidates for this job')]","xpath")
    xpath_call_now_button=("(//button[contains(text(),'CALL NOW')])[1]","xpath")
    skip_navigation_pop_up=("//div/button[contains(text(),'Skip')]","xpath")

    ############################# verification text ###########################################
    view_sug_candidates_popup="View suggested candidates for this job"
    def enterMobileNo(self, mobile):
        self.sendKeys(mobile, self.xpath_mobileNo)
        self.pressEnter(self.xpath_mobileNo)

    def enterOTP(self, otp):

        self.sendKeys(otp, self.xpath_otp)
        self.pressEnter(self.xpath_otp)
       

    def clickPostAJob(self):
        self.elementClick(self.xpath_post_a_job_button)
    def clickIndustryTextBox(self, industry):
        self.sendKeys(industry,self.xpath_industry_textbox)
    def selectIndustry(self):
        self.elementClick(self.xpath_industry_selection)
    def clickCategoryTextBox(self, category):
        self.sendKeys(category, self.xpath_category_textbox)
    def selectCategory(self):
        self.elementClick(self.xpath_category_selection)
    def clickRoleTextBox(self, role):
        self.sendKeys(role, self.xpath_role_textbox)
    def selectRole(self):
        self.elementClick(self.xpath_add_item)
    def enterLocation(self,loc):
        self.sendKeys( loc,self.xpath_location)     
        self.elementClick(self.select_location(loc))
    def clickNextButton(self):
        self.elementClick(self.xpath_next_button)
    def select_skill(self):
        self.elementClick(self.skill_1)
        self.elementClick(self.skill_2)
        self.elementClick(self.skill_3)
        self.elementClick(self.skill_4)

    def clickPublishJob(self):
        self.elementClick(self.xpath_publish_job)

    def click_skip(self):
        if self.isElementPresent( self.skip_navigation_pop_up) is True:
            time.sleep(3)
            self.elementClick(self.skip_navigation_pop_up)
        else:
            print("popup not present")

    def login_Click_Post_Job_Btn(self, mobile_no, otp):
        # time.sleep(2)
        self.enterMobileNo(mobile_no)
        # time.sleep(3)
        self.enterOTP(otp)
        self.clickPostAJob()

    def postAJob(self, industry, category, role, loc):

        self.clickIndustryTextBox(industry)
           
        self.selectIndustry()
        self.click_skip()
        self.clickCategoryTextBox(category)
        time.sleep(2)
        self.selectCategory()
        # time.sleep(2)
        self.clickRoleTextBox(role)
        # time.sleep(2)
        self.selectRole()
        self.enterLocation(loc)
        time.sleep(4)
        self.clickNextButton()
        time.sleep(2)
        self.select_skill()
        time.sleep(4)
        self.clickNextButton()
        time.sleep(3)
        self.clickNextButton()
        time.sleep(4)
        self.clickNextButton()
        self.clickNextButton()
        # time.sleep(4)
        self.screenShot("publish job")
        # time.sleep(3)
        self.clickPublishJob()
        # time.sleep(3)

    def verifyJobPostSuccessMessage(self):
        result=self.isElementPresent(self.xpath_post_job_success_popup)
        return result

    def clickViewSugCan(self):
        self.elementClick(self.xpath_view_sug_can)

    def verifyCallNowButton(self):
        result=self.isElementPresent(self.xpath_call_now_button)
        return result

    def clickCallNowButton(self):
        self.elementClick(self.xpath_call_now_button)
        time.sleep(3)
        self.screenShot("contact status")


