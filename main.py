import time
from turtle import Screen
from player import Player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("corssing game")
screen.tracer(0)
player=Player()
car_manager=CarManager()
score=Scoreboard()
screen.listen()
screen.onkey(player.go_up,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    #detecting collision with car
    for car in car_manager.all_car:
        if car.distance(player)<20:
            game_is_on=False
            score.game_over()
            #the game over message is shown up in the middle
    #detecting turtle reaches the other side
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.incrment_speed()
        score.increment_level()
screen.exitonclick()
