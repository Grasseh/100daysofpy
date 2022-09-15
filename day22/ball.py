from turtle import Turtle
import random

START_SPEED = 0.4

class Ball(Turtle):
    def __init__(self, ball_direction):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 0)
        self.move_speed = START_SPEED

        if ball_direction == 'left':
            random = self.random_left()
        else:
            random = self.random_right()

        self.setheading(random)

    def random_left(self):
        return random.randint(105, 256)

    def random_right(self):
        if random.randint(0, 2) == 0:
            return random.randint(15, 76)

        return random.randint(285, 346)

    def move(self):
        self.forward(self.move_speed)

    def hit_top_wall(self, HEIGHT):
        y = self.ycor()
        return abs(y) > ((HEIGHT / 2) - 20)

    def hit_right_wall(self, WIDTH):
        x = self.xcor()
        return x > ((WIDTH / 2) - 20)

    def hit_left_wall(self, WIDTH):
        x = self.xcor()
        return x < -((WIDTH / 2) - 20)

    def hit_paddle(self, paddle):
        return abs(self.xcor() - paddle.xcor()) < 20 and self.distance(paddle) < 50

    def bounce_ver(self):
        current = self.heading()
        new = 360 - current
        self.setheading(new)

    def bounce_hor(self):
        current = self.heading()
        new = (180 - current) % 360
        valid = False
        quadrant = new / 4
        variation = 0

        while not valid:
            variation = random.randint(-45, 45)
            valid = ((new + variation) / 4) == quadrant
        new += variation

        self.move_speed += 0.05
        self.setheading(new)
