#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
# First import the urllib.request and sys modules
import urllib.request
from sys import argv


def main(argv):
    """
    Method that takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id variable
    found in the header of the response
    """
    url = argv
    with urllib.request.urlopen(url) as response:
        header = response.info()
        print(header['X-Request-Id'])


if __name__ == "__main__":
    main(argv[1])
