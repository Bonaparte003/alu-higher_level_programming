#!/usr/bin/python3
"""sends request to the url and displays the values"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as answer:
        print(dict(answer.headers).get("X-Request-Id"))
