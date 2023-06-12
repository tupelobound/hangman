import random

# create a list of five favourite fruits
word_list = ["cherry", "blueberry", "strawberry", "apple", "watermelon"]

# print word list to standard out
print(word_list)

# initialise varable for random.choice method
choice = random.choice

# assign random word from list to word variable
word = choice(word_list)

# print word to standard out
print(word)

# ask user to input a letter and save it to 'guess' variable
guess = input("Please enter a letter: ")

# conditional to check that guess is an alphabetic character and only a single letter
if guess.isalpha() == True and len(guess) == 1:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
