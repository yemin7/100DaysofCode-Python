#https://bit.ly/338qTMh


def up():
    turn_left()
    move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def down():
    move()
    turn_right()
    move()
    turn_left()
    
for i in range(0,6):
    move()
    up()
    turn_right()
    down()
