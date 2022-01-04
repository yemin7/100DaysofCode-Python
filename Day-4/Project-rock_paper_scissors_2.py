import random

you_choose = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors?\n "))

#variable
rock_asci = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_asci = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_asci = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps_list = [rock_asci, paper_asci, scissors_asci]
computer_choose = random.randint(0,2)

you_output = rps_list[you_choose]
computer_output = rps_list[computer_choose]

if you_choose < 0 or you_choose >= 3:
    print("Your input is wrong.")

elif you_choose == 0 and computer_choose != 0:
    if computer_choose == 1:
        print(you_output + "\nComputer choose:\n" + computer_output)
        print("You Loose.")
    elif computer_choose == 2:
        print(you_output + "\nComputer choose:\n" + computer_output)
        print("You Win.")

elif you_choose == 1 and computer_choose != 1:
    if computer_choose == 0:
        print(you_output + "\nComputer choose:\n" + computer_output)
        print("You Win.")
    elif computer_choose == 2:
        print(you_output + "\nComputer choose:\n" + computer_output)
        print("You Loose.")

elif you_choose ==2 and computer_choose != 2:
    if computer_choose == 0:
        print(you_output + "\nComputer choose:\n" + computer_output)
        print("You Loose.")
    elif computer_choose == 1:
        print(you_output + "\nComputer choose:\n" + computer_output)
        print("You Win.")

elif you_choose == computer_choose:
    print(you_output + "\nComputer choose:\n" + computer_output)
    print("Draw.")