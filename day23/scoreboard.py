from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, height):
        super().__init__()
        self.penup()
        self.ht()
        self.speed("fastest")
        self.goto(-300, (height - 100) / 2)
        self.score = 1
        self.display_score()

    def add_level(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Level : {self.score}", align='left', font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game over!", align='center', font=FONT)
