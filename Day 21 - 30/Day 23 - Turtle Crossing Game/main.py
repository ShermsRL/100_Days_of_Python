import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

CARS = []

RANDOM_Y = random.randint(-250, 250)

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Creating objects
player = Player()
scoreboard = Scoreboard()


# Screen Event
screen.listen()
screen.onkeypress(player.move, "Up")

loop = 0
speed = 5
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.stage(scoreboard.level)

    if player.ycor() == 280:
        scoreboard.level += 1
        player.new_stage()
        speed += 5

    loop += 1

    if loop == 6:
        car = CarManager()
        CARS.append(car)
        loop = 0

    for car in CARS:
        car.car_move(speed)
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False





screen.exitonclick()
