import pytest
from selenium import webdriver

# A random website that shows a joke
WEB_URL = "https://jokes.one/"

# A fixture that creates and returns a webdriver instance
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# A test that checks if the website title is correct
def test_title(driver):
    driver.get(WEB_URL)
    assert driver.title == "Jokes One - Jokes, Funny Videos, Funny Pictures"

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
