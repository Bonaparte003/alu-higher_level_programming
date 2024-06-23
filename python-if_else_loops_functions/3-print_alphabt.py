#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if i == ord('q') or i == ord('e'):
        i += 1
    else:
        print("{}".format(chr(i)), end='')
