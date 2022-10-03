#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = argv[1:]
    length = len(args)

    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(length))

    for i, val in enumerate(args):
        print("{}: {}".format(i + 1, args[i]))
