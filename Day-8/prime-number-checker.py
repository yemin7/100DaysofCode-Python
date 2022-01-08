import os
check = 'y'
def prime_checker(number):
    prime, divide = True, []


    for count in range(2, number):
        if number % count == 0:
            prime = False
            divide.append(str(count))
            
    if prime:
        print ("It is a prime number.")
    else:
        print ("It is not a prime number.\nBecause you can divide it by 1,", ', '.join(divide) + ", "+ str(number))


while check == 'y':
    num = int(input("Prime Number Checker\nGive a number: "))
    prime_checker(num)
    check = input("Do you want to check next one?(y/n)").lower()
    os.system('clear')