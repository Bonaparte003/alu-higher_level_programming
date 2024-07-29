#!/usr/bin/python3
"""use the github api"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    au = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get("https://api.github.com/user", auth=au)
    print(req.json().get("id"))
