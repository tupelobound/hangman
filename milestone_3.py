# Continuous loop to ask for user input until correct format of input is received
while True:
    # ask user to input a letter and save it to 'guess' variable
    guess = input("Please enter a letter: ")
    
    # conditional to check that guess is an alphabetic character and only a single letter
    if guess.isalpha() == True and len(guess) == 1:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
