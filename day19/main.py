from turtle import Turtle, Screen
import random

HEIGHT=400
WIDTH=500
COLORS_LIST = [
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'purple'
]

def ask_for_input():
    entry = ''
    prompt = f"Which turtle will win the race?\n({', '.join(COLORS_LIST)}):"
    while not entry in COLORS_LIST:
        entry = screen.textinput('Make your bet.', prompt)
    return entry

def draw_lines(lines):
    lines.speed('fastest')
    lines.hideturtle()
    draw_line(x=(WIDTH - 100) / 2, y=HEIGHT / 2)
    draw_line(x=(WIDTH - 100) / 2 + 3, y=HEIGHT / 2)
    draw_line(x=(WIDTH - 100) / 2 + 6, y=HEIGHT / 2)
    draw_line(x=(WIDTH - 100) / -2, y=HEIGHT / 2)
    draw_line(x=(WIDTH - 100) / -2 - 3, y=HEIGHT / 2)
    draw_line(x=(WIDTH - 100) / -2 - 6, y=HEIGHT / 2)

def draw_line(x, y):
    lines.penup()
    lines.goto(x, y)
    lines.setheading(270)
    lines.pendown()
    lines.forward(HEIGHT)

def create_turtles(colors):
    color_count = len(colors)
    index = 0
    turtles = []
    for color in colors:
        turtles.append(create_turtle(start_y(index, color_count), colors[index]))
        index += 1
    return turtles

def start_y(index, count):
    race_height = (HEIGHT - 100)
    middle = race_height / 2
    return middle * -1 + (index * (race_height / (count - 1)))

def create_turtle(y, color):
    new_turtle = Turtle()
    new_turtle.shape('turtle')
    new_turtle.penup()
    new_turtle.color(color)
    lines.speed('slow')
    new_turtle.goto(x=(WIDTH / -2) + 20, y=y)
    return new_turtle

def race(turtles):
    winner = ''
    while winner == '':
        for turtle in turtles:
            turtle.forward(random.randint(0, 5))
            if turtle.position()[0] > ((WIDTH / 2) - 44):
                winner = turtle.color()
    return winner[0]

lines = Turtle()
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
bet = ask_for_input()
draw_lines(lines)
turtles = create_turtles(COLORS_LIST)
winner_turtle = race(turtles)
screen.bye()
print(f"The winner is {winner_turtle}")
if winner_turtle == bet:
    print("You won!")
else:
    print("You lost!")
