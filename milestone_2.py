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
