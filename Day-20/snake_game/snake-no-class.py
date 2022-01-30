from turtle import Turtle, Screen
import turtle, time


#snake = Turtle("square")
screen = Screen()
is_move = True

def moveforward():
    snake.fd(10)

screen.title("Snake Game")
screen.setup(width=500,height=700)
screen.bgcolor("black")
screen.tracer(0)

positions = [(0,0), (-20, 0), (-40, 0)]
new_position = []


for i in positions:
#    snake.goto(-((i+10)+10),0)
    snake = Turtle("square")
    snake.color("white")
    snake.penup()
    snake.goto(i)
    new_position.append(snake)

while is_move:
    screen.update()
    time.sleep(0.1)

    for seg in range((len(new_position)-1), 0, -1): #from new_positions range
        new_x = new_position[seg-1].xcor()
        new_y = new_position[seg-1].ycor()
        new_position[seg].goto(new_x, new_y)
    new_position[0].fd(20)
    new_position[0].left(90)


#screen.listen()
screen.exitonclick()