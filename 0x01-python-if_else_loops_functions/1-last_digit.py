#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
no = abs(number) % 10
if number < 0:
    no = -no
no_str = str(no)
if int(no) > 5:
    print(f"Last digit of {number} is {no_str} and is greater than 5")
elif int(no) == 0:
    print(f"Last digit of {number} is {no_str} and is 0")
elif int(no) < 6 and int(no) != 0:
    print(f"Last digit of {number} is {no_str} and is less "
          f"than 6 and not 0")
