from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(1, 5)
        self.setheading(90)
        self.color("white")
        self.speed("fastest")
        self.goto(x, y)

    def up(self):
        self.setheading(90)
        self.forward(8)

    def down(self):
        self.setheading(270)
        self.forward(8)
