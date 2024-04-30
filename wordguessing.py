# Consolidation project
# set the game to two person players
# create word bank as a list of words
# Pick a word from the list randomly 
# Loop through each letter in the chosen word
# Make the players take turns to enter a letter or word (make sure they only have three word guesses)
# Display the number of times the letter appears in the word
# Count the letter and word guesses for each player
# after the player guesses a letter, they have an option to guess the word
# track the score for each player (score is the number of turns they made before guessing correctly)
# when the right word is guessed, the loop stops and displays the scores of each player and says who wins

import random 

player_count = 2

word_bank = ["River", "Ocean", "Beach", "Stone", "Earth"]
secret_word = random.choice(word_bank)
list(secret_word)
for x in list(secret_word):
    print(x.lower())
    for y in range (2):
        print (y)
        letter = input("Please enter a letter: ")
        print(letter)
        if letter == x: 
            print("Your guess was correct")
        word = input("Guess the word: ")
        print(word)
        if word == secret_word:
            print("Congradulations! You guessed the word!")
