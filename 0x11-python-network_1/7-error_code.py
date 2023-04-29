#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the body of the response.
"""
# Import requests and sys modules
import requests
from sys import argv


def main(argv):
    """
    Sends a request to the passed URL and displays the body of the response.
    If the HTTP status code is greater than or equal to 400, prints: Error
    code: followed by the value of the HTTP status code
    """
    # Get the url from the command line argument
    url = argv[1]

    # Send a request to the url
    response = requests.get(url)

    # Check the status code of the response
    if response.ok:
        # Print the response text if the status code is OK
        print(response.text)
    else:
        # Print the error code if the status code is not OK
        print("Error code: {}".format(response.status_code))


if __name__ == "__main__":
    main(argv)
