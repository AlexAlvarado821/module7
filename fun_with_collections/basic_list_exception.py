"""
Author: Alex Alvarado
Program: basic_list_exceptions.py
Date: 10-11-20
Description: creates a list from user input and outputs the list, while handling exceptions.

"""


def make_list():
    """
    :return: returns a list created by user input
    """

    u_list = []
    for i in range(0, 3):
        try:
            u_input = int(get_input())
            if u_input < 1 or u_input > 50:
                raise ValueError
        except ValueError:
            raise ValueError
        else:
            u_list.insert(i, u_input)
    return u_list


def get_input():
    u_input = input("please enter a number: ")
    return u_input


if __name__ == '__main__':
    test_list = make_list()
    print(test_list)

