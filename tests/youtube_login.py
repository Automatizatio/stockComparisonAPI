'''
Rewrite test to test two different websites and an API
'''

# Import the required modules
import os
import pytest
import time
# Import logging module
import logging

# Configure logging level, format, and output
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Define the URL and locators for youtube login page
url = "https://www.youtube.com/"
sign_in_button = (By.XPATH, "//ytd-button-renderer[@class='style-scope ytd-masthead style-suggestive size-small']")
email_field = (By.ID, "identifierId")
next_button = (By.ID, "identifierNext")
password_field = (By.NAME, "password")
login_button = (By.ID, "passwordNext")

# Define the driver path
driver_path = "/chromedriver_win32/chromedriver.exe"
service = Service(driver_path)
# Define a fixture to initialize and quit the webdriver
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

# Define a test function to log into youtube using the credentials
def test_login_youtube(driver):
    logging.info("hello")
    print('hello chris')

    # Navigate to the url
    driver.get(url)
    #driver.implicitly_wait(10)    
    WebDriverWait(driver, 10).until(EC.title_contains("YouTube"))
    a_tag = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Sign in']")))    
    a_tag.click()
    # Find input element by aria-label
    input_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Email or phone']")))    

    #input_field = driver.find_element_by_xpath("//input[@aria-label='Email or phone']")

    # Type into the input field
    input_field.send_keys('hiChris')
    signInNext = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']")))    
    signInNext.click()
    time.sleep(10)
    '''
    # Click on the sign in button
    driver.find_element(*sign_in_button).click()
    # Wait for the email field to be visible and enter the email
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(email_field))
    driver.find_element(*email_field).send_keys(email)
    # Click on the next button
    driver.find_element(*next_button).click()
    # Wait for the password field to be visible and enter the password
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(password_field))
    driver.find_element(*password_field).send_keys(password)
    # Click on the login button
    driver.find_element(*login_button).click()
    # Wait for the login to be successful and verify the title
    WebDriverWait(driver, 10).until(EC.title_contains("YouTube"))
    assert "YouTube" in driver.title
    '''