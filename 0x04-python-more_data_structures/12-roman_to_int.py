#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = maximun = 0
    for num in range(len(roman_string) - 1, -1, -1):
        if roman[roman_string[num]] >= maximun:
            number += roman[roman_string[num]]
        else:
            number -= roman[roman_string[num]]

        maximun = roman[roman_string[num]]

    return number
