from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(0, 260)
        self.score = 0
        with open("data.txt") as file:
            self.high_score = file.read()
        self.total_score()

    def total_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align="Center", font=("Arial", 20, 'normal'))

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.total_score()

    def update_score(self):
        self.score += 1
        self.total_score()

    # def game_over(self):
    #     self.setposition(0, 0)
    #     self.write("Game Over.", False, align="Center", font=("Arial", 20, 'normal'))

