# Initialise variable to act as test word
word = 'Test'

# define function that takes a character and checks if it is in a word
def check_guess(guess):
    guess = guess.lower()
    
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

# define function that asks for user input and then runs the check_guess function
def ask_for_input():
    while True:
        # ask user to input a letter and save it to 'guess' variable
        guess = input("Please enter a letter: ")
        
        # conditional to check that guess is an alphabetic character and only a single letter
        if guess.isalpha() == True and len(guess) == 1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    
    # call check_guess function and pass in the user input string
    check_guess(guess)

ask_for_input()
