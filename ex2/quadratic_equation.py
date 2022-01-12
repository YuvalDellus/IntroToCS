############################################################
# FILE : equation_quadratic.pys
# WRITER : Yuval Dellus , yuval_dellus, 305211880
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION :  gives the answer of the root equation by user input
############################################################
import math

ENTER_COEFFICIENTS_MESSAGE = "Insert coefficients a, b, and c: "
NO_SOLUTIONS_MESSAGE = "The equation has no solutions"
ONE_SOLUTION_MESSAGE = "The equation has 1 solution:"
TWO_SOLUTIONS_MESSAGE = "The equation has 2 solutions:"


def quadratic_equation(a, b, c):
    """calculates the roots of the equation"""
    delta = b ** 2 - 4 * a * c
    if delta < 0:  # have no answer
        return None, None
    elif delta == 0:  # have 1 answer
        return -b/2*a, None
    elif delta > 0:  # have 2 answers
        root_1 = (-b + math.sqrt(delta)) / 2 * a
        root_2 = (-b - math.sqrt(delta)) / 2 * a
        return root_1, root_2


def quadratic_equation_user_input():

    """takes input from the user and return how many roots to the equation
    and their value"""

    raw_input = input(ENTER_COEFFICIENTS_MESSAGE)
    a, b, c = raw_input.split()  # split the input to different variable
    a, b, c = float(a), float(b), float(c)  # work with float for calculation
    if quadratic_equation(a, b, c) == (None, None):
        print(NO_SOLUTIONS_MESSAGE)
    else:
        first, second = quadratic_equation(a, b, c)  # first and second roots
        if second is None:
            print(ONE_SOLUTION_MESSAGE, first)
        else:
            print(TWO_SOLUTIONS_MESSAGE, first, "and", second)
