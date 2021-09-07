#!/usr/bin/python3
for letter in range(122, 96, -1):
    if letter % 2 == 0:
        print("{:c}".format(letter), end="")
    else:
        print("{:c}".format(letter - 32), end="")
