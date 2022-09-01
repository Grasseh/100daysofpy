# Test 5
from turtle import Turtle, Screen
import random

the_turtle = Turtle()
the_turtle.speed('fastest')

def random_color():
    return (random.random() / 1.0, random.random() / 1.0, random.random() / 1.0)

for _ in range(36):
    the_turtle.color(random_color())
    the_turtle.circle(50, 360, 50)
    the_turtle.left(10)

screen = Screen()
screen.exitonclick()

# Test 4
# from turtle import Turtle
# import random

# the_turtle = Turtle()
# the_turtle.width(5)
# the_turtle.speed('fastest')

# def angle():
#     return 90 * random.randint(0, 4)

# def random_color():
#     return (random.random() / 1.0, random.random() / 1.0, random.random() / 1.0)

# for _ in range(250):
#     the_turtle.color(random_color())
#     the_turtle.right(angle())
#     the_turtle.forward(20)

# Test 3
# from turtle import Turtle
# import random

# the_turtle = Turtle()

# def angle(side_count):
#     return 180 - (180 * (side_count - 2)) / side_count

# def random_color():
#     return (random.random() / 1.0, random.random() / 1.0, random.random() / 1.0)

# for side_count in range(3, 11):
#     the_turtle.color(random_color())
#     this_angle = angle(side_count)
#     for _ in range(side_count):
#         the_turtle.forward(100)
#         the_turtle.right(this_angle)

# Test 2

# from turtle import Turtle

# the_turtle = Turtle()
# the_turtle.color('black')
# for _ in range(15):
#     the_turtle.pendown()
#     the_turtle.forward(10)
#     the_turtle.penup()
#      the_turtle.forward(10)

# Test 1

# from turtle import Turtle

# the_turtle = Turtle()
# the_turtle.color('black')
# the_turtle.begin_fill()
# while True:
#     the_turtle.forward(200)
#     the_turtle.left(90)
#     the_turtle.forward(200)
#     the_turtle.left(90)
#     the_turtle.forward(200)
#     the_turtle.left(90)
#     the_turtle.forward(200)
#     the_turtle.left(90)
#     break

# the_turtle.end_fill()
