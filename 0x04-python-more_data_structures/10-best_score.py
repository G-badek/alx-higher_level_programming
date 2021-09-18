#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    maximun = -99999
    key = ""

    for k, v in a_dictionary.items():
        if v >= maximun:
            maximun = v
            key = k
    return key
