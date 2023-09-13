# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    wordToGuess = pickWord()
    # Checking to see if it is in the dictionary
    def enter_action(s):
        s= s.lower()
        if len(s) < 5:
            if s in FIVE_LETTER_WORDS:
                gw.show_message("This is in the dictionary")
            else :
                gw.show_message("Not in dictionary.")
        else :
            gw.show_message("Please enter a 5 letter word")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    print(wordToGuess)

def pickWord() :
    pickedWordNum = random.randrange(len(FIVE_LETTER_WORDS))
    pickedWord = FIVE_LETTER_WORDS[pickedWordNum]
    return pickedWord
    

# Startup code

if __name__ == "__main__":
    wordle()
