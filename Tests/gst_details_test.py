import pytest
import unittest
from Pages.gst_details_page import GSTDetailEntry
from Pages.plans_page import PlansPage
import unittest
import pytest
import time
from utilities.teststatus import TestStatus
from  utilities.get_csv_data import  read_csv_data
from ddt import ddt, data, unpack
@ddt
@pytest.mark.usefixtures("oneTimeSetUp")
class TestGSTDetailsEntry(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classLevelSetup(self):
        self.gdp=GSTDetailEntry(self.driver)
        self.pp= PlansPage(self.driver)
        self.ts= TestStatus(self.driver)
    @data(*read_csv_data("gst_details.csv"))
    @unpack
    def test_gst_popup(self,mobile_no, otp, email, gst_no, address):
        self.pp.login(mobile_no, otp)
        self.pp.navigate_to_buy_plan(mobile_no, email)
        time.sleep(4)
        self.gdp.gst_details_entry( mobile_no, otp, email, gst_no, address)
        time.sleep(2)
        result=self.gdp.verify_gst_details()
        self.ts.markFinal('GST details popup', result, 'Verification of GST details')



