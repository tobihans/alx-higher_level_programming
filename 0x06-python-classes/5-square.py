#!/usr/bin/python3
"""Classes

This contains some classes definitions.
"""


class Square:
    """A class to represent a square."""

    def __init__(self, size=0):
        if type(size) is int:
            if size >= 0:
                self._Square__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, size):
        if type(size) is int:
            if size > 0:
                self._Square__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self._Square__size ** 2

    def my_print(self):
        print(
            "\n".join(['#' * self._Square__size for _ in range(self._Square__size)]))
