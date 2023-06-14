import pytest
import requests
import pprint
import os

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
    return response
    
# A test that checks if the response status code is 200
def test_statusCode(stockTicker):
    print('hello')
    print(stockTicker)
    response = quoteRequest(stockTicker)
    pprint.pprint(response.json())    
    assert response.status_code == 200

'''
# A test that checks if the response status code is 200
def test_contentKey():
    response = quoteRequest()
    responseJson = response.json() 
    expectedKeys = ("c", "d", "dp", "h", "l", "o", "pc", "t")
    #print(expectedKeys)
    #print(responseJson['c'])
    #print(responseJson.items())
    #print(responseJson.keys())
    keys_list = list(responseJson.keys())
    #print(keys_list)
    for expectedKey in expectedKeys:
        #print(expectedKey)
        #print(expectedKey in keys_list)
        assert(expectedKey in keys_list)

# A test that ensures all quote response key-values are integers
# And checks that low is lower than high
# And checks that the dp percentage is correct.
def test_contentValues():
    response = quoteRequest()
    print("\n")
    pprint.pprint(response.json())
    #assert(False)


# A test that checks if the response is a valid JSON
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

# A test that checks if the response has the expected keys
def test_keys():
    response = get_joke()
    data = response.json()
    assert "id" in data
    assert "type" in data
    assert "setup" in data
    assert "punchline" in data
'''