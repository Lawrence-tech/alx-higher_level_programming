#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8).
"""

# First import the urllib and sys modules
import urllib.request
from sys import argv


def main(argv):
    """
    Takes a URL and an email, sends a POST request with the email as parameter
    and prints the response body (decoded in utf-8)
    """
    # Create a dictionary with the email as a key-value pair
    params = {'email': argv[2]}
    # Encode the dictionary into a query string
    query = urllib.parse.urlencode(params)
    # Convert the query string into bytes
    query = query.encode('utf8')
    # Get the URL from the command line argument
    url = argv[1]
    # Create a Request object with the URL and the query bytes
    req = urllib.request.Request(url, query)
    # Open the URL and read the response
    with urllib.request.urlopen(req) as response:
        # Get the response body as bytes
        body = response.read()
        # Decode the body using utf-8 and print it
        print("{}".format(body.decode('utf8')))


if __name__ == "__main__":
    main(argv)
