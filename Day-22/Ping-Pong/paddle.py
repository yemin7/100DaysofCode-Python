from turtle import Turtle

WIDTH = 5
HEIGHT = 1
MOVE_FORWARD = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.paddle_position(position)

    def paddle_position(self, position):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=HEIGHT, stretch_wid=WIDTH)
        self.goto(position)


    def up(self):
        new_y = self.ycor() + MOVE_FORWARD
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVE_FORWARD
        self.goto(self.xcor(), new_y)