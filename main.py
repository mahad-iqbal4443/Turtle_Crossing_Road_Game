import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

STARTING_MOVE_DISTANCE = 0
screen = Screen()
screen.setup(width=600, height=600)
score = Scoreboard()
player = Player()
car = CarManager()
screen.tracer(0)
my_2 = Turtle()
my_2.hideturtle()
my_2.penup()
my_2.color("black")

s = screen.textinput("Level Selection", "Easy/Normal/Hard").lower()
if s == "easy":
    STARTING_MOVE_DISTANCE = 5
    game_is_on = True
elif s == "normal":
    STARTING_MOVE_DISTANCE = 7
    game_is_on = True
elif s == "hard":
    STARTING_MOVE_DISTANCE = 9
    game_is_on = True
else:
    my_2.write("Invalid Level entered", align="center", font=("Courier", 15, "normal"))
    game_is_on = False

while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkey(player.chal_aagy, "Up")
    score.inc_score(player.finished())
    car.naya_dabba()
    car.new_pos(STARTING_MOVE_DISTANCE)

    for naya_dabba in car.sary_ping:
        if naya_dabba.distance(player) < 20:
            my_2.showturtle()
            my_2.write(arg="Game Over", align="center", font=("Courier", 15, "normal"))
            game_is_on = False

    if player.finished():
        player.ghr_ja()
        STARTING_MOVE_DISTANCE += 2

screen.exitonclick()
