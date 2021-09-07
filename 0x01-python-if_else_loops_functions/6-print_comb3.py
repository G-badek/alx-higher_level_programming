#!/usr/bin/python3
for num in range(0, 9):
    for ber in range(num + 1, 10):
        if num is 8 and ber is 9:
            print("{:d}{:d}".format(num, ber))
        else:
            print("{:d}{:d}".format(num, ber), end=", ")
