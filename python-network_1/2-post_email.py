#!/usr/bin/python3
"""
script that intakes URL and email for CLI
sends a POST request to the passed URL
"""

import sys
import urllib.request
import urllib.parse

if __name__ == '__main__':
    """START"""
    email = sys.argv[2]
    url = sys.argv[1]
    data = urllib.parse.urlencode({'email': email}).encode("utf-8")
    request = urllib.request.Request(url, data=data, method="POST")
    with urllib.request.urlopen(request) as f:
        print(f.read().decode("utf-8"))
