from Pages.post_job_add_company import JobPostingFlowAddCompany
import unittest
import pytest
import time
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("oneTimeSetUp")

class PostJobAddCompanyTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.jpp = JobPostingFlowAddCompany(self.driver)

    def test_purchasePlans(self,mobileNo='9538596331', otp='495004'):
        time.sleep(3)
        self.jpp.enterMobileNo(mobileNo)
        time.sleep(3)
        self.jpp.enterOTP(otp)
        time.sleep(3)
        self.jpp.postAJob()
        time.sleep(3)
        self.jpp.callFeedback()
        time.sleep(2)

