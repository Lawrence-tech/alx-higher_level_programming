#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""

# Import urllib.request and sys modules
import urllib.request
from sys import argv


def main(argv):
    """
    Method that handles urllib.error.HTTPError exceptions and
    prints: Error code: followed by the HTTP status code
    """
    # Get the URL from the command line argument
    url = argv[1]
    # Create a Request object with the URL
    request = urllib.request.Request(url)
    try:
        # Open the URL and read the response
        with urllib.request.urlopen(request) as response:
            # Get the response body as bytes
            body = response.read()
            # Decode the body using utf-8 and print it
            print("{}".format(body.decode('utf8')))
    except urllib.error.URLError as e:
        # Print the error code if an exception occurs
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    main(argv)
