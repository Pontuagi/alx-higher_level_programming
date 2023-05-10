#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
no_str = str(number)
no = len(no_str)
if int(no_str[no - 1]) > 5:
    print(f"Last digit of {number} is {no_str[no - 1]} and is greater than 5")
elif int(no_str[no - 1]) == 0:
    print(f"Last digit of {number} is {no_str[no - 1]} and is 0")
elif int(no_str[no - 1]) < 6 and int(no_str[no - 1]) != 0:
    print(f"Last digit of {number} is {no_str[no - 1]} and is less "
          f"than 6 and not 0")
