# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

# Milestone 1
First milestone in project was to clone AICore project repository and connect Github bot to account in order to track commits and update project progress automatically.

# Milestone 2
This milestone involved setting up variables and a simple conditional to test user input. The following tasks were completed:

- create a short list of words to act as the possible answers, in this case five favourite fruits, and print the list to standard out.
- import built-in Python module random and use the function choice(), which accepts an iterable as an argument and returns a random item, to assign a random word as the answer. At this stage, print word to standard out.
- ask user to input a letter, using the input() function and assign the inputted string to the 'guess' variable.
- use an if-else conditional structure to check that the inputted string is:
1. a single character, using the len() function
2. alphabetical, using the isalpha() string method

