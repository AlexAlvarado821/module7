"""
Author: Alex Alvarado
Program: basic_list.py
Date: 10-11-20
Description: creates a list from user input and outputs the list.
"""



def make_list():
    """
    :return: returns a list created by user input
    """

    u_list = []
    for i in range(0, 3):
        try:
            u_input = int(get_input())

        except ValueError as err:
            print("Please enter a numerical value!")
        else:
            u_list.insert(i, u_input)
    return u_list




def get_input():
    u_input = input("please enter a number: ")
    return u_input



if __name__ == '__main__':
    test_list = make_list()
    print(test_list)

