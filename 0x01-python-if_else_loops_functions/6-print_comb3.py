#!/usr/bin/python3

for i, j in [(i, j) for i in range(10) for j in range(10)]:
    if i < j:
        print("{}{}".format(i, j), end=", " if f"{i}{j}" != "89" else "\n")
