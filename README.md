# stockComparisonAPI
Pytest that tests performance of various stock APIs
Python3 and pytest required

For Ubuntu, use command
1) Install dependencies.
Python
pytest
dotenv
Chrome
Chromedriver

2) Create environmental file

3) Command for running all tests
"python3 -m pytest -s --html=reporter.html"
4) Command for running single test
"python3 -m pytest -s tests/test_finnHubQuote.py --html=reporter.html"
GUI tests
"python3 -m pytest -s tests/test_website.py --html=reporter.html"

-s flag for displaying console messages

Reporter via pytest-html

Finnhub documentation
https://finnhub.io/docs/api/quote