from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.sary_ping = []

    def naya_dabba(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            ping = Turtle("square")
            ping.penup()
            ping.shapesize(stretch_len=2)
            ping.goto(300, random.randint(-250, 250))
            ping.color(random.choice(COLORS))
            self.sary_ping.append(ping)

    def new_pos(self, num):
        for dabba in self.sary_ping:
            dabba.backward(num)
