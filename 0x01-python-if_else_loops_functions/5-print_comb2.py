#!/usr/bin/python3

for n in range(99):
    print("{:0>2}".format(n), end=", " if n > 98 else "\n")
