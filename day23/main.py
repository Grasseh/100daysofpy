import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
score = Scoreboard(600)
hitbox = Player()
screen.onkey(hitbox.move, 'w')
screen.onkey(hitbox.move, 'Up')
cars = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.update_cars()
    if hitbox.is_at_wall():
        hitbox.start()
        score.add_level()
        cars.level_up()
    if cars.collision(hitbox.xcor(), hitbox.ycor()):
        game_is_on = False
    screen.update()

score.game_over()
screen.exitonclick()
