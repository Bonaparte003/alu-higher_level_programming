#!/usr/bin/python3
"""scipt that intakes the url"""

from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


if __name__ == "__main__":
    "lets begin"
    url = argv[1]
    req = Request(url)

    try:
        with urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
    except URLError as e:
        print(e.reason)
