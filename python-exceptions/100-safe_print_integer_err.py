#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (IndexError, TypeError) as error:
        print("Exception:", error, file=sys.stderr)
        return False
