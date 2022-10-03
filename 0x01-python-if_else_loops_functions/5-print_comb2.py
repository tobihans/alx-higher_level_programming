#!/usr/bin/python3

for n in range(100):
    print("{:0>2}".format(n), end=", " if n < 99 else "\n")
