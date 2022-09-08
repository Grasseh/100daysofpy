from turtle import Turtle, Screen
from snake import Snake
import random
import time

HEIGHT=600
WIDTH=600
TIME_SLEEP=0.2

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)
snake = Snake()

playing = True

screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.left, 'a')
screen.onkey(snake.down, 's')
screen.onkey(snake.right, 'd')
screen.onkey(snake.up, 'Up')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')

while playing:
    screen.update()
    time.sleep(TIME_SLEEP)
    snake.move()

screen.exitonclick()
