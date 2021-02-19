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


    @data(*read_csv_data("plans.csv"))
    @unpack
    def test_purchasePlans(self,mobile_no, otp, email):

        self.pp.login( mobile_no, otp)
        self.pp.navigate_to_buy_plan( mobile_no, email)
        #self.pp.enter_GST_Details(gst_no, address, email)








