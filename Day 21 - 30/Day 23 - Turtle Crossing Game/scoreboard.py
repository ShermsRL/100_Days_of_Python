from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Black")
        self.hideturtle()
        self.penup()
        self.level = 1

    def stage(self, level):
        self.goto(-280, 250)
        self.clear()
        self.write(f"Level: {level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
