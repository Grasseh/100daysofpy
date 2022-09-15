from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

HEIGHT=600
WIDTH=800
TIME_SLEEP=0.001

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
screen.title('PONG')
screen.tracer(0)
screen.listen()

left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)

screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')

score = Score(HEIGHT)
ball = Ball('right')

playing = True

while playing:
    time.sleep(TIME_SLEEP)
    ball.move()
    screen.update()

    if ball.hit_top_wall(HEIGHT):
        ball.bounce_ver()

    if ball.hit_paddle(left_paddle):
        ball.bounce_hor()

    if ball.hit_paddle(right_paddle):
        ball.bounce_hor()

    if ball.hit_right_wall(WIDTH):
        score.add_point_left()
        ball.ht()
        ball = Ball('right')

    if ball.hit_left_wall(WIDTH):
        score.add_point_right()
        ball.ht()
        ball = Ball('left')

screen.exitonclick()
