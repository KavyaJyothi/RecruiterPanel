from selenium import webdriver
from Pages.plans_page import PlansPage
import unittest
import pytest
import time
from utilities.get_csv_data import read_csv_data
from  ddt import  ddt, data, unpack

@pytest.mark.usefixtures("oneTimeSetUp")
@ddt
class PlanPurchase_Test(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.pp = PlansPage(self.driver)


    @data(*read_csv_data("data1.csv"))
    @unpack
    def test_purchasePlans(self,mobileNo, otp):
        time.sleep(3)
        self.pp.enterMobileNo(mobileNo)
        time.sleep(3)
        self.pp.enterOTP(otp)
        time.sleep(3)
        self.pp.clickPlansIcon()
        time.sleep(2)
        self.pp.clickBuyNow()
        time.sleep(5)
        self.pp.enterPlansContactNo(mobileNo)
        time.sleep(2)
        self.pp.switch_to_window()






