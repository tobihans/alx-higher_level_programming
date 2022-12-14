#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = (abs(number) % 10) * (-1 if number < 0 else 1)
prefix = f"Last digit of {number} is {last_digit} and is"

if number == 0:
    print(f"{prefix} 0")
elif last_digit > 5:
    print(f"{prefix} greater than 5")
elif number < 6 and number != 0:
    print(f"{prefix} less than 6 and not 0")
