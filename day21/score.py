from turtle import Turtle

HEIGHT=600
WIDTH=600

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.color("green")
        self.speed("fastest")
        self.goto(-(WIDTH - 20) / 2, (HEIGHT - 40) / 2)
        self.score = 0
        self.display_score()

    def add_point(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font=('Arial', 12, 'normal'))

    def gameover(self):
        self.goto(0, 0)
        self.write('Game over!', align='center', font=('Arial', 24, 'normal'))
