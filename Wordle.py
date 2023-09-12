# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    # Checking to see if it is in the dictionary
    def enter_action(s):
        s= s.lower()
        if s in FIVE_LETTER_WORDS:
            gw.show_message("This is in the dictionary")
        else :
            gw.show_message("Not in dictionary.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    

# Startup code

if __name__ == "__main__":
    wordle()
