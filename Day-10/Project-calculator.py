import os, art

operator_list = ['+', '-', '*', '/']

def add (num1, num2):
    return num1 + num2

def subtract (num1, num2):
    return num1 - num2

def multiply (num1, num2):
    return num1 * num2

def divide (num1, num2):
    return num1 / num2

operator_dict = {'+': add, '-': subtract, '*': multiply, '/': divide}

def calculator(): 
    finished = False
    print(art.logo)
    first_num = float(input("Enter first number. "))
    while not finished:
#        first_num = int(input("Enter first number. "))
        operator = input("Give the operator (+, -, *, /) ")

        while operator not in operator_list:                                        # check wrong operator input
            operator = input("Wrong opreator! Choose the operator (+, -, *, /)")

        second_num = float(input("Enter second number. "))

        _function = operator_dict[operator]
        answer = _function(first_num, second_num)
        print (f"{first_num} {operator} {second_num} = {answer}")
    
        result = input("Type 'y' if you want to continue calculating or type 'n' to start a new calculation.\nType 'exit' to finish the calculation. ").lower()
        if result == 'y':
            first_num = answer
        elif result == 'n':
            finished = True
            os.system("clear")
            calculator()
        elif result == 'exit':
            finished = True

calculator()