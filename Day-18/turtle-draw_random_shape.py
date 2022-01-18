from turtle import Turtle, Screen
from random import choice


colors = ['chartreuse4', 'DarkGreen', 'aquamarine4', 'goldenrod3', 'MediumSeaGreen', 'DarkSeaGreen3', 'gray50', 'DeepSkyBlue4']

minion = Turtle()

minion.shape('classic')
for i in range(3,10):
    minion.color(choice(colors))
    degree = 360/i
    for _ in range(i):
        minion.forward(100)
        minion.left(degree)

screen = Screen()
screen.exitonclick()