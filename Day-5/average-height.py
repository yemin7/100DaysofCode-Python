#Calculates the average student height from a List of heights.
#Input: 156 178 165 171 187

####################################

student_heights = input("Input a list of student heights ").split()
total = 0

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

for student in student_heights:
    total += student

average = round(total / len(student_heights))
print (average)
