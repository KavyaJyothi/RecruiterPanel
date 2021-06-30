from base.selenium_driver import SeleniumDriver
from  Pages.login_page import LoginFlow
import utilities.custom_logger as cl
import logging
import time
class AddStaffFlow(LoginFlow):

    log = cl.customLogger(logging.DEBUG)
    manage_staff_tab=("//span[contains(text(),'Manage Staff')]", "xpath")
    all_staff_tab=("//span[ contains(text(),'All Staff')]","xpath")
    add_employee_button=("//div[@nbcontextmenutag= 'add-employee-options'  and contains(text(),'Add Employee')]", "xpath")
    add_single_staff=("//ul/li/a[@title='Add Single Staff']", "xpath")
    employee_name=("//input[@formcontrolname='name']","xpath")
    employee_mobile=("//input[@formcontrolname='mobileNo']","xpath")
    employee_role=("//input[@formcontrolname='role']","xpath")
    select_role=("//nb-option-list/ul/nb-option[1]","xpath")
    joining=("//input[@formcontrolname='joiningDate']", "xpath")
    in_time_xp=("//input[@formcontrolname='inTime']", "xpath")
    out_time_xp=("//input[@formcontrolname='outTime']", "xpath")
    
    def select_joining_date(self, date):
        date_of_joining="(//nb-calendar-day-cell/div[text()=' {0} '])[1]"
        xpath_date_of_joining=date_of_joining.format(date)
        xp_date=(xpath_date_of_joining, "xpath")
        return xp_date
    def select_gender(self, gender):
        gender_radio="//label/span[3][contains(text(),'{0}')]"
        select_gender=gender_radio.format(gender)
        xp_gender_radio=(select_gender, "xpath")
        return xp_gender_radio
    def payroll_type(self, payroll):
        payroll_select="//label/input[@value='{0}']"
        xp_payroll=payroll_select.format(payroll)
        xp_payroll_type=(xp_payroll,"xpath")
        return xp_payroll_type
    nxt_button=("(//button[contains(text(),'Next')])[1]","xpath")
    employee_sal=("//input[@formcontrolname='salary']","xpath")
    skip_navigation_pop_up = ("//div/button[contains(text(),'Skip')]", "xpath")
    
    def click_manage_staff(self):
        self.elementClick(self.manage_staff_tab)
    def click_all_staff(self):
        self.elementClick(self.all_staff_tab)
    def click_add_staff_button(self):
        self.elementClick(self.add_employee_button)
        self.elementClick(self.add_single_staff)
    def enter_employee_name(self, name):
        self.sendKeys(name, self.employee_name )
    def enter_employee_mobile_no(self, mobile_no):
        self.sendKeys(mobile_no, self.employee_mobile )
    def enter_employee_role(self, role):
        self.sendKeys(role, self.employee_role)
        self.elementClick(self.select_role)
    def select_joining(self, date):
        self.elementClick(self.joining)
        self.elementClick(self.select_joining_date(date))
    def click_gender(self, gender):
        self.elementClick(self.select_gender(gender))
    def enter_sal(self, salary):
        self.sendKeys(salary,self.employee_sal)

    def click_nxt(self):
        self.elementClick(self.nxt_button)
        time.sleep(1)

    def enter_in_time(self, in_time):
        
        self.sendKeys(in_time, self.in_time_xp)


    def click_skip(self):
        if self.isElementPresent(self.skip_navigation_pop_up) is True:
            time.sleep(3)
            self.elementClick(self.skip_navigation_pop_up)
        else:
            print("popup not present")
            
    def login_as_bo(self, mobile, otp):
        self.login_flow(mobile, otp)
    def click_add_staff(self):
        self.click_manage_staff()
        self.click_skip()
        time.sleep(2)
        self.click_manage_staff()
        self.click_all_staff()
        self.click_add_staff_button()
    def enter_employee_details(self, name, mobile_no, role, date,gender, salary, in_time):
        self.enter_employee_name(name)
        self.enter_employee_mobile_no(mobile_no)
        self.enter_employee_role(role)
        time.sleep(3)
        self.select_joining(date)
        self.click_gender(gender)
        self.click_nxt()
        time.sleep(3)
        self.enter_sal(salary)
        time.seep(3)
        self.click_nxt()
        time.sleep(3)
        self.enter_in_time(in_time)
        time.sleep(1)
        self.click_nxt()

    
    
    
    