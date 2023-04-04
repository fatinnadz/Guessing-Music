#!/usr/bin/env python

import random

def main():
    """Start a music guessing game."""
    print("Guess the music!")

    genre = [
        "K-pop",
        "J-pop",
        "Rock",
        "Classic",
        "Ballad",
        "Hiphop",
        "Jazz",
        "Traditional",   
        ]

    x = random.choice(genre)
    print(x)
    guess = None

    while x != guess:

        guess = str(input("What music am I thinking of? "))

        if x == guess:
            print("You guessed {}. Congratulations, you are cultured!".format(guess))
            break
        else:
            print("You guessed {}. Please try again!".format(guess))
main()