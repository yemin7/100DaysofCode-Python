# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
upper_name1 = name1.upper()
upper_name2 = name2.upper()

name_concat = upper_name1 + upper_name2

t = name_concat.count("T")
r = name_concat.count("R")
u = name_concat.count("U")
e = name_concat.count("E")
l = name_concat.count("L")
o = name_concat.count("O")
v = name_concat.count("V")

total_true_count = t + r + u + e
total_love_count = l + o + v + e

love_score = str(total_true_count) + str(total_love_count)

if int(love_score) < 10 or int(love_score) > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif int(love_score) >= 40 and int(love_score) <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
