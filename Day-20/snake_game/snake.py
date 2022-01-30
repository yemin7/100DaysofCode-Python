from tkinter import LEFT
from turtle import Turtle

POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
#        self.position = [(0,0), (-20, 0), (-40, 0)]
        self.new_position = []
        self.snake_position()
        self.head = self.new_position[0]

    def snake_position(self):
        for i in POSITIONS:
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(i)
            self.new_position.append(snake)
#        return self.new_position

    def move(self):
        for seg in range((len(self.new_position)-1), 0 , -1):
            new_x = self.new_position[seg-1].xcor()
            new_y = self.new_position[seg-1].ycor()
            self.new_position[seg].goto(new_x, new_y)
        self.head.fd(MOVE_FORWARD)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)