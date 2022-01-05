import random
lower_case_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_case_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#lower_case = upper_case = numbers = symbols = ''
letters = ''

print("Welcome to the PyPassword Generator!")
lower_input = int(input("How many lower case letters would you like in your password?\n")) 
upper_input = int(input("How many upper case letters would you like in your password?\n")) 
symbols_input = int(input(f"How many symbols would you like?\n"))
numbers_input = int(input(f"How many numbers would you like?\n"))

for lower_count in range(lower_input):
#    lower_case += random.choice(lower_case_list)
    letters += random.choice(lower_case_list)

for upper_count in range(upper_input):
#    upper_case += random.choice(upper_case_list)
    letters += random.choice(upper_case_list)

for symbol_count in range(symbols_input):
#    symbols += random.choice(symbols_list)
    letters += random.choice(symbols_list)

for number_count in range(numbers_input):
#    numbers += random.choice(numbers_list)
    letters += random.choice(numbers_list)

#letters = list(lower_case + upper_case + symbols + numbers)
letters_list = list(letters)
random.shuffle(letters_list)
print ("Here is your password:\t", ''.join(letters_list))