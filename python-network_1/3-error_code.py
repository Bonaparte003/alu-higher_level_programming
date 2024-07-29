#!/usr/bin/python3i
"""
takes URL sends a request to the URL
Displays the body of the response
"""

import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    """handles errors"""
    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as f:
            print(f.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
    except urllib.error.URLError as n:
        print(n.reason)
