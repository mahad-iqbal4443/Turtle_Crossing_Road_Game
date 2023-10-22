from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.hideturtle()
        self.left(90)
        self.ghr_ja()
        self.showturtle()

    def chal_aagy(self):
        self.forward(MOVE_DISTANCE)

    def finished(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def ghr_ja(self):
        self.goto(STARTING_POSITION)
