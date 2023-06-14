from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=260)
        self.update_score()

    def update_score(self):
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def increase_score(self):
        self.clear()
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align='center', font=FONT)