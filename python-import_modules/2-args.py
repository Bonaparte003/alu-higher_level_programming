#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = len(sys.argv) - 1
    if (a == 0):
        print("0 arguments.")
    elif (a == 1):
        print(a, "argument:")
    else:
        print(a, "arguments:")
    for i in range(a):
        print("{}: {}".format((i + 1), (sys.argv[i + 1])))
