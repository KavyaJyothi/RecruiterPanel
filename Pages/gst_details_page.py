from Pages.plans_page import PlansPage
import utilities.custom_logger as cl
import logging
import time
class GSTDetailEntry(PlansPage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    id_email_field = "email"
        
    def gst_details_entry(self, mobile_no, otp, email, gst_no, address):
        self.login( mobile_no, otp)
        time.sleep(2)
        self.navigate_to_buy_plan( mobile_no, email)
        time.sleep(3)
        self.enter_GST_Details( gst_no, address, email)
        