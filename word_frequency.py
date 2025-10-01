#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies
#!/usr/bin/env python3

import re
import string 

def is_sentence(text):
    if not isinstance(text, str) or not text.strip():
        return False
    if not text[0].isupper():
        return False
    if not re.search(r'[.!?]$', text):
        return False
    if not re.search(r'\w+', text):
        return False
    return True

while True:
    sentence = input("Enter a sentence: ")
    if is_sentence(sentence):
        break
    else:
        print("Invalid input. Please enter a valid sentence (Starts with a capital letter, contains at least one word and ends with a punctuation mark).")

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
