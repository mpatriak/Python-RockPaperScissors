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
        pass # Allows the loops to stop when player is done
    scores() # Call function when done playing



