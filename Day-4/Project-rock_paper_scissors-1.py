import random

you_choose = input("What do you choose? Rock, Paper, Scissors?\n ").lower()

#variable
rps_list = ["rock", "paper", "scissors"]
computer_choose = random.choice(rps_list)

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

if you_choose not in rps_list:
    print("Your input is wrong.")

elif you_choose == "rock" and computer_choose == "paper":
    print (rock_asci + "\nComputer choose:\n" + paper_asci)
    print ("You loose")

elif you_choose == "rock" and computer_choose == "scissors":
    print (rock_asci + "\nComputer choose:\n" + scissors_asci)
    print ("You Win")

elif you_choose == "paper" and computer_choose == "rock":
    print (paper_asci + "\nComputer choose:\n" + rock_asci)
    print ("You Win")

elif you_choose == "paper" and computer_choose == "scissors":
    print (paper_asci + "\nComputer choose:\n" + scissors_asci)
    print ("You loose")

elif you_choose == "scissors" and computer_choose == "rock":
    print (scissors_asci+ "\nComputer choose:\n" + rock_asci)
    print ("You loose")

elif you_choose == "scissors" and computer_choose == "paper":
    print (scissors_asci+ "\nComputer choose:\n" + paper_asci)
    print ("You Win")

elif you_choose == computer_choose:
    same_choose = globals()[you_choose+ "_asci"]
    print (same_choose + "\nComputer choose:\n" + same_choose)
    print ("Draw")