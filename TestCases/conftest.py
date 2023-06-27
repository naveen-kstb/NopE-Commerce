from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser =="chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome Browser.......")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox Browser.......")
    elif browser == "edge":
        driver = webdriver.Edge()
        print("Launching Edge Browser.......")
    else:
        driver = webdriver.Chrome()
        print("Launching in default browser")
    return driver

def pytest_addoption(parser):  # This is will get the value form CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser")

############### PyTest HTML Report ########################

# It is hook for Adding Environment info to HTML Reort
def pytest_configure(config):
    config._metadata['Project Name'] = "nop commerce"
    config._metadata['Module Name'] = "customers"
    config._metadata['Tester'] = "Naveen"

# It is hook for delete/modify Environment info to HTML Reort
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)