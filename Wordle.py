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
        print(s)
        if len(s) == 5:
            #make sure it is in the dictionary, but it isn't the guessed word
            if (s in FIVE_LETTER_WORDS) & (s != wordToGuess):
                gw.show_message("This is in the dictionary")
                row = gw.get_current_row()
                s=str(s)
                for x in s:
                    xIndex = wordToGuess.find(x)
                    if xIndex > 0 :
                        xColumn = s.index(x)
                        if(xColumn == xIndex) :
                            gw.set_square_color(row,xColumn,"green")
                        else :
                            gw.set_square_color(row,xColumn,"yellow")
                    xIndex = 0
                #making sure they aren't out of guesses
                if row <5 :
                    gw.set_current_row(row + 1)
                else:
                    gw.show_message("You are out of guesses")
            #not in dictionary
            elif (s not in FIVE_LETTER_WORDS) :
                gw.show_message("Not in dictionary.")
            #guessed the word
            elif (s == wordToGuess) :
                row = gw.get_current_row()
                for x in range(0,5) :
                    gw.set_square_color(row,x,"green")
                gw.show_message("You guessed the word")
        #didn't put in enough letters
        else :
            gw.show_message("Please enter a 5 letter word")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
        

    print(wordToGuess)

#picks the word from the dictionary
def pickWord() :
    pickedWordNum = random.randrange(len(FIVE_LETTER_WORDS))
    pickedWord = FIVE_LETTER_WORDS[pickedWordNum]
    return pickedWord
    

# Startup code

if __name__ == "__main__":
    wordle()
