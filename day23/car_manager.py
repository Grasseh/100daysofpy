from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_CHANCE = 0.5

class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def update_cars(self):
        if random.random() < CAR_CHANCE:
            self.cars.append(Car())
        for car in self.cars:
            car.forward(self.move_distance)

    def level_up(self):
        for car in self.cars:
            car.clear()
            car.ht()
        self.cars = []
        self.move_distance += MOVE_INCREMENT

    def collision(self, x, y):
        collided = False
        for car in self.cars:
            collided = collided or car.distance(x, y) < 20
        return collided


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(180)
        self.speed("fastest")
        self.shape("square")
        self.color(random.choice(COLORS))
        self.goto(300, random.randint(-300,301))
        self.shapesize(1, 2)
