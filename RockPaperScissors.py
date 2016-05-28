#!/usr/bin/env python2

# Extra modules used
import random
import time

# Set each move to a specific number
# Once a selection is made by the player,
# it will be equated to that specific variable.
rock = 1
paper = 2
scissors = 3

# Text representation of each move
names = { rock: "Rock", paper: "Paper", scissors: "Scissors" }

# Game Rules
rules = { rock: scissors, paper: rock, scissors: paper }

# Declare variables to be used to track scoring
player_score = 0
computer_score = 0

# Function to print a greeting and start
# a loop to allow the player to continue
#playing as many times as they wish
def start():
    print ("Let's play a game of Rock, Paper, Scissors.")
    while game():
        pass # Allows the loop to stop when player is done
    scores() # Call function when done playing

def game():
    # Call move function to determine player move
    player = move()
    # Get computer move as random int between 1 and 3
    computer = random.randint(1, 3)
    # Send the move through the result function
    result(player, computer)
    return play_again()

# Function to obtain a move from the player
def move():
    while True:
        print
        player = raw_input("Rock = 1\nPaper = 2\nScissors = 3\nMake a move: ")
        # Try to set the player move, or catch the error
        try:
            # Cast the user input as an integer
            player = int(player)
            # If entry is valid, set the variable
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print ("Oops! I didn't understand that. Please enter 1, 2, or 3.")

# Function to determine the result of the game
# player move and computer move are passed in
def result(player, computer):
    # Countdown to result display
    print ("1...")
    time.sleep(1)
    print ("2...")
    time.sleep(1)
    print("3!")
    time.sleep(0.5)
    # Display the computer's move
    # string.format() gets the text version
    # of the move and inserts it where "0"
    print ("Computer threw {0}!".format(names[computer]))
    #Call the scores set earlier
    global player_score, computer_score
    

    

