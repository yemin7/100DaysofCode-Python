#https://bit.ly/32Mqy2p

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
    
while not at_goal():
    move()
    up()
    turn_right()
    down()
