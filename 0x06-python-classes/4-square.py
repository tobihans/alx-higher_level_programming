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
        """Returns he square size"""
        return self._Square__size

    @size.setter
    def size(self, size):
        """Sets the square size"""
        if type(size) is int:
            if size > 0:
                self._Square__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns the are of the square."""

        return self._Square__size**2
