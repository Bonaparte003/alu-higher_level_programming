#!/usr/bin/python3
""" documentation
- Fetches data from https://alu-intranet.hbtn.io/status
- uses urrlib module
"""

import urllib.request


url = "https://alu-intranet.hbtn.io/status"
if url.startswith("https://"):
	url = "https://alu-intranet.hbtn.io/status"

if __name__ == '__main__':
    with urllib.request.urlopen(url) as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
