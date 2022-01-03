#Body Mass Index (BMI) based on a user's weight and height.

#Under 18.5 they are underweight.
#Over 18.5 but below 25 they have a normal weight.
#Over 25 but below 30 they are slightly overweight.
#Over 30 but below 35 they are obese.
#Above 35 they are clinically obese.

####################################

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi_float = weight / (height ** 2)
bmi = round(bmi_float)

if bmi > 25:
    if bmi < 30:
        print(f"Your BMI is {bmi}, you are slightly overweight.")
    elif bmi < 35:
        print(f"Your BMI is {bmi}, you are obese.")
    else:
        print(f"Your BMI is {bmi}, you are clinically obese.")
elif bmi < 25:
    if bmi > 18.5:
        print(f"Your BMI is {bmi}, you have a normal weight.")
    else:
       print(f"Your BMI is {bmi}, you are underweight.")
