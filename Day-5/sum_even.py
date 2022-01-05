#Calculates the sum of all the even numbers from 1 to 100.

numbers = list(range(2,101))
sum = 0
for even in numbers:
    if even%2 == 0:
        sum += even
print(f"The sum of all even numbers from 1 to 100 is: {sum}")
