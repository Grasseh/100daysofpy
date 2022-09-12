from turtle import Turtle
import random

HEIGHT=600
WIDTH=600

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.move()

    def move(self):
        x = random.randint((WIDTH - 40) / - 2, (WIDTH - 40) / 2)
        y = random.randint((HEIGHT - 40) / - 2, (HEIGHT - 40) / 2)
        self.goto(x, y)
