#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = argv[1:]

    print(sum([int(i) for i in args]))
