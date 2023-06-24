# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is a Python implementation of the Hangman game, where the computer 'thinks' of a word and the user tries to guess it.

# Playing a game
To quickly start a game with a limited number of words pre-loaded, simply download and run milestone_5.py. Don't peek at the list of words!

# Game details
The game is implemented as a Python class, *Hangman* that can be instantiated by passing in a list of potential words for the user to solve and the number of lives the user will have (essentially the number of incorrect guesses the user can have before losing the game). The *Hangman* class has the following attributes:

- self.word - this is the word to be guessed and is generated upon instantiation by using the choice() method from the Python module random to randomly select one word from the list of words passed into the class

- self.word_guessed - this is a representation of the word the user needs to guess, with underscores replacing any letters that have not been guessed yet. This list is printed at the beginning of the word, and after any guess.

- self.num_letters - this is an integer representing the number of unique letters in the word still remaining to be guessed by the user

- self.word_list - a list of words (strings) from which the computer will randomly choose one for the user to guess

- self.list_of_guesses - a list of all the letters that the user has tried during the game. This list is used to warn the user if a guess they enter has already been tried.

The *Hangman* class has the following methods:

- check_guess(self, guess) - this method takes the letter the user has inputted, converts it to lower case and compares it to the randomly-chosen word. A message is printed to the terminal telling the user if the letter is in the word or not, along with the number of lives remaining if the user guessed incorrectly plus self.word_guessed so the user can see their progress.

- ask_for_input(self) - this method is used to ask the user to input a letter to guess. Conditionals check whether the inputted letter is a single, alphabetical character or whether the letter has been guessed already. If the letter is acceptable, self.check_guess is called on the letter.

Outside of the *Hangman* class definition, a function called play_game() is defined that accepts a list of possible words. Within this function definition, the number of lives are set, an instance of the *Hangman* class is created and a while loop executes until either the user runs out of lives or correctly guesses the word. Within the loop, the ask_for_input() method of this instance of the Hangman() class is called repeatedly, for each successive user guess.

# Thoughts and future work

At the moment, the list from which the computer can randomly choose a word to guess is hard-coded into milestone_5.py. In future, I would like to adapt the game so that the user can load in their own lists of words. Another feature that would be cool would be different difficulty modes that offer the user differing numbers of lives and/or different length words. Another cool feature would be to offer the user the opportunity to get a clue!