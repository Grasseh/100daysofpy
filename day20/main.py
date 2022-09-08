from turtle import Turtle, Screen
import random
import time

HEIGHT=600
WIDTH=600
TIME_SLEEP=0.2

def create_square(x, y):
    new_turtle = Turtle()
    new_turtle.shape('square')
    new_turtle.color('white')
    new_turtle.penup()
    new_turtle.goto(x=x, y=y)
    return new_turtle

def create_starting_squares():
    squares = []
    for i in range(0, 3):
        x = 0 - 20 * i
        squares.append(create_square(x=x, y=0))
    return squares

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
screen.title('Snake')
snake = create_starting_squares()
playing = True
while playing:
    screen.update()
    time.sleep(TIME_SLEEP)
    for square in snake:
        square.forward(20)
screen.exitonclick()
