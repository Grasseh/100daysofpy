# Test 5
from turtle import Turtle, Screen
import random

the_turtle = Turtle()

def move_forward():
    the_turtle.forward(10)
def move_backward():
    the_turtle.backward(10)
def turn_left():
    the_turtle.left(10)
def turn_right():
    the_turtle.right(10)
def clear():
    the_turtle.clear()


screen = Screen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear)
screen.listen()
screen.exitonclick()
