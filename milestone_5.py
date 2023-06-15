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
        guess = guess.lower()
        
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            
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
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
        if game.num_lives == 0:
            print("You lost!")
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations! You won the game!")
            break

play_game(["strawberry"])

