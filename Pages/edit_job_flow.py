from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time
class EditJobFlow(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver = driver

    xpath_mobileNo = "//input[@formcontrolname='mobile_no']"
    xpath_otp = "//input[@formcontrolname='otp']"
    xpath_job_card="(//nb-card/div[@class='nb-card-div'])[1]"
    xpath_actions="(//nb-select/button[@type='button'])[1]"
    xpath_edit_job="//div/ul[@class='options-list']/nb-option[@value='editjob']"
    xpath_no_of_openings="(//div/span[contains(text(),'10+')])[1]"
    xpath_part_time="//div/span[contains(text(),'Part Time')]"
    xpath_qual_master="//div/span[contains(text(),'Masters')]"
    xpath_add_more_skills="//div/span/span[contains(text(),' Add More Skills')]"
    xpath_add_skills_text_box="//div[@class='ng-select-container']/div[@class='ng-value-container']/div[@class='ng-input']/input"
    xpath_add_item="//div[@role='option']/span"
    xpath_save_button="(//div/button[@tabindex='0' and contains(text(),'Save')])[2]"
    xpath_add_benifits="//span[contains(text(),' Add Benefits')]"
    xpath_select_benifits="//nb-card/nb-card-body/div[9]"
    xpath_benifits_done="//button[contains(text(),'Done')] "
    xpath_add_lan = "//span[contains(text(),' Add Language')]"
    xpath_select_lan = "//nb-card/nb-card-body/div[3]"
    xpath_lan_done = "//button[contains(text(),'Done')] "
    xpath_save_edit="(//button[contains(text(),'Save')])[2]"
    xpath_toast="nb-toastr-container.ng-tns-c35-7 ng-star-inserted > nb-toast"
    expected_text="Job post details updated successfully"


    def enterMobileNo(self, mobile):
        self.sendKeys(mobile, self.xpath_mobileNo, locatorType='xpath')
        self.pressEnter(self.xpath_mobileNo, locatorType='xpath')

    def enterOTP(self, otp):
        time.sleep(2)
        self.sendKeys(otp, self.xpath_otp, locatorType='xpath')
        self.pressEnter(self.xpath_otp, locatorType='xpath')

    def clickJobCard(self):
        self.elementClick(self.xpath_job_card, locatorType='xpath')
    def clickActions(self):
        self.waitForElement(self.xpath_actions, locatorType="xpath")
        self.elementClick(self.xpath_actions, locatorType="xpath")
    def clickEditJob(self):
        self.waitForElement(self.xpath_edit_job, locatorType="xpath")
        self.elementClick(self.xpath_edit_job, locatorType="xpath")
    def clickNoOfOpenings(self):
        self.elementClick(self.xpath_no_of_openings, locatorType='xpath')
    def clickPartTimeChip(self):
        self.elementClick(self.xpath_part_time, locatorType='xpath')
    def clickQualMasters(self):
        self.elementClick(self.xpath_qual_master, locatorType='xpath')
    def clickAddMoreSkills(self):
        self.elementClick(self.xpath_add_more_skills, locatorType='xpath')
    def enterMoreSkills(self, skill):
        self.sendKeys(skill, self.xpath_add_skills_text_box, locatorType='xpath')
        self.elementClick(self.xpath_add_item, locatorType='xpath')
    def clickSave(self):
        self.elementClick(self.xpath_save_button, locatorType='xpath')
    def addBenifits(self):
        # time.sleep(2)
        self.elementClick(self.xpath_add_benifits, locatorType='xpath')
        # time.sleep(2)
        self.elementClick(self.xpath_select_benifits, locatorType='xpath')
        self.elementClick(self.xpath_benifits_done, locatorType='xpath')
    def addLanguage(self):
        self.elementClick(self.xpath_add_lan, locatorType='xpath')
        # time.sleep(2)
        self.elementClick(self.xpath_select_lan, locatorType='xpath')
        # time.sleep(2)
        self.elementClick(self.xpath_lan_done, locatorType='xpath')
    def clickSaveEdit(self):
        self.elementClick(self.xpath_save_edit, locatorType='xpath')
    def getToastText(self):
        actual_text=self.getElement(self.xpath_toast, locatorType='xpath').text
        if self.expected_text in actual_text:
            self.log.info("Pass")

    def editJob(self):
        self.clickJobCard()

        self.clickActions()
        time.sleep(1)
        self.clickEditJob()
        time.sleep(1)
        self.clickNoOfOpenings()
        # time.sleep(1)
        self.clickQualMasters()
        # time.sleep(1)
        self.clickAddMoreSkills()
        # time.sleep(1)
        self.enterMoreSkills('tally')
        # time.sleep(2)
        self.clickSave()
        # time.sleep(6)
        self.addBenifits()
        # time.sleep(2)
        self.addLanguage()
        # time.sleep(4)
        self.clickSaveEdit()
        
        self.screenShot("Job Edit")
        time.sleep(2)





