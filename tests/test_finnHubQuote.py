import pytest
import requests
import pprint
import os
import time

from dotenv import load_dotenv
load_dotenv()

finnHub_API = os.getenv("finnHub_API")
finnHub_API_key = os.getenv("finnHub_API_key")

# A random API that returns a joke
API_URL = "https://official-joke-api.appspot.com/random_joke"


# Define a pytest_generate_tests function
def pytest_generate_tests(metafunc):
    # Check if the test function has a url argument
    if "stockTicker" in metafunc.fixturenames:
        # Apply the same parameter values to all test functions with a url argument
        metafunc.parametrize("stockTicker", ["AAPL", "SPY"])

# A function that makes a GET request to the API and returns the response
def quoteRequest(stockTickerInput):
    quoteRequestBuilder = ""
    quoteRequestBuilder += finnHub_API
    quoteRequestBuilder += "quote?symbol=" + stockTickerInput +"&token="
    quoteRequestBuilder += finnHub_API_key
    response = requests.get(quoteRequestBuilder)
    time.sleep(30) # to account for API usage limits
    return response


# A test that checks if the response status code is 200
def test_statusCode(stockTicker):
    response = quoteRequest(stockTicker)
    assert response.status_code == 200


# A test that checks if the response status code is 200
def test_contentKey(stockTicker):
    response = quoteRequest(stockTicker)
    responseJson = response.json() 
    expectedKeys = ("c", "d", "dp", "h", "l", "o", "pc", "t")
    keys_list = list(responseJson.keys())
    for expectedKey in expectedKeys:
        assert(expectedKey in keys_list)


# A test that ensures all quote response key-values are integers
# And checks that low is lower than high
# And checks that the dp percentage is correct.
def test_contentValues(stockTicker):
    response = quoteRequest(stockTicker)
    responseJson = response.json() 
    keys_list = list(responseJson.keys())
    for key in keys_list:
        assert(isinstance (responseJson[key], int) or isinstance (responseJson[key], float))
    if (responseJson['h'] < responseJson['l']):
        assert(False)
    multiplier = 1 + (responseJson['dp'] / 100)
    expectedClose = multiplier * responseJson['pc']
    expectedClose = round(expectedClose, 2)
    closePrice = responseJson['c']
    if (expectedClose != closePrice):
        assert(False)

'''
# this is kept to remember seeing JSON structure and pprint
def test_json():
    response = get_joke()
    print("response.json()")
    print(response.json())
    print("response.headers")
    print(response.headers)
    print("response.url")
    print(response.url)
    print("response.status_code")
    print(response.status_code)
    print("response.__dict__")
    #print(response.__dict__)
    pprint.pprint(response.__dict__)
    pprint.pprint(response.content)
    #print(response.headers)
    print("API_KEY")
    print(API_KEY)
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
'''