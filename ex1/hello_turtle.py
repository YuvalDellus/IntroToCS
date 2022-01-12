############################################################
# FILE : hello_turtle.py
# WRITER : Yuval Dellus , yuval_dellus, 305211880
# EXERCISE : intro2cs ex1 2016-2017
# DESCRIPTION :  draw a bed of flower using turtle function
############################################################

import turtle


def draw_petal():
    """this function draws one pental"""
    turtle.forward(30)
    turtle.left(45)
    turtle.forward(30)
    turtle.left(135)
    turtle.forward(30)
    turtle.left(45)
    turtle.forward(30)
    turtle.left(135)

def draw_flower():
    """this function draws four pentals in a form of a flower"""
    turtle.right(45)
    draw_petal()
    turtle.right(90)
    draw_petal()
    turtle.right(90)
    draw_petal()
    turtle.right(90)
    draw_petal()
    turtle.right(135)
    turtle.forward(150)

def draw_flower_advanced():
    """this function draws one flower and move the turtle as perparation to draw another flower"""
    draw_flower()
    turtle.left(90)
    turtle.up()
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.down()

def draw_flower_bed():
    """this function move us to the right position and will drwa three flowers side by side"""
    turtle.up()
    turtle.left(180)
    turtle.forward(200)
    turtle.right(180)
    turtle.down()
    draw_flower_advanced()
    draw_flower_advanced()
    draw_flower_advanced()
