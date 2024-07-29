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
    print("- {}".format(type(response.text)))
    print("- {}".format(response.text))
