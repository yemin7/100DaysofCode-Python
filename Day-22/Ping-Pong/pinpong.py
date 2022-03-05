from turtle import Turtle

class PingPong(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("white")
        self.movespeed = 0.05
        self.x_move = 6
        self.y_move = 6

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.movespeed *= 0.8


    def reset(self):
        self.goto(0, 0)
        self.movespeed = 0.05
        self.bounce_x()