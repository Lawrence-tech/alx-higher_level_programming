#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header.
"""

# Import the requests and sys modules
import requests
import sys

# Get the URL from the command line argument
url = sys.argv[1]

# Send a GET request to the URL and get the response
response = requests.get(url)

# Get the value of the X-Request-Id header
header = response.headers.get('X-Request-Id')

# Display the value of the X-Request-Id header
print(header)
