from  selenium import webdriver
import os
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()
    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType +
                          " not correct/supported")
        return False

    # def waitForElement(self, locator, locatorType="id",
    #                    timeout=10, pollFrequency=0.5):
    #     element = None
    #     try:
    #         byType = self.getByType(locatorType)
    #         print("Waiting for maximum :: " + str(timeout) +
    #               " :: seconds for element to be clickable")
    #         wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
    #                              ignored_exceptions=[NoSuchElementException,
    #                                                  ElementNotVisibleException,
    #                                                  ElementNotSelectableException])
    #         element = wait.until(EC.element_to_be_clickable((byType, locator)))
    #         print("Element appeared on the web page")
    #     except:
    #         print("Element not appeared on the web page")
    #         print_stack()
    #     return element
    #
    def getElement(self, locator):
        value= locator[0]
        locator_type=locator[1]
        
        try:
            locatorType = locator_type.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, value)
            self.log.info("Element found with locator: " + value +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + value +
                          " and  locatorType: " + locator_type)
        return element
    def clearField(self, locator):
       
        try:

            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, value)
            element.clear()
            self.log.info("Element found with locator: ")
        except:
            self.log.info("Element not found with locator: " )

    def elementClick(self, locator):

        try:

            element = self.getElement(locator)
            element.click()
            self.log.info("Clicked on element with locator: " )
        except:
            self.log.info("Cannot click on the element with locator: " )
            print_stack()

    def getTextOnElement(self, locator):
        try:
            actual_text= self.getElement(locator).getText()
            self.log.info(actual_text)
            return actual_text
        except:
            self.log.info("Unable to locate element: " )
            print_stack()
    def accept_alert(self):

        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')
            alert = self.driver.switch_to.alert
            alert.accept()
            print("alert accepted")
        except TimeoutException:
            print("no alert")

    def verifyText(self, expected_text, actual_text):
        if expected_text in actual_text:
            return True
        else:
            return  False
    def getCookies(self):
        cookies=self.driver.get_cookies()
        return cookies

    def getParentWindowHandle(self):
      parent_handle= self.driver.current_window_handle
      self.log.info(parent_handle)
      return parent_handle
    def getAllWindowHandle(self, locator):
        parent_handle=self.getParentWindowHandle()
        self.elementClick(locator)
        handles = self.driver.window_handles

        for handle in handles:
            self.log.info("inside for loop")
            if handle not in parent_handle:
                self.log.info(handle)
                child_window = handle
                time.sleep(2)
                self.driver.switch_to.window(child_window)
                self.log.info("switched window")
                return


    def pressEnter(self, locator):

        try:
            element = self.getElement(locator)
            element.send_keys(Keys.ENTER)
            self.log.info("Sent data on element with locator: " )
        except:
            self.log.info("Cannot send data on the element with locator: ")
            print_stack()


    def sendKeys(self, data, locator):

        try:
            element = self.getElement(locator)
            element.send_keys(data)
            self.log.info("Sent data on element with locator:")
        except:
            self.log.info("Cannot send data on the element with locator: ")
            print_stack()

    def isElementPresent(self, locator):

        try:
            element = self.getElement(locator)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    # def waitForElement(self, locator,
    #                            timeout=10, pollFrequency=0.5):
    #     element = None
    #     try:
    #         byType = self.getByType(locator)
    #         self.log.info("Waiting for maximum :: " + str(timeout) +
    #               " :: seconds for element to be clickable")
    #         wait = WebDriverWait(self.driver, 10, poll_frequency=1,
    #                              ignored_exceptions=[NoSuchElementException,
    #                                                  ElementNotVisibleException,
    #                                                  ElementNotSelectableException])
    #         element = wait.until(EC.element_to_be_clickable((byType,
    #                                                          "stopFilter_stops-0")))
    #         self.log.info("Element appeared on the web page")
    #     except:
    #         self.log.info("Element not appeared on the web page")
    #         print_stack()
    #     return element
    def webScroll(self):
        self.driver.execute_script("window.scrollTo(0, -1000);")