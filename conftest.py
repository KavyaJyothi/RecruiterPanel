import pytest
from Pages.login_page import LoginFlow
from base.webDriverFactory import WebDriverFactory
import time

@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    # lf=LoginFlow(driver)
    # time.sleep(2)
    # lf.loginFlow("9538596331","495004")
    if request.cls is not None:
        request.cls.driver = driver


    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")