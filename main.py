import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager = CarManager()
tim = Player()

screen.listen()
screen.onkey(tim.move_up, "Up")
game_is_on = True
score = Scoreboard()
while game_is_on:
    time.sleep(0.1)
    car_manager.create()
    car_manager.move()
    if tim.result():
        score.level_up()
        car_manager.inc_speed()
    for car in car_manager.cars:
        if tim.distance(car) < 30:
            score.game_over()
            game_is_on = False
    screen.update()

screen.exitonclick()
