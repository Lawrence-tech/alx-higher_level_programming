#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""

# Import the requests module
import requests

# Send a GET request to the URL and get the response
response = requests.get('https://alx-intranet.hbtn.io/status')

# Get the body of the response as a string
body = response.text

# Display the body of the response
print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
