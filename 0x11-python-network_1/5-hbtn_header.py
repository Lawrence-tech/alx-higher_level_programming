#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header.
"""

# Import the requests and sys modules
import requests
import sys


# Define a main function that takes the URL as an argument
def main(argv):
    """
    Method that takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id variable
    found in the header of the response
    """
    # Get the URL from the command line argument
    url = argv[1]
    # Send a GET request to the URL and get the response
    response = requests.get(url)
    # Get the value of the X-Request-Id header
    x_request_id = response.headers.get('X-Request-Id')
    # Print the value of the X-Request-Id header
    print("{}".format(x_request_id))


# Check if the script is run as the main program
if __name__ == "__main__":
    # Call the main function with argv[1] as the argument
    main(sys.argv)
