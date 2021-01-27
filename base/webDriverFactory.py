import traceback
from selenium import webdriver
import os


class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser

    def getWebDriverInstance(self):

        baseURL = "https://cerebrodev.workex.ai/recruiter/home"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set chrome driver
            chromedriver = "/home/kavya/tools/chromedriver_linux64/chromedriver"
            os.environ["webdriver.chrome"] = chromedriver
            driver = webdriver.Chrome(chromedriver)


        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        driver.get(baseURL)


        # Maximize the window
        driver.maximize_window()


        # Loading browser with App URL

        return driver