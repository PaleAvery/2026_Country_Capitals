import csv
import random
from tkinter import *
from functools import partial  # To prevent unwanted windows


def get_capital_country():
    """ this is used for reading the data required for this program to operate as intended"""


def get_question_cc():
    """
    Choose four colours from larger list ensuring that the scores are all different.
    :return: list of colours and score to beat (median of scores) and high score (for stats)
    """
class StartGame:
    """
    Initial game interface (asks users how many questions
    they would like to play)
    """

    def __init__(self):
        """
    gets number of questions from user
    and  this innit component is where the brunt
    of my pregame code will be stored such
    as the gui like the buttons and the overlay
        """

        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

    def check_rounds(self):
        """
    I will be using this component in order to start the game with
    a preset number of rounds this will be for my normal game mode
    this will trigger the play function with how_many = whatever u want
    """




    def infinite_rounds(self):
        """
    for this component I will be using it in order to start the main
    game as well however this will be used for infinite questions
    this will trigger the play function with how_many = infinite
    """









class difficulty:
    """"""

    def __init__(self):
        """
        this will cover my gui which includes
        the shape and the buttons applied to this
        """

    def hard_mode(self):
        """
        this will be my hard mode difficulty this will rely on having to type in the answers this is
        more difficult because recall is more complex than recognition
        this will also remove hints
        """
        # this takes you to class hard_game
        hard_game()
        #this deletes the difficulty selection window
        root.withdraw()

    def easy_mode(self):
        """
        this will be my easy mode because recognition is easier than recall
        therefore it will be easier selecting from a few options
        this will give you hints if needed
        """
        # this takes you over to class easy_game
        easy_game()
        # this deletes the difficulty selection window
        root.withdraw()

class game_components:
    """
    this component's sole purpose is too used as storage to
    save lines of code  because of the repeated code problem
    it also makes modification of existing code way easier
    """
    def stats(self):
        """"""
    def hints(self):
        """"""
    def close_play(self):
        """"""
    # this class will refer to the game components for components such as stats and hints etc
class easy_game(game_components):
    # this component will store the gui of my code such as the 4 boxes of options and the next round button
    def __init__(self):
        """"""

    # this class will refer to the game components for stats and not hints and also close play and more
class hard_game(game_components):
    # this gui will be overall more simple as the 4 boxes will be absent
    # however it will instead boast a text box that you can type into

    def __init__(self):
        """"""


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    StartGame()
    root.mainloop()