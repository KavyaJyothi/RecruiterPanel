from selenium import webdriver
from Pages.edit_job_flow import EditJobFlow

import unittest
import pytest
import time
from  utilities.get_csv_data import  read_csv_data
from ddt import ddt, data, unpack
@ddt
@pytest.mark.usefixtures("oneTimeSetUp")
class EditJob_Test(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.ejf = EditJobFlow(self.driver)

    @data(*read_csv_data("data1.csv"))
    @unpack
    def test_edit_job(self,mobileNo, otp):
        time.sleep(3)
        self.ejf.enterMobileNo(mobileNo)
        time.sleep(3)
        self.ejf.enterOTP(otp)
        time.sleep(2)
        self.ejf.editJob()

