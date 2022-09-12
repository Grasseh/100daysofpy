from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import random
import time

HEIGHT=600
WIDTH=600
TIME_SLEEP=0.1

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
food = Food()
score = Score()

while playing:
    screen.update()
    time.sleep(TIME_SLEEP)
    snake.move()
    # check if food
    if snake.head().distance(food) < 15:
        food.move()
        snake.grow()
        score.add_point()
    # check if walldead
    if snake.hit_wall():
        playing = False
    # check if taildead
    if snake.hit_tail():
        playing = False

score.gameover()
screen.exitonclick()
