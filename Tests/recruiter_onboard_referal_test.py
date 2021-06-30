from selenium import webdriver
from Pages.recruiter_onboarding_with_referal import RecruiterOnboardReferal
from Pages.gst_details_page import GSTDetailEntry
import unittest
import pytest
import time
from utilities.teststatus import TestStatus
from  utilities.get_csv_data import  read_csv_data
from ddt import ddt, data, unpack
@ddt
@pytest.mark.usefixtures("oneTimeSetUp")
class RecruiterOnboarding_Test(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.ro= RecruiterOnboardReferal(self.driver)
        self.ts = TestStatus(self.driver)
        self.gst= GSTDetailEntry(self.driver)
        


    @data(*read_csv_data("onboard_data.csv"))
    @unpack
    def test_recruiter_onboard(self, mobile_no, otp, email, password, referal_code):
        time.sleep(2)
        self.ro.recruiter_login( mobile_no, otp)
        time.sleep(6)
        self.ro.recruiter_details(email, password, referal_code)
        time.sleep(4)
        result1=self.ro.verify_onboard_succesful()
        self.ts. mark(result1,'recruiter onboard' )
        self.ro.verifyFreeJobPost()
        time.sleep(2)
        result2=self.ro.verifyFreemiumPopup()
        # time.sleep(2)
        self.ts.markFinal('test recruiter onboard', result2, 'verified free job post')
        # time.sleep(5)
        # self.gst.gst_details_entry(mobile_no, otp, email, gst_no, address)


