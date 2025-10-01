#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

while True:
    user_input = input("How many terms of the Fibonacci sequence do you want? ")
    
    if user_input.isdigit():  
        terms = int(user_input)
        
        if terms > 0:
            break
        else:
            print("Please enter a positive integer.")   
    else:
        print("Please enter a positive integer.")

a, b = 0, 1
for i in range(terms):
    print(a, end=" ")
    a, b = b, a + b
