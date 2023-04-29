#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

# Import the requests and sys modules
import requests
from sys import argv


def main(argv):
    """
    Takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
    The letter must be sent in the variable q
    If no argument is given, set q=""
    If the response body is properly JSON formatted and not empty, display
    the id and name like this: [<id>] <name>
    Otherwise:
    Display Not a valid JSON if the JSON is invalid
    Display No result if the JSON is empty
    """
    # Get the letter from the command line argument or set it to ""
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]

    # Create a dictionary with the letter as a key-value pair
    data = {'q': q}

    # Send a POST request to the url with the data
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data=data)

    # Try to parse the response as JSON
    try:
        result = response.json()
        # Check if the result is empty
        if result:
            # Display the id and name
            print("[{}] {}".format(result['id'], result['name']))
        else:
            # Display no result
            print("No result")
    except ValueError:
        # Display not a valid JSON
        print("Not a valid JSON")


if __name__ == "__main__":
    main(argv)
