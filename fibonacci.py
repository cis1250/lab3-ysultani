#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

while True:
    try:
        terms = int(input("How many terms of the Fibonacci sequence do you want? "))
        if terms <= 0:
            print("Error: Please enter a positive integer greater than 0.")
        else:
            break
    except ValueError:
        print("Error: Please enter a valid integer.")
a, b = 0, 1
print("Fibonacci sequence:")

for i in range(terms):
    print(a, end=" ")
    a, b = b, a + b
