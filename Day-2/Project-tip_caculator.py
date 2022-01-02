print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100
people = int(input("How many people to split the bill? "))

total_tip = bill * tip_percent
calculate = round((bill + total_tip) / people, 2)
print(f"Each person should pay: $ {calculate}")