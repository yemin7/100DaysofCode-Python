numbers = list(range(1,101))
fizz = "Fizz"
buzz = "Buzz"
for divide in numbers:
    if divide %3 == 0 and divide % 5 == 0:
        numbers[divide-1] = fizz + buzz

    elif divide % 3 ==0:
        numbers[divide-1] = fizz

    elif divide % 5 == 0:
        numbers[divide-1] = buzz

    print(numbers[divide-1])
print(numbers)