from os import minor
from turtle import Turtle, Screen
from random import choice

minion = Turtle()
screen = Screen()
screen.colormode(255)
minion.speed("fastest")

radius = 100
gap = 5

def random_color():
    r = choice(range(0,255))
    g = choice(range(0,255))
    b = choice(range(0,255))
    random_color = (r, g, b)
    return random_color


for i in range(int(360/gap)):
    minion.color(random_color())
    minion.circle (radius)
    minion.setheading(minion.heading() + gap)



screen.exitonclick()