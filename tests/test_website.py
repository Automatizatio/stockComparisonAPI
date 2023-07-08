import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

from dotenv import load_dotenv
load_dotenv()

finnHub_username = os.getenv("finnHub_username")
finnHub_password = os.getenv("finnHub_password")

# A random website that shows a joke
WEB_URL = "https://finnhub.io/"

# A fixture that creates and returns a webdriver instance
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
'''
# A test that checks if the website title is correct
def test_APIKeyGen(driver):
    driver.get(WEB_URL)
    getAPIKeyBtn = driver.find_element(By.XPATH, ".//a[contains(text(), 'Get free API key') ]")    
    assert getAPIKeyBtn.text == "Get free API key"
    getAPIKeyBtn.click()
    signUpH2Element = driver.find_element(By.XPATH, ".//h2")
    print(signUpH2Element.text)
    assert signUpH2Element.text == "Welcome to Finnhub.io"
    signupInputs = driver.find_elements(By.TAG_NAME, "input")    
    print(len(signupInputs))
    assert len(signupInputs) == 3
    print(signupInputs[0])
    nameInput = signupInputs[0].get_attribute("placeholder")
    print(nameInput)
    assert nameInput == "Name"
    emailInput = signupInputs[1].get_attribute("placeholder")
    print(emailInput)
    assert emailInput == "Email"
    passwordInput = signupInputs[2].get_attribute("placeholder")
    print(passwordInput)
    assert passwordInput == "Password"
'''
# A test that checks if the website title is correct
def test_APISignIn(driver):
    driver.get(WEB_URL)
    getAPIKeyBtn = driver.find_element(By.XPATH, ".//a[contains(text(), 'Login') ]")
    assert getAPIKeyBtn.text == "Login"
    getAPIKeyBtn.click()
    emailLogin = driver.find_element(By.XPATH, ".//input[@placeholder = 'Email']").send_keys(finnHub_username)
    emailPassword = driver.find_element(By.XPATH, ".//input[@placeholder = 'Password']").send_keys(finnHub_password)
    # submit btn had the weirdest selector because there are two a elements with text "Login"
    submitLoginBtn = driver.find_element(By.XPATH, ".//a[contains(text(), 'Login') and contains(@class, 'btn')]")
    submitLoginBtn.click()
    time.sleep(10)


'''
# A test that checks if the website has a joke section
def test_joke_section(driver):
    driver.get(WEB_URL)
    joke_section = driver.find_element_by_id("joke-section")
    assert joke_section.is_displayed()

# A test that checks if the website has a random joke button
def test_random_joke_button(driver):
    driver.get(WEB_URL)
    random_joke_button = driver.find_element_by_id("random-joke-button")
    assert random_joke_button.is_displayed()
'''