#!/usr/bin/python3
def fizzbuzz():
    for key in range(1, 101):
        if key % 5 == 0 and key % 3 == 0:
            print("FizzBuzz ", end="")
        elif key % 5 == 0:
            print("Buzz ", end="")
        elif key % 3 == 0:
            print("Fizz ", end="")
        else:
            print("{:d} ".format(key), end="")
