#!/usr/bin/python3
"""scipt that intakes the url"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as ans:
            print(ans.read().decode('UTF-8'))
    except error.HTTPError as e:
        print('Error code:', e.code)
