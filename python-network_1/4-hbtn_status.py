#!/usr/bin/python3
"""
uses the request package to handle
request
"""

import requests


if __name__ == "__main__":
    """let's go!"""
    response = requests.get("https://alu-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- {}".format(type(response.text)))
    print("\t- {}".format(response.text))
