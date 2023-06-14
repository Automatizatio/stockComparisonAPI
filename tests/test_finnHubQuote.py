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


# A function that makes a GET request to the API and returns the response
def quoteRequest():
    quoteRequestBuilder = ""
    quoteRequestBuilder += finnHub_API
    quoteRequestBuilder += "quote?symbol=AAPL&token="
    quoteRequestBuilder += finnHub_API_key
    response = requests.get(quoteRequestBuilder)
    return response
    
# A test that checks if the response status code is 200
def test_statusCode():
    response = quoteRequest()
    assert response.status_code == 200

# A test that checks if the response status code is 200
def test_contentKey():
    response = quoteRequest()
    print("\n")
    pprint.pprint(response.json())
    responseJson = response.json() 
    expectedKeys = ("c", "d", "dp", "h", "l", "o", "pc", "t")
    print(expectedKeys)
    print(responseJson['c'])
    #print(responseJson.items())
    #print(responseJson.keys())
    keys_list = list(responseJson.keys())
    print(keys_list)
    for expectedKey in expectedKeys:
        print(expectedKey)
        print(expectedKey in keys_list)
        assert(expectedKey in keys_list)
    '''
    for key, value in responseJson.items():
        print(key)
    '''
    #assert response.status_code == 200

'''
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