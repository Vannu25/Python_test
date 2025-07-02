# The xdist package is used to run the test in parallel using -n argument using
# that many num of workers.
# To run HTML report install pyest-html package

# using fixture to minimize unnecessary repetitive code and clean code for better understanding.
# params can be used to optimized and reduce code, eg for using web drivers.

import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    print("\n[SETUP] Launching Chrome")
    driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
    yield driver
    print("\n[TEARDOWN] Closing Chrome")
    driver.quit()

def test_login1(driver):
    driver.get("https://www.google.com")
    assert driver.title == "Google"

def test_login2(driver):
    driver.get("https://www.facebook.com")
    assert driver.title == "facebook"

def test_login3(driver):
    driver.get("https://www.instagram.com")
    assert driver.title == "Instagram"
