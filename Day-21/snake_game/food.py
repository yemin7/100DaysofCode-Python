from turtle import Turtle
import random as rd

WIDTH= 800
HEIGHT= 800
WIDTH_MINUS = -(WIDTH/2)+20
WIDTH_PLUS= (WIDTH/2)-20
HEIGHT_MINUS= -(HEIGHT/2)+20
HEIGHT_PLUS= (HEIGHT/2)-20

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.color("green")
        self.speed("fastest")
        self.refresh(x_minus=WIDTH_MINUS, x_plus=WIDTH_PLUS, y_minus=HEIGHT_MINUS, y_plus=HEIGHT_PLUS)

    def refresh(self, x_minus, x_plus, y_minus, y_plus):
        random_x = rd.randint(x_minus, x_plus)
        #random_x = rd.randint(-230, 230)
        random_y = rd.randint(y_minus, y_plus)
        #random_y = rd.randint(-330, 330)
        self.goto(random_x, random_y)
