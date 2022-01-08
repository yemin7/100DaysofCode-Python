def math (number, count):
    multiply = range(number, number*count+1, number)
    
    for idx, num in enumerate(multiply):
        print (f"{number} x {idx+1}\t= {num}")

number = int(input("Multiply Number: "))
count = int(input("Maximum count: "))

math(number, count)