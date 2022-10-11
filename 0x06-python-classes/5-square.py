#!/usr/bin/python3
"""Classes

This contains some classes definitions.
"""


class Square:
    """A class to represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        self._Square__position = position

        if type(size) is int:
            if size > 0:
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

    @property
    def position(self):
        return self._Square__position

    @position.setter
    def position(self, position):
        is_0_int = type(position[0]) is int
        is_1_int = type(position[1]) is int

        if type(position) is not tuple or not is_0_int or not is_1_int:
            raise TypeError("position must be a tuple of 2 positive integers")

        self._Square__position = position

    def area(self):
        return self._Square__size ** 2

    def my_print(self):
        print(
            "\n".join(['#' * self._Square__size for _ in range(self._Square__size)]))
