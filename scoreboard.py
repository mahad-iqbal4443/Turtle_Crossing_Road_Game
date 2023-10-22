from turtle import Turtle
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-250, 270)
        self.level = 1
        self.write(f"Level :{self.level}", align="center", font=FONT)

    def inc_score(self, num):
        self.clear()
        self.level += num
        self.write(f"Level :{self.level}", align="center", font=FONT)
