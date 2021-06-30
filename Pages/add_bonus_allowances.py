from base.selenium_driver import SeleniumDriver
from  Pages.login_page import LoginFlow
import utilities.custom_logger as cl
import logging
import time
from Pages.add_staff import AddStaffFlow 
class AddBonusAllowances(AddStaffFlow):
    payrol_tab=("(//span[contains(text(),'Payroll')])[2]","xpath")
    bonus_tab=("//ngx-employee-payroll/div[1]/button[1]","xpath")
    amount_input=("//input[@formcontrolname='allowance_amount']","xpath")
    date_field=("//div/div/input[@placeholder='Select Date...']","xpath")
    def select_date(self, date):
        date_of_joining="(//nb-calendar-day-cell/div[text()=' {0} '])[1]"
        xpath_date_of_joining=date_of_joining.format(date)
        xp_date=(xpath_date_of_joining, "xpath")
        return xp_date
    note_field=("//textarea[@formcontrolname='allowance_description']","xpath")
    reason_bonus=("//div/span[contains(text(),'Positive Attitude')]","xpath")
    add_button=("//button[@type='submit' and @tabindex='0']", "xpath")

    def click_payroll(self):
        self.elementClick(self.payrol_tab)
    def click_bonus_allowances(self):
        self.elementClick(self.bonus_tab)
    def enter_amount(self, amt):
        self.sendKeys(amt,self.amount_input)
    def enter_date(self, date):
        self.elementClick(self.date_field)
        self.elementClick( self.select_date(date))
    def enter_note(self, note):
        self.sendKeys(note, self.note_field)
    def click_reason(self):
        self.elementClick(self.reason_bonus)
    def click_add(self):
        self.elementClick(self.add_button)

    def add_bonus_allowances(self, mobile, otp, amt, date, note):
        self.login_as_bo( mobile, otp)
        self.click_manage_staff()
        self.click_skip()
        time.sleep(2)
        self.click_manage_staff()
        time.sleep(2)      
        self.click_all_staff()
        self.click_payroll()
        self.click_bonus_allowances()
        self.enter_amount(amt)
        self.enter_date(date)

        self.enter_note(note)
        self.click_reason()
        self.click_add()
        time.sleep(3)
        



