"""
Author: Alex Alvarado
Program: sort_and_search_list.py
Date: 10-9-20
Description: The program will sort and search a list based on its alphabetical order.
"""




def sort_list(sort):
    """

    :param sort: the list that will be sorted
    :return: returns the sorted list
    """
    List = ["Ally", "George", "Kyle", "Cale", "Fernando", "Bailey", "Zane"]
    if (sort == "forward"):

        return (sorted(List))
    else:
        return(sorted(List, reverse=True))



def search_list(target):
    """

    :param target: the target that the function is looking for
    :return: message declaring if the target was found or not
    """
    # the first letter of the target used to identify the best way to sort the list.
    sorted_list = []
    first_target = target[:1]
    if first_target < 'n':
        sorted_list = sort_list("forward")

    else:
        sorted_list = sort_list("reverse")


    for i in range(len(sorted_list)):
        if sorted_list[i] == target:
            return "The target is located in the list"

    return "The target is not located in the list"



if __name__ == '__main__':
    print(search_list("Kyle"))

