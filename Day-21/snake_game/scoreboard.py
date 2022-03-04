from tkinter import font
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.position = position
        self.color("white") 
        self.penup()
        self.hideturtle()
#        self.setpos(0, 330)
        self.setpos(0, position)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGNMENT, font=("Courier", 50, "normal"))

    def score_plus(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()