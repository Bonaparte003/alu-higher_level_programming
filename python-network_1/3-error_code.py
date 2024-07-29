#!/usr/bin/python3
"""
In takes a url, performs a request
and handles errors if any
"""

import urllib.request
import urllib.error
import sys

if __name__ == '__main__':
    """"STARTING THE PROCESS"""
    url = sys.argv[1]
    re = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(re) as response:
            content = response.read()
            print("{}".format(content.decode("utf-8")))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
    except urllib.error.URLError as e:
        print(e.reason)
