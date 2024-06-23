#!/usr/bin/python3
for i in range(ord('a'), ord(123) + 1):
    if i == ord('q') or i == ord('e'):
        i+=1
    else:
        print("%c" %chr(i), end="")
