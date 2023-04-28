#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
# First Import the urllib.request module
import urllib.request

# Create a Request object with the URL
req = urllib.request.Request('https://alx-intranet.hbtn.io/status')

# Open the URL and read the response
with urllib.request.urlopen(req) as response:
    # Get the content type of the response
    content_type = response.getheader('Content-Type')
    # Get the body of the response as bytes
    body = response.read()

# Display the body of the response
print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
print("\t- utf8 content: {}".format(body.decode('utf-8')))
