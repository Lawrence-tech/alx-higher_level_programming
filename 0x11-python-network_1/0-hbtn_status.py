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
    # Decode the body according to the content type
    if content_type == 'text/html; charset=utf-8':
        body = body.decode('utf-8')
    elif content_type == 'application/json':
        body = body.decode('json')
    else:
        # Use a default encoding if not specified
        body = body.decode()

# Display the body of the response
print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
print('\t- utf8 content: {}'.format(html.decode('utf8')))
