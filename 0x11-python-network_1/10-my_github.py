#!/usr/bin/python3

"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

from sys import argv
import requests
from requests.auth import HTTPBasicAuth


def main(argv):
    """
    Script that takes your GitHub credentials (username and password) and
    uses the GitHub API to display your id.
    """
    user = argv[1]
    password = argv[2]
    response = requests.get('https://api.github.com/user',
                            auth=HTTPBasicAuth('Lawrence-tech',
                                               'ghp_r8CIQDYQJU1LmvA4EbmZMNU'
                                               'ijflJu33z11fq'))
    try:
        profile_info = response.json()
        print(profile_info['id'])
    except KeyError:
        print('Error: Could not retrieve user ID')


if __name__ == "__main__":
    main(argv)
