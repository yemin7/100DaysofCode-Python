#The person selected will have to pay for everybody's food bill.

import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

#names_length = len(names)
#random_name = random.randint(0,names_length-1)
#print(f"{names[random_name]} is going to buy the meal today!")

print(f"{random.choice(names)} is going to buy the meal today!")