import random # import random module to use choice() method

class Hangman():
    '''
    This class is used to represent an instance of the Hangman game

    Attributes:
        word: word to be guessed
        word_guessed: representation of the word to be guessed, with underscores replacing any letters that have not been guessed yet
        num_letters: integer representing the number of unique letters in the word still remaining to be guessed
        num_lives: integer representing the number of lives the user has remaining this game
        word_list: list of words (strings) from which the computer will randomly choose one for the user to guess
        list_of_guesses: list of all the letters that the user has tried during the game
    '''
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for _ in self.word]
        self.num_letters = len(set([*self.word]))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []


    def check_guess(self, guess):
        '''
        Checks the user-inputted guess against the computer-chosen word.
        
        Accepts a string as a parameter, converts that string to lowercase and checks if the string is in the word chosen
        by the computer. Prints appropriate message before updating Hangman class attributes

        Parameters
        ----------
        guess : str
            A string that should consist of a single alphabetic character
        
        Returns
        -------
        None
        '''
        # convert guess to lowercase
        guess = guess.lower()
        # check if guessed letter is in the chosen word
        if guess in self.word:
            # if so, print message to user
            print(f"Good guess! {guess} is in the word.")
            # loop over chosen word
            for index, letter in enumerate(self.word):
                # check if guessed letter equals current letter of word
                if guess == letter:
                    # if so, replace the underscore in word_guessed at the same index with the correct letter
                    self.word_guessed[index] = guess
            # update the number of letters remaining to guess
            self.num_letters -= 1
            # print word_guessed as a clue for user
            print(self.word_guessed)
        # if guess isn't in the chosen word
        else:
            # decrease number of lives by one
            self.num_lives -= 1
            # print message to user, along with word_guessed and number of lives remaining
            print(f"Sorry, {guess} is not in the word.")
            print(self.word_guessed)
            print(f"You have {self.num_lives} lives left.")
            

    def ask_for_input(self):
        '''
        Gets user input as string.
        
        Stores user input in guess variable and performs check to ensure a single alphabetic character is inputted.
        If not, tells user that input is invalid and prompts input again. If correct input is received, then checks
        if that letter has already been used in current instance of Hangman class. If not, self.check_guess is called,
        guess is added to list of previous guesses and loop is broken.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
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
    '''
    Creates an instance of the Hangman class and repeatedly calls ask_for_input() method until either the user runs out of
    lives or correctly guesses all letters in the chosen word

    Parameters
    ----------
    word_list : list
        List of strings to use as potential words for computer to choose from
    
    Returns
    -------
    None
    '''
    # set initial number of lives
    num_lives = 5
    # create instance of Hangman class
    game = Hangman(word_list, num_lives)
    # print word_guessed (only underscores) as a clue for user
    print(game.word_guessed)
    # infinite loop
    while True:
        # check if user has run out of lives
        if game.num_lives == 0:
            # if so, print losing message and break loop
            print("You lost!")
            break
        elif game.num_letters > 0:
            # otherwise, if there are still letters to guess, ask user for input
            game.ask_for_input()
        else:
            # otherwise, user has won - print congratulatory message and break loop
            print("Congratulations. You won the game!")
            break

play_game(["strawberry", "blueberry", "apple", "watermelon", "cherry"])

