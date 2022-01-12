############################################################
# FILE : bmi.py
# WRITER : Yuval Dellus , yuval_dellus, 305211880
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION :  calculate the BMI and return if it's in the health range or not
############################################################

min_bmi = 18.5
max_bmi = 24.9

def is_normal_bmi(weight, height):

    """calculate the BMI and return if it's in the health range or not"""

    if height == 0:  # I believe you have bigger problems if your height is 0 than your BMI
        return None
    bmi = weight/height**2  # BMI calculation
    if min_bmi <= bmi <= max_bmi:  # The range of healthy BMI
        return True
    else:
        return False
