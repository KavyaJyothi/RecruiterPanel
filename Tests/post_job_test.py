from Pages.job_posting_flow_page import JobPostingFlow
import unittest
import pytest
import time
from utilities.get_csv_data import read_csv_data
from ddt import  ddt, data, unpack

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.jpp = JobPostingFlow(self.driver)
    @data(*read_csv_data("data1.csv"))
    @unpack
    def test_purchasePlans(self,mobileNo, otp):
        time.sleep(3)
        self.jpp.enterMobileNo(mobileNo)
        time.sleep(3)
        self.jpp.enterOTP(otp)
        time.sleep(3)
        self.jpp.postAJob()
        time.sleep(3)
        self.jpp.callFeedback()
        time.sleep(2)


