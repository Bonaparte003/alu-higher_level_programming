#!/usr/bin/python3
"""
sends a request to url and
displays the value of the
X-Requests-Id
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    print("{}".format(res.headers.get("X-Requests-Id")))
