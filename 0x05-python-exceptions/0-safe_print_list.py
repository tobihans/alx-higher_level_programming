#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    count = 0
    while i < x:
        try:
            print(my_list[i], end='')
            count += 1
        except IndexError:
            print("\n", end="")
            break
        i += 1
    return count
