from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280,250)
        self.write(f"Level {self.level}", font=FONT)
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level {self.level}", font=FONT)
    def score_up(self):
        self.level += 1
        self.update_scoreboard()
    def end_game(self):
        self.goto(0,0)
        self.write("Game over",align="center",font=FONT)

