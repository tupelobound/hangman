import random

class Hangman():
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for _ in self.word]
        self.num_letters = len(set([*self.word]))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        # convert guess to lower case
        guess = guess.lower()

        # check if guess is in randomly-generated word
        if guess in self.word:
            # if so, tell user
            print(f"Good guess! {guess} is in the word.")
            
    def ask_for_input(self):
        while True:
            # ask user to input a letter and save it to 'guess' variable
            guess = input("Please enter a letter: ")
            
            # conditional to check that guess is an alphabetic character and only a single letter
            if not (guess.isalpha() == True and len(guess) == 1):
                # if not, print error message to user
                print("Invalid letter. Please, enter a single alphabetical character.")
            # otherwise, check if user has already guessed the letter
            elif guess in self.list_of_guesses:
                # if so, print appropriate message
                print("You already tried that letter!")
            # if letter is good and hasn't been tried already
            else:
                # check letter against random word
                self.check_guess(guess)
                # add the letter to the list of previous guesses
                self.list_of_guesses.append(guess)
