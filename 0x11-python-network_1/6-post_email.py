#!/usr/bin/python3
"""
 Python script that takes in a URL and an email address, sends a POST request
 to the passed URL with the email as a parameter, and finally displays the
 body of the response.
"""

# Import requests and sys modules
import requests
from sys import argv


def main(argv):
    """
    Sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
    """
    # Get the url and email from the command line arguments
    url = argv[1]
    email = argv[2]

    # Create a dictionary with the email as a key-value pair
    data = {'email': email}

    # Send a POST request to the url with the data
    response = requests.post(url, data=data)

    # Print the response text
    print(response.text)


if __name__ == "__main__":
    main(argv)
