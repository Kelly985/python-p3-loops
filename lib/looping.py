#!/usr/bin/env python3

def happy_new_year():
    countdown = list(range(10, 0, -1))
    countdown.append("Happy New Year!")
    for item in countdown:
        print(item)

def square_integers(int_list):
    return [num**2 for num in int_list if isinstance(num, int)]

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)



print(happy_new_year())

numbers = [1, 2, 3, 4, 5]
squared_numbers = square_integers(numbers)
print(squared_numbers)

print(fizzbuzz())
