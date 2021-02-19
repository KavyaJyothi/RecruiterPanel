from Pages.job_posting_flow_page import JobPostingFlow
import unittest
import pytest
import time
from utilities.get_csv_data import read_csv_data
from utilities.teststatus import TestStatus
from base.selenium_driver import SeleniumDriver
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("oneTimeSetUp")
@ddt
class Post_Job_Test(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.jpp = JobPostingFlow(self.driver)
        self.ts= TestStatus(self.driver)

    @data(*read_csv_data("data1.csv"))
    @unpack
    def test_post_a_job(self,mobile_no, otp):
        time.sleep(3)
        self.jpp.login_Click_Post_Job_Btn( mobile_no, otp)
        time.sleep(3)
        self.jpp.postAJob()
        time.sleep(3)
        result1=self.jpp.verifyJobPostSuccessMessage()
        self.ts.markFinal('job posting flow', result1, 'Verification of job posting flow')
        time.sleep(2)
        self.jpp.clickViewSugCan()
        time.sleep(2)
        result2=self.jpp.verifyCallNowButton()
        self.ts.markFinal('contact candidate', result2, 'Candidate unlocking')
        time.sleep(2)
        self.jpp.clickCallNowButton()
        time.sleep(2)




