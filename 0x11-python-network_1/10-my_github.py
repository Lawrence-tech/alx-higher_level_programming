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
                            auth=HTTPBasicAuth(Lawrence-tech,
                                               github_pat_11AXVGSRA0aP2uIsQmGO
                                               Wj_5YoMSYDkd0Z9779BSQGsIbjkHtUf
                                               emtC9IRwiGF4EBw5HTC5RPD404QPXd
                                               r))
    try:
        profile_info = response.json()
        print(profile_info['id'])
    except ValueError:
        print('None')


if __name__ == "__main__":
    main(argv)
