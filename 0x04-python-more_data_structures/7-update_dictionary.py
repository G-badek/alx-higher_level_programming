#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if not a_dictionary.get(key):
        a_dictionary.update({key: value})

    for k, v in a_dictionary.items():
        a_dictionary[k] = (v if k != key else value)

    return a_dictionary
