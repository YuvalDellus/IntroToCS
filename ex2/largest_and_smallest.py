############################################################
# FILE : largest_and_smallest.py
# WRITER : Yuval Dellus , yuval_dellus, 305211880
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION :  returns the largest and smallest of three numbers
############################################################


def largest_and_smallest(num_1, num_2, num_3):

    """determines what are the largest and smallest of three numbers"""

    temp_min = what_is_min(num_1, num_2)  # check the largest of 2 numbers
    min_value = what_is_min(num_3, temp_min)  # check the largest of 2 numbers
    temp_max = what_is_max(num_1, num_2)  # check the smallest of 2 numbers
    max_value = what_is_max(num_3, temp_max)  # check the smallest of 2 numbers

    return max_value, min_value


def what_is_min(a, b):
    """assist function to determine what is min"""
    if a < b:
        return a
    else:
        return b


def what_is_max(a, b):
    """assist function to determine what is max"""
    if a > b:
        return a
    else:
        return b
