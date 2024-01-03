#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastDigit = ((number * -1) % 10) * -1
else:
    lastDigit = number % 10

line1 = f"Last digit of {number:d} is {lastDigit:d}"

if lastDigit > 5:
    print(f"{line1} and is greater than 5")
elif lastDigit == 0:
    print(f"{line1} and is 0")
else:
    print(f"{line1} and is less than 6 and not 0")
