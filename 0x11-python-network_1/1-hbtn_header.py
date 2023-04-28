#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
# First import the urllib.request and sys modules
import urllib.request
import sys

# Get the URL from the command line argument
url = sys.argv[1]

# Create a Request object with the URL
req = urllib.request.Request(url)

# Open the URL and read the response
with urllib.request.urlopen(req) as response:
    # Get the value of the X-Request-Id header
    x_request_id = response.getheader('X-Request-Id')

# Display the value of the X-Request-Id header
print(x_request_id)
