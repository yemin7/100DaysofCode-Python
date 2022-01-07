import random, hangman_words as hw

words_list = hw.words_list
letter = random.choice(words_list)
char_list = []
match = False

for char in range(len(letter)):
    char_list.append(letter[char])

for blank in range(1,len(letter)-1):
    char_list[blank] = "_"

print(' '.join(char_list))

def match_letter():
    count = 0
    user_guess = input("Guess the letter: ").lower()

    if len(user_guess) != len(letter):
        print (f"{len(letter)-len(user_guess)} is missing.")
    
    for guess in range(len(letter)):
        if user_guess[guess] == letter[guess]:
            char_list[guess] = user_guess[guess]
        else:
            char_list[guess] = "❌"
            count += 1

    letter_in_def = ''.join(char_list)

    if letter_in_def == letter:
        print ("Words match.")
    else:
        print(f'{count} characters wrong.')
        print(''.join(char_list))

user_letter = ''.join(char_list)

while not match:
    match_letter()
    if ''.join(char_list) == letter:
        match = True