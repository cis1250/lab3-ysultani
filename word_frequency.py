#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

user_sentence = input("Enter a sentence: ")

while (is_sentence(user_sentence) == False):
    print("This does not meet the criteria for a sentence.")
    user_input = input("Enter a sentence: ")
    
{
    import string

def is_sentence(text):
    return (
        len(text) > 0
        and text[0].isupper()
        and text[-1] in ".?!"
        and any(char.isalpha() for char in text)
    )
while True:
    sentence = input("Enter a sentence: ")
    if is_sentence(sentence):
        break
    else:
        print("Error: Please enter a valid sentence (start with a capital letter, contain words, and end with . ? or !).")

words_list = sentence.split()
words_list = [word.strip(string.punctuation).lower() for word in words_list]
words = []
frequencies = []

for word in words_list:
    if word in words:
        index = words.index(word)
        frequencies[index] += 1
     else:
        words.append(word)
        frequencies.append(1)

for i in range(len(words)):
    print(f"{words[i]}: {frequencies[i]}")
}
