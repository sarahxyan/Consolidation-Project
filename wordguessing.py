# Consolidation project
# set the game to any number of players
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

def pick_letter():
    letter = input("Please enter a letter : ")
    if len(letter) != 1:
        return pick_letter()
    return letter

player_count = int(input("Before the game starts, please enter the number of players you would like: "))

word_bank = ["River", "Ocean", "Beach", "Stone", "Earth"]
scores = []
word_guess_counts = []
for playerIndex in range(player_count):
    scores.append(0)
    word_guess_counts.append(0)

secret_word = random.choice(word_bank).lower()
print(secret_word)
print("Theme of the word is nature, and the word is five letters long")
game_is_completed = False
while True:  
    for y in range (player_count):
        print ("Person Number: ", y+1)
        letter = pick_letter()
        print("The letter appears this many times in the word: ", secret_word.count(letter))
        scores[y] = scores[y] + 1
        word = input("Guess the word (press enter if you would like to skip): ")
        print(word)
        if word != "": 
            if word == secret_word:
                word_guess_counts[y] = word_guess_counts[y] + 1 
                print("Congradulations! You guessed the word!")
                game_is_completed = True
                break
            else:
                print("Sorry, that is not the correct answer.")
            word_guess_counts[y] = word_guess_counts[y] + 1 
            if word_guess_counts[y] == 3:
                print("You have guessed the word 3 times, you lose :(")
                game_is_completed = True
                break 
            
    if game_is_completed: 
        break    
for y in range(player_count):
    print("Player #%d Score: %d Guess Count: %d" % (y+1, scores[y], word_guess_counts[y]))
          
