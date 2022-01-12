from random import randrange
from art import art

HIGH_LEVEL = 5
EASY_LEVEL = 10

def set_level():
    choose_level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if choose_level == "easy":
        return EASY_LEVEL
    else:
        return HIGH_LEVEL

def check_num (guess, random_num, turns):
    if guess < random_num:
        print("Too low.")
        return turns -1
    elif guess > random_num:
        print("Too high.")
        return turns -1
    else:
        print(f"You got it! The answer was {random_num}")

print(art)
print ("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

random_num = randrange(1,100)

def guess_num():
    guess = 0
#    print(f"Random num: {random_num}")
    turns =  set_level()

    while guess != random_num:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_num(guess, random_num, turns)

        if turns == 0:
            print("You've out of guesses, you losse.")
            return
        elif guess != random_num:
            print("Guess again.")

guess_num()