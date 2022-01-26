from turtle import Turtle, Screen
from random import randrange

screen = Screen()

screen_size = (900, 600)
turtle_color = ["gold", "purple", "red", "blue", "green"]
turtle_yaxis = [-200, -100, 0, 100, 200]
turtle_list = []
winner, is_race = "", True


def betturtle():
    betcolor = screen.textinput("Welcome to the Turtle race.", "Which turtle color will win the race?")
    return betcolor


bet = betturtle()
screen.setup(width=screen_size[0], height=screen_size[1], startx=None, starty=None)

for count in range(0, (len(turtle_color))):
    t_gold = Turtle()
    t_gold.shape("turtle")
    t_gold.color(turtle_color[count])
    t_gold.penup()
    t_gold.setpos((screen_size[0]/-2 + 20), turtle_yaxis[count])
    turtle_list.append(t_gold)

while is_race:
    for turtles in turtle_list:
        turtles.fd(randrange(0,20))
        if int(turtles.xcor()) > screen_size[0]/2:
            winner = turtles.pencolor()
            is_race = False
if winner == bet:
    print("You win.")
else: print(f"You loose.\nWinner is {winner}")

screen.exitonclick()