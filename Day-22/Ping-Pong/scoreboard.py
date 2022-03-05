from turtle import Turtle

ALIENMENT = "center"
FONT = ("Courier", 50, "normal")

class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.position = position
        self.color("white")
        self.penup()
        self.hideturtle()
        self.scoreboard(self.position)

    def l_point(self):
        self.l_score += 1
        self.scoreboard(self.position)

    def r_point(self):
        self.r_score += 1
        self.scoreboard(self.position)

    def scoreboard(self, position):
        self.clear()
        self.setpos(80, position)
        self.write(self.r_score, align=ALIENMENT, font=FONT)
        self.setpos(-80, position)
        self.write(self.l_score, align=ALIENMENT, font=FONT)
#        self.write(f"{self.r_score} : {self.l_score}", align=ALIENMENT, font=FONT)


    def player_win(self, player):
        self.goto(0, 0)
        self.write(f"{player} WIN!", align=ALIENMENT, font=FONT)