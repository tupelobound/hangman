# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is a Python implementation of the Hangman game, where the computer 'thinks' of a word and the user tries to guess it.

# Playing a game
To quickly start a game with a limited number of words pre-loaded, simply download and run milestone_5.py. Don't peek at the list of words!

```
% python milestone_5.py
```

# Game details
The game is implemented as a Python class, `Hangman` that can be instantiated by passing in a list of potential words for the user to solve and the number of lives the user will have (essentially the number of incorrect guesses the user can have before losing the game). The `Hangman` class has the following attributes:

- `self.word` - this is the word to be guessed and is generated upon instantiation by using the `choice()` method from the Python module `random` to randomly select one word from the list of words passed into the class

- `self.word_guessed` - this is a representation of the word the user needs to guess, with underscores replacing any letters that have not been guessed yet. This list is printed at the beginning of the word, and after any guess.

- `self.num_letters` - this is an integer representing the number of unique letters in the word still remaining to be guessed by the user

- `self.word_list` - a list of words (strings) from which the computer will randomly choose one for the user to guess

- `self.list_of_guesses` - a list of all the letters that the user has tried during the game. This list is used to warn the user if a guess they enter has already been tried.

The `Hangman` class has the following methods:

```python
def check_guess(self, guess):
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
```

```python
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
```

Outside of the `Hangman` class definition, a function called `play_game()` is defined that accepts a list of possible words. Within this function definition, the number of lives are set, an instance of the `Hangman` class is created and a while loop executes until either the user runs out of lives or correctly guesses the word. Within the loop, the `ask_for_input()` method of this instance of the `Hangman` class is called repeatedly, for each successive user guess.

```python
def play_game(word_list):
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
```

# Thoughts and future work

At the moment, the list from which the computer can randomly choose a word to guess is hard-coded into milestone_5.py. In future, I would like to adapt the game so that the user can load in their own lists of words. Another feature that would be cool would be different difficulty modes that offer the user differing numbers of lives and/or different length words. Another cool feature would be to offer the user the opportunity to get a clue!