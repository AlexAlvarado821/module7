"""
Author: Alex Alvarado
Program: keyword_and_arguments.py
Date: 10-13-20
Description: accepts arguments and outputs name, gpa, and class name in a formatted string.
"""


def average_scores(*args, **kwargs):
    """

    :param args: accepts arguments
    :param kwargs: accepts arguments from tuples
    :return: returns a formatted string that includes the information from the parameters
    """

    # Use *args for average calculation
    total = 0
    for x in args:
        total += x

    average = total/len(args)


    return 'Result: name = {} gpa = {} course = {}'.format(kwargs['last_name'], average, kwargs['major'])

if __name__ == '__main__':
    info = average_scores(4, 3, 2, 4, first_name='Michelle', last_name='Alex', major='U.S Domination')
    print(info)







