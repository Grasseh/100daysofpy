from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = self.create_starting_squares()

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            current_square = self.segments[i]
            next_square = self.segments[i - 1]
            current_square.goto(next_square.xcor(), next_square.ycor())
        self.head().forward(20)

    def create_square(self, x, y):
        new_turtle = Turtle()
        new_turtle.shape('square')
        new_turtle.color('white')
        new_turtle.penup()
        new_turtle.goto(x=x, y=y)
        return new_turtle

    def create_starting_squares(self):
        squares = []
        for i in range(0, 3):
            x = 0 - 20 * i
            squares.append(self.create_square(x=x, y=0))
        return squares

    def head(self):
        return self.segments[0]

    def up(self):
        if self.head().heading() % 180 == 0:
            self.head().setheading(90)

    def down(self):
        if self.head().heading() % 180 == 0:
            self.head().setheading(270)

    def left(self):
        if self.head().heading() % 180 == 90:
            self.head().setheading(180)

    def right(self):
        if self.head().heading() % 180 == 90:
            self.head().setheading(0)
