from turtle import Turtle
PADDLE_WIDTH = 1
PADDLE_LENGTH = 5
MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LENGTH)
        self.penup()
        self.goto(position)

    def up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)

    