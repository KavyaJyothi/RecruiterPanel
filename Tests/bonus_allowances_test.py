from selenium import webdriver
from Pages.add_bonus_allowances import AddBonusAllowances

import unittest
import pytest
import time
from  utilities.get_csv_data import  read_csv_data
from ddt import ddt, data, unpack
@ddt
@pytest.mark.usefixtures("oneTimeSetUp")
class Bonus_Allowances_Test(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.aba = AddBonusAllowances(self.driver)
    @data(*read_csv_data("bonus.csv"))
    @unpack
    def test_add_bonus_aliow(self, mobile, otp, amt, date, note):
        self.aba.add_bonus_allowances( mobile, otp,amt, date, note)
