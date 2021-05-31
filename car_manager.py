from turtle import Turtle
from random import *

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_COR = []
for i in range(-230, 250, 40):
    Y_COR.append(i)
print(Y_COR)


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create(self):
        chance = randint(1, 6)
        if chance == 6 or chance == 3:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(choice(COLORS))
            car.penup()
            car.setx(300)
            car.sety(choice(Y_COR))
            car.setheading(180)

            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed)

    def inc_speed(self):
        self.speed += MOVE_INCREMENT
