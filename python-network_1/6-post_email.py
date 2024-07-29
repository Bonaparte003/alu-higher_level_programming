#!/usr/bin/python3
"""post an email"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    req = requests.post(url, data=data)
    print(req.text)
