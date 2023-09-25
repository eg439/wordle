# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

#Message box imports-------------------------------------------------------------------
import tkinter as tk
from tkinter import messagebox

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

#Message box code-------------------------------------------------------------------
def set_variable_true():
    global hard_mode
    hard_mode = True
    root.destroy()

def set_variable_false():
    global hard_mode
    hard_mode = False
    root.destroy()

# Create the main application window
root = tk.Tk()
root.title("Variable Selection")

# Initialize the variable to None
hard_mode = None

# Create a label
label = tk.Label(root, text="Do you want to play in Hard Mode?")
label.pack()

# Create "True" button
true_button = tk.Button(root, text="Yes, bring it on", command=set_variable_true)
true_button.pack()

# Create "False" button
false_button = tk.Button(root, text="No, just the normal mode", command=set_variable_false)
false_button.pack()

# Start the Tkinter main loop
root.mainloop()

# Check the value of my_variable after the pop-up window is closed
if hard_mode is not None:
    print("my_variable is:", hard_mode)
else:
    print("No value selected for my_variable")


####COLOR BUTTON#####################

def set_color_variable(color):
    global color_variable
    color_variable = color
    root.destroy()

# Create the main application window
root = tk.Tk()
root.title("Color Variable Selection")

# Initialize the color_variable to None
color_variable = None

# Create a label
label = tk.Label(root, text="Select a color:")
label.pack()

# Create "Red" button
normal_button = tk.Button(root, text="Normal", command=lambda: set_color_variable("normal"))
normal_button.pack()

# Create "Green" button
blind_button = tk.Button(root, text="Color Blind Friendly", command=lambda: set_color_variable("colorblind"))
blind_button.pack()

# Start the Tkinter main loop
root.mainloop()

# Check the value of color_variable after the pop-up window is closed
if color_variable is not None:
    print("Selected color is:", color_variable)
else:
    print("No color selected.")




def wordle():
    wordToGuess = pickWord()

    if color_variable == "normal" :
        correctColor = "green"
        midCorrect = "yellow"
    else :
        correctColor = "blue"
        midCorrect = "red"
    # Checking to see if it is in the dictionary
    def enter_action(s):
        s= s.lower()
        print(s)
        s = s.replace(" ","")
        if len(s) == 5:
            previous = [False, False,False,False, False]
            #make sure it is in the dictionary, but it isn't the guessed word
            if (s in FIVE_LETTER_WORDS) & (s != wordToGuess) & (hard_mode == False):
                gw.show_message("This is in the dictionary")
                row = gw.get_current_row()
                s=str(s)
                for x in s:
                    xIndex = wordToGuess.find(x)
                    if xIndex > 0 :
                        xColumn = s.index(x)
                        if(xColumn == xIndex) :
                            gw.set_square_color(row,xColumn,correctColor)
                        else :
                            gw.set_square_color(row,xColumn,midCorrect)
                    xIndex = 0
                #making sure they aren't out of guesses
                if row <5 :
                    gw.set_current_row(row + 1)
                else:
                    gw.show_message("You are out of guesses")
            #not in dictionary
            elif (s in FIVE_LETTER_WORDS) & (s!= wordToGuess) & (hard_mode == True):
                    gw.show_message("This is in the dictionary")
                    row = gw.get_current_row()
                    s=str(s)
                    word= [False, False,False,False,False]
                    for x in s:
                        xIndex = wordToGuess.find(x)
                        if(row != 0) :
                            if xIndex != -1 :
                                xColumn = s.index(x)
                                word[xColumn] = True
                                if word[xColumn] != previous[xColumn] :
                                    gw.show_message("This does not work in hard mode try again")
                                else :
                                    if(xColumn == xIndex) :
                                        gw.set_square_color(row,xColumn,correctColor)
                                        
                                    else :
                                        gw.set_square_color(row,xColumn,midCorrect)          
                        else:
                            if xIndex != -1 :
                                xColumn = s.index(x)
                                if(xColumn == xIndex) :
                                    previous[xColumn] = True
                                else :
                                    previous[xColumn] = True
                                if(xColumn == xIndex) :
                                    gw.set_square_color(row,xColumn,correctColor)
                                else :
                                    gw.set_square_color(row,xColumn,midCorrect)
                    for i in word :
                        word[i] = previous[i]
                    xIndex = 0
                #making sure they aren't out of guesses
                    if row <5:
                        gw.set_current_row(row + 1)
                    else:
                        gw.show_message("You are out of guesses")
            elif (s not in FIVE_LETTER_WORDS) :
                gw.show_message("Not in dictionary.")
            #guessed the word
            elif (s == wordToGuess) :
                row = gw.get_current_row()
                for x in range(0,5) :
                    gw.set_square_color(row,x,correctColor)
                gw.show_message("You guessed the word")
        #didn't put in enough letters
        else:
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
