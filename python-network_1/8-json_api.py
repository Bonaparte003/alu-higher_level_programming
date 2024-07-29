#!/usr/bin/python3
"""sends the post"""
import sys
import requests


if __name__ == "__main__":
    le = "" if len(sys.argv) == 1 else sys.argv[1]
    pay = {"q": le}
    req = requests.post("http://0.0.0.0:5000/search_user", data=pay)
    try:
        res = req.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
