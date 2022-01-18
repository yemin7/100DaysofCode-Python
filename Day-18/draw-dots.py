from turtle import Turtle, Screen
from random import choice

minion = Turtle()
screen = Screen()

screen.colormode(255)
minion.hideturtle()
minion.speed('fastest')
minion.up()

rgb_color = [(245, 243, 237), (248, 241, 244), (238, 240, 246), (201, 164, 112), (239, 246, 241), (152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44), (138, 31, 20)]
dots = 50

for i in range(1, dots):
    minion.dot(20, choice(rgb_color))
    minion.fd(50)

    if i %10 == 0:
        minion.setheading(90)
        minion.fd(50)
        minion.setheading(180)
        minion.fd(500)
        minion.setheading(0)
screen.exitonclick()