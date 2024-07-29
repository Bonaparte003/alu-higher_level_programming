#!/usr/bin/python3
"""sends a request"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    code = req.code
    if code >= 400:
        print(f"Error code: {code}")
    else:
        print(req.text)
