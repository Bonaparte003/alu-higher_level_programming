#!/usr/bin/python3
"""
takes URL sends a request to the URL
Displays the body of the response
"""

import sys
import urllib.error
import urllib.request

if __main__ == "__name__":
    """handles errors"""
    url = sys.argv[1]
    try:
        with url.request.urlopen(url) as f:
            print(f.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"{e}")
