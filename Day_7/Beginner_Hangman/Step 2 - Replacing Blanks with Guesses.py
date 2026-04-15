import random

word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""

word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

guess = input("Guess the letter:").lower()

display = ""

for letter in chosen_word:
    if letter == guess:
       display += letter
    else:
       display += "_"
print(display)