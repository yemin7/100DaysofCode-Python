import time
from turtle import Screen
from paddle import Paddle
from pinpong import PingPong
from scoreboard import Score

WIDTH = 800
HEIGHT = 600
X_POS_PLUS = (WIDTH/2)-50
X_POS_MINUS = (-WIDTH/2)+50
Y_POS_PLUS = (HEIGHT/2)-50
Y_POS_MINUS = (-HEIGHT/2)+50
is_move = True

screen = Screen()
screen.bgcolor("black")
screen.title("Ping Pong")
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

r_paddle = Paddle((X_POS_PLUS, 0))
l_paddle = Paddle((X_POS_MINUS, 0))
pingpong = PingPong()
score = Score(Y_POS_PLUS)

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

while is_move:
    screen.update()
    time.sleep(pingpong.movespeed)
    pingpong.move()

    #Detect collision with Wall
    if pingpong.ycor() < (-HEIGHT/2)+20 or pingpong.ycor() > (HEIGHT/2)-20:
        pingpong.bounce_y()

    #Detect collision with Paddle
    if (pingpong.distance(r_paddle) < 50 and pingpong.xcor() > X_POS_PLUS-20) or (pingpong.distance(l_paddle) < 50 and pingpong.xcor() < X_POS_MINUS+20):
        pingpong.bounce_x()

    '''Detect pingpong goes out of bounds'''
    #Detect L paddle misses
    if pingpong.xcor() < (-WIDTH/2):
        score.r_point()
        pingpong.reset()
        if score.r_score > 5:
            is_move = False
            score.player_win("RIGHT")

    #Detect R paddle misses
    elif pingpong.xcor() > (WIDTH/2):
        score.l_point()
        pingpong.reset()
        if score.l_score > 5:
            is_move = False
            score.player_win("LEFT")

screen.exitonclick()