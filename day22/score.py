from turtle import Turtle

class Score(Turtle):
    def __init__(self, height):
        super().__init__()
        self.penup()
        self.ht()
        self.color("green")
        self.speed("fastest")
        self.goto(0, (height - 100) / 2)
        self.left_score = 0
        self.right_score = 0
        self.display_score()

    def add_point_left(self):
        self.left_score += 1
        self.display_score()

    def add_point_right(self):
        self.right_score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"{self.left_score} -- {self.right_score}", align='center', font=('Courier', 30, 'normal'))
