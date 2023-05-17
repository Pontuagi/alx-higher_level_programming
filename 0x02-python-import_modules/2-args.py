#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    if length == 2:
        print("1 argument:")
    elif length == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(length - 1))
    i = 1
    while length > 1:
        print("{}: {}".format(i, argv[i]))
        i += 1
        length -= 1
