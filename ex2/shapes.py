############################################################
# FILE : shapes.pys
# WRITER : Yuval Dellus , yuval_dellus, 305211880
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION :  gives the area for a given shape base on user input
############################################################
import math

CHOOSE_SHAPE_MESSAGE = "Choose shape (1=circle, 2=rectangle, 3=trapezoid): "
CIRCLE = "1"
RECTANGLE = "2"
TRAPEZOID = "3"


def shape_area():
    """sort the user input and direct it to the right shape calculation"""
    shape = input(CHOOSE_SHAPE_MESSAGE)
    if shape == CIRCLE:
        return float(circle_area())
    elif shape == RECTANGLE:
        return float(rectangle_area())
    elif shape == TRAPEZOID:
        return float(trapezoid_area())
    else:
        return None


def circle_area():
    """calculate the shape of a circle"""
    r = int(input())
    circ_area = r ** 2 * math.pi
    return circ_area


def rectangle_area():
    """calculate the shape of a rectangle"""
    side_a = int(input())
    side_b = int(input())
    rec_area = side_a * side_b
    return rec_area


def trapezoid_area():
    """calculate the shape of a trapezoid"""
    base_a = int(input())
    base_b = int(input())
    height = int(input())
    trape_area = ((base_a + base_b)/2) * height
    return trape_area
