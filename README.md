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

# Milestone 3
This milestone consists of the following tasks:

- add a while loop that loops indefinitely until the user input meets the criteria added in milestone 2.
- use a conditional if-else statement to check whether the user-inputted character is in the randomly-generated word.
- move the code into two functions, check_guess and ask_for_input. check_guess is called within the body of ask_for_input.

# Milestone 4
This milestone moves the code from the previous milestones into a class, Hangman, and expands the existing functions to display the appropriate responses to the user and update the class attributes, in this case the in-game variables.
