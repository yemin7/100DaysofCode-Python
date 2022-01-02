#BMI = heigh(kg)/weight2(m2)

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

####################################

bmi = int(weight) / float(height) ** 2
print (str(int(bmi)))
