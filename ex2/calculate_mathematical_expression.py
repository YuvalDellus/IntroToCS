############################################################
# FILE : calculate_mathematical_expression.py
# WRITER : Yuval Dellus , yuval_dellus, 305211880
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION : Do simple mathematical manipulations
############################################################


def calculate_mathematical_expression(number_1, number_2, operator):
    """calculate two numbers with one of the four operators + , - , * , /"""
    if operator == "+":
        summation = number_1 + number_2
        return summation

    elif operator == "-":
        difference = number_1 - number_2
        return difference

    elif operator == "*":
        product = number_1 * number_2
        return product

    elif operator == "/":
        if number_2 == 0:  # can't devise by 0
            return None
        else:
            quotient = number_1/number_2
            return quotient

    else:
        return None  # Illegal operator won't calculate


def calculate_from_string(question):
    """the function will return an answer for a calculae asked by string"""
    number_1, operator, number_2 = question.split()
    number_1 = float(number_1)
    operator = str(operator)
    number_2 = float(number_2)
    return calculate_mathematical_expression(number_1, number_2, operator)
