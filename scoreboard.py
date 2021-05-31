from turtle import Turtle
FONT = ("Courier", 24, "normal")
STARTING_LEVEL = 1

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-260,260)
        self.level = STARTING_LEVEL
        self.pencolor("black")
        self.write(f"Level = {self.level}",font=FONT,align="left")
        self.hideturtle()

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level = {self.level}",font=FONT,align="left")

    def game_over(self):
        self.home()
        self.write("Game Over!",font=FONT,align="center")