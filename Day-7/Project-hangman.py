import random, hangman_words as hw

### Variables
words_list = hw.words_list
letter = random.choice(words_list)
char_list = []
blank = len(letter)
live = 6

char_list.extend("_" for i in range(len(letter)))

print(hw.logo)
### Function
def guess():
    global live
    user_guess = input("Guess the letter. ").lower()
    hw.clear_screen()

    if user_guess in char_list:
        print("You've already guessed ", user_guess)

    for char in range(len(letter)):
        if user_guess == letter[char]:
            char_list[char] = letter[char]

    if user_guess not in letter:
        same_char = user_guess
        live -= 1
        print("Your guess ", user_guess, "is not correct. You loose a life.")
        print(f"{hw.stages[5-live]}")

    print(' '.join(char_list))

### Condition
while blank > 0:
    guess()
    blank = char_list.count("_")
    if blank == 0:
        print("You Win")
    if live == 0:
        print ("You loose.\nCorrect word is " + '\033[1m' + letter + '\033[0m')
        break