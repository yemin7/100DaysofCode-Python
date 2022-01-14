from game_data import data, clear, logo, vs
from random import choice

def choice_data():
    random_data = choice(data)
    return random_data

def calculate_score(first_data, second_data):
    if first_data > second_data:
        return 1
    else: return 0

def show_format(format):
    name = format['name']
    description = format['description']
    country = format['country']
    return (f"{format['name']}, a {format['description']}, from {format['country']}")

#def swap_compare(compare_data, against_data):
#    compare_data = against_data
#    against_data = choice_data()
#    return compare_data, against_data

def higher_lower():
    compare = choice_data()
    against = choice_data()
    result, score = 1, 0
    
    print(logo)
    print (f"Compare A: {show_format(compare)}")
    print(vs)
    print (f"Against B: {show_format(against)}")
    while result != 0:
        user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        if user_choice == 'A':
            result = calculate_score(compare['follower_count'], against['follower_count'])
        elif user_choice == 'B':
            result = calculate_score(against['follower_count'], compare['follower_count'])
        
        clear()
        print(logo)

        if result == 1:
            score += 1
            print(f"You're right! Current score: {score}.")
            compare = against
            against = choice_data()
            if compare == against:
                against = choice_data()
            print (f"Compare A: {show_format(compare)}")
            print(vs)
            print (f"Against B: {show_format(against)}")
#            new_compare = swap_compare(compare, against)
#            print (f"Compare A: {new_compare[0]['name']}, a {new_compare[0]['description']}, from {new_compare[0]['country']}.")
#            print (f"Against B: {new_compare[1]['name']}, a {new_compare[1]['description']}, from {new_compare[1]['country']}.")
        
        elif result == 0:
            print(f"You're wrong! Final score: {score}")

higher_lower()