"""
Author: Alex Alvarado
Program: sort_and_search_array.py
date: 10-11-20
description: sorts through an array looking for a target value and outputs if it found the value.
"""


import array as arr
found_msg = "The target was found"
not_found_msg = "The target was not found"


def sort_array(input_array):
    """

    :param input_array:
    :return: returns a sorted list
    """
    return(sorted(input_array))
    #uses the return because this function serves one purpose that aids the other function.


def search_array(target):
    my_array = arr.array('i', [1, 3, -1, 27, 56, 11])
    sorted_array = sort_array(my_array.tolist())

    try:
        index = sorted_array.index(target)
    except ValueError:
        return -1
    else:
        return index


if __name__ == '__main__':
    search_array(20)

