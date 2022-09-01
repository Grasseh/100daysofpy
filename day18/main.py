import colorgram
import turtle as turtle
import random

colors = colorgram.extract('image.jpg', 100)
colors_list = list(map(lambda x: (x.rgb[0], x.rgb[1], x.rgb[2]), colors))

the_turtle = turtle.Turtle()
the_turtle.speed('fastest')
the_turtle.penup()
turtle.colormode(255)

def draw_row(the_turtle):
    the_turtle.color(random.choice(colors_list))
    the_turtle.begin_fill()
    the_turtle.pendown()
    the_turtle.circle(10)
    the_turtle.penup()
    the_turtle.end_fill()
    the_turtle.forward(40)

for _ in range(5):
    for _ in range(10):
        draw_row(the_turtle)
    the_turtle.backward(40)
    the_turtle.left(90)
    the_turtle.forward(60)
    the_turtle.left(90)
    for _ in range(10):
        draw_row(the_turtle)
    the_turtle.backward(40)
    the_turtle.right(90)
    the_turtle.forward(20)
    the_turtle.right(90)

screen = turtle.Screen()
screen.exitonclick()
