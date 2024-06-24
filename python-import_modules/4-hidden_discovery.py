#!/usr/bin/python3
if __main__ == "__name__":
    import hidden_4
    for i in dir(hidden_4):
        if '__' not in i:
            print(i)
