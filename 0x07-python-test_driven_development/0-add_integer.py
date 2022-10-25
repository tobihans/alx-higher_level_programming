#!/usr/bin/python3
"""
A module for addition.

It provides functions to perfom addition operations.

That's it.
"""

def add_integer(a, b=98):
  """Sums two int or floats together.

  A TypeError will be raised if one the arguments is not an int or a float
  """

  if not isinstance(a, (int, float)):
    raise TypeError("a must be an integer")

  if not isinstance(b, (int, float)):
    raise TypeError("b must be an integer")

  return int(a) + int(b)
