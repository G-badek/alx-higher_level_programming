#!/usr/bin/python3
def uniq_add(my_list=[]):
    adding = 0

    for x in set(my_list):
        adding += x

    return adding
