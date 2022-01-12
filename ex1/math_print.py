############################################################
# FILE : math_print.py
# WRITER : Yuval Dellus , yuval_dellus, 305211880
# EXERCISE : intro2cs ex1 2016-2017
# DESCRIPTION :  calculate different mathematical questions
############################################################

import math


def golden_ratio():
    """Returns the golden ratio"""
    print((1 + math.sqrt(5)) / 2)

def square_five():
    """Returns the the value of fifth to the second power"""
    print(math.pow(5,2))

def hypotenuse():
    """Returns the value of the hypotenuse of a triangle with sides of 4 and 5"""
    print(math.hypot(4,5))

def pi():
    """Returns the value of pi"""
    print(math.pi)

def e():
    """Returns the value of e"""
    print(math.e)

def squares_area():
    """take a side of a square and multiply it by itself to get the area of the square"""
    print(1**1,2**2,3**2,4**2,5**2,6**2,7**2,8**2,9**2,10**2)