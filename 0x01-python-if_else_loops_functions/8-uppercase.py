#!/usr/bin/python3

def uppercase(str):
    caps = ''
    for char in str:
        if 'a' <= char <= 'z':
            upper_case = chr(ord(char) - ord('a') + ord('A'))
            caps += upper_case
        else:
            caps += char
    print (caps)
