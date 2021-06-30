from selenium import webdriver
from Pages.add_staff import AddStaffFlow

import unittest
import pytest
import time
from  utilities.get_csv_data import  read_csv_data
from ddt import ddt, data, unpack
@ddt
@pytest.mark.usefixtures("oneTimeSetUp")
class Add_Staff_Test(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.asf = AddStaffFlow(self.driver)

    @data(*read_csv_data("add_staff.csv"))
    @unpack
    def test_add_staff(self,mobileNo, otp, emp_name, emp_no, emp_role, date,gender, salary, in_time):
        self.asf.login_as_bo(mobileNo, otp)
        time.sleep(2)
        self.asf.click_add_staff()
        time.sleep(2)
        self.asf.enter_employee_details( emp_name, emp_no, emp_role, date,gender, salary, in_time )
        
        