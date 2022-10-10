#!/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    results = []
    i = 0

    while i < list_length:
        try:
            results.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            results.append(0)
        except ZeroDivisionError:
            print("division by 0")
            results.append(0)
        except IndexError:
            print("out of range")
            results.append(0)
            break
        finally:
            i += 1

    results.extend([0] * max(0, (list_length - i - 1)))

    return results
