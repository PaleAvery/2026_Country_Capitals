import csv
import random
from tkinter import *
from functools import partial  # To prevent unwanted windows

from Countries_Capitals.B_01_Capital_Country_stablev1 import Difficulty


def get_capital_country():
    """ this is used for reading the data required for this program to operate as intended"""
    file = open("country_capitals.csv", "r")
    all_colours = list(csv.reader(file, delimiter=","))
    file.close()

    all_colours.pop(0)

    round_capitals = []
    country_tocap = []

    while len(round_capitals) < 4:
        potential_capital = random.choice(all_colours)
        round_capitals.append(potential_capital)
        country_tocap.append(potential_capital[1])

    print(round_capitals)
    print(country_tocap)

    print(round_capitals[0][1])

def get_question_cc():
    """
    Choose four colours from larger list ensuring that the scores are all different.
    :return: list of colours and score to beat (median of scores) and high score (for stats)
    """
    all_colour_list = get_capital_country()

    round_colours = []
    colour_scores = []
def round_ans(val):
    """
    rounds numbers to nearest integer
    :param val: number to be rounded.
    :return: rounded number ( an integer)
    """
    var_rounded = (val * 2 +1) // 2
    raw_rounded = "{:.2f}".format(var_rounded)
    return int(raw_rounded)

    # loop until we have four colours with different scores...
    while len(round_colours) < 4:
        potential_colour = random.choice(all_colour_list)

        # colour scores are being read as a string,
        # change them to an integer to compare / when adding to score list.
        if potential_colour[1] not in colour_scores:
            round_colours.append(potential_colour)

            # make score an integer and add it to the list of scores
            colour_scores.append(potential_colour[1])

    # change scores to integers...
    int_scores = [int(x) for x in colour_scores]

is_hard=False


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

        # strings for labels
        intro_string = ("For each round you will be given the name of the country and you will be tasked"
                        " with clicking which capital is the capital for the country ")

        # choose_string = "Oops - please choose a whole number more than zero."
        choose_string = "how many Question's would you like to answer?"

        # list of labels to be made (text / Font / fg)
        start_labels_list = [
            ["Country's Capitals 🌍", ("Arial", 16, "bold"), None],
            [intro_string, ("Arial", 12), None],
            [choose_string, ("Arial", 12, "bold"), "#009900"]
        ]

        # create labels and add them to the referrence list ...

        start_labels_ref = []
        for count, item in enumerate(start_labels_list):
            make_label = Label(self.start_frame, text=item[0], font=item[1],
                               fg=item[2],
                               wraplength=350, justify="left", pady=10, padx=20)
            make_label.grid(row=count)

            start_labels_ref.append(make_label)

        # extract choice label so that it can be changed to an
        # error message if necessary
        self.choose_label = start_labels_ref[2]

        # frame so that entry box and button can be in the same row
        self.entry_area_frame = Frame(self.start_frame)
        self.entry_area_frame.grid(row=3)

        self.num_rounds_entry = Entry(self.entry_area_frame, font=("Arial", 20, "bold"),
                                      width=14)
        self.num_rounds_entry.grid(row=1, column=0, padx=10, pady=10,columnspan=2)

        # create play button...
        self.play_button = Button(self.entry_area_frame, font=("Arial", 16, "bold"),
                                  fg="#FFFFFF", bg="#E6BD27", text="Play", width=6,
                                  command=self.check_rounds)
        self.play_button.grid(row=2, column=0)
        self.infinite_button = Button(self.entry_area_frame, font=("Arial", 16, "bold"),
                                      fg="#FFFFFF", bg="#0057D8", text="Infinite", width=6,
                                      command=self.infinite_rounds)
        self.infinite_button.grid(row=2, column=1)

        self.Difficulty_button = Button(self.entry_area_frame, font=("Arial", 16, "bold"),
                                  fg="#FFFFFF", bg="blue", text="Easy", width=16,
                                  command=self.difficulty)
        self.Difficulty_button.grid(row=0,column=0, columnspan=3)

    def difficulty(self):
        """
        this will be my hard mode difficulty this will rely on having to type in the answers this is
        more difficult because recall is more complex than recognition
        this will also remove hints
        """
        global is_hard
        if is_hard==True:

            self.Difficulty_button.config(text="Easy",
                            bg="blue")
            is_hard = False
        else:


            self.Difficulty_button.config(text="Hard", bg="red")
            is_hard = True


    def check_rounds(self):
        """
    I will be using this component in order to start the game with
    a preset number of rounds this will be for my normal game mode
    this will trigger the play function with how_many = whatever u want
    """
        # retirieve temp to be converted
        questions_wanted = self.num_rounds_entry.get()

        # reset label and entry box (for when users come back to home screen)
        self.choose_label.config(fg="#009900", font=("Arial", 12, "bold"))
        self.num_rounds_entry.config(bg="#FFFFFF")

        error = "Oops - please pick a whole number more than zero"
        has_errors = "no"

        # checks that amount to be converted is a number above absolute zero
        try:
            questions_wanted = int(questions_wanted)
            if questions_wanted > 0 and is_hard==True:
                # Invoke Play Class (and take across number of rounds)
                hard_game(questions_wanted)
                # Hide root window (ie: hide rounds choice window).
                root.withdraw()
                print(f"hard mode and {questions_wanted} questions ")

            elif questions_wanted > 0 and is_hard==False:
                # Invoke Play Class (and take across number of rounds)
                easy_game(questions_wanted)
                # Hide root window (ie: hide rounds choice window).
                root.withdraw()
                print(f"easy mode and {questions_wanted} questions")
            else:
                has_errors = "yes"

        except ValueError:
            has_errors = "yes"

        # display the error is necessary
        if has_errors == "yes":
            self.choose_label.config(text=error, fg="#990000",
                                     font=("Arial", 10, "bold"))
            self.num_rounds_entry.config(bg="#F4CCCC")
            self.num_rounds_entry.delete(0, END)

    def infinite_rounds(self):
        """
    for this component I will be using it in order to start the main
    game as well however this will be used for infinite questions
    this will trigger the play function with how_many = infinite
    """
        infinite = "Infinite"

        # reset label and entry box (for when users come back to home screen)
        self.choose_label.config(fg="#009900", font=("Arial", 12, "bold"))
        self.num_rounds_entry.config(bg="#FFFFFF")

        self.choose_label.config(text=f"You have chosen to play in infinite mode")
        # Invoke Play Class (and take across number of rounds)
        if is_hard:
            # Invoke Play Class (and take across number of rounds)
            hard_game(infinite)
            # Hide root window (ie: hide rounds choice window).
            root.withdraw()
            print("hard mode infinite picked")
        else:
            # Invoke Play Class (and take across number of rounds)
            easy_game(infinite)
            # Hide root window (ie: hide rounds choice window).
            root.withdraw()
            print("easy mode infinite picked")












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
    def new_round(self):
        """"""
    def round_results(self, user_choice):
        """
        Retrieves which button was pushed index 0 - 3 retrieves
        score and then compares it with median, updates results
        and adds results to stats list
        """
        colour_name = self.colour_button_ref[user_choice].cget('text')

        # enable stats button (because we have played a round)
        answer = ("Sydney")

    # this class will refer to the game components for components such as stats and hints etc
class easy_game(game_components):
    # this component will store the gui of my code such as the 4 boxes of options and the next round button
    def __init__(self,how_many):
        """"""
        # rounds played - start with zero
        self.rounds_played = IntVar()
        self.rounds_played.set(0)

        self.rounds_wanted = IntVar()
        self.rounds_wanted.set(how_many)

        self.rounds_won = IntVar()

        # Colour lists and score list
        self.round_colour_list = []
        self.all_scores_list = []
        self.all_high_score_list = []

        self.play_box = Toplevel()

        self.start_frame = Frame(self.play_box)
        self.start_frame.grid(padx=10, pady=10)

        # strings for the labels
        hard_string = (f"What is the capital of Australia.")
        hard_labels_list = [
            ["Country's Capitals🌍 EASY MODE", ("Arial", 16, "bold"), None],
            [hard_string, ("Arial", 12), None]
        ]

        # create the labels and add them to the ref list
        hard_labels_ref = []
        for count, item in enumerate(hard_labels_list):
            make_label = Label(self.start_frame, text=item[0], font=item[1],
                               fg=item[2],
                               wraplength=350, justify="left", pady=10, padx=20)
            make_label.grid(row=count)

            hard_labels_ref.append(make_label)

        self.entry_area_frame = Frame(self.start_frame)
        self.entry_area_frame.grid(row=3)

        # set up colour buttons...
        self.colour_frame = Frame(self.start_frame)
        self.colour_frame.grid(row=3)
        # Creates the four buttons in a 2 x 2 grid

        self.colour_button_ref = []
        self.button_colours_list = []

        # create four buttons in a 2 x 2 grid
        for item in range(0, 3):
            self.colour_button = Button(self.colour_frame, font=("Arial", 12),
                                        text="Colour Name", width=15,
                                        command=partial(self.round_results, item))
            self.colour_button.grid(row=item // 2,
                                    column=item % 2,
                                    padx=5, pady=5)
            self.colour_button_ref.append(self.colour_button)


        # if users press the x button on the game window than the whole game is ended
        self.play_box.protocol('WM_DELETE_WINDOW', root.destroy)

    # this class will refer to the game components for stats and not hints and also close play and more
class hard_game(game_components):
    # this gui will be overall more simple as the 4 boxes will be absent
    # however it will instead boast a text box that you can type into

    def __init__(self,how_many):
        """"""

        # rounds played - start with zero
        self.rounds_played = IntVar()
        self.rounds_played.set(0)

        self.rounds_wanted = IntVar()
        self.rounds_wanted.set(how_many)

        self.rounds_won = IntVar()

        # Colour lists and score list
        self.round_colour_list = []
        self.all_scores_list = []
        self.all_high_score_list = []

        self.play_box = Toplevel()


        self.start_frame = Frame(self.play_box)
        self.start_frame.grid(padx=10,pady=10)

        #strings for the labels
        hard_string = (f"What is the capital of Australia.")
        hard_labels_list = [
            ["Country's Capitals🌍 HARD MODE", ("Arial", 16,"bold"), None],
            [hard_string, ("Arial",12),None]

        ]


        # create the labels and add them to the ref list
        hard_labels_ref = []
        for count, item in enumerate(hard_labels_list):
            make_label = Label(self.start_frame, text=item[0], font=item[1],
                               fg=item[2],
                               wraplength=350, justify="left", pady=10, padx=20)
            make_label.grid(row=count)

            hard_labels_ref.append(make_label)





        self.entry_area_frame = Frame(self.start_frame)
        self.entry_area_frame.grid(row=3)

        self.num_rounds_entry = Entry(self.entry_area_frame, font=("Arial", 20, "bold"),
                                      width=7)
        self.num_rounds_entry.grid(row=0, column=0, padx=10, pady=10)
        # if users press the x button on the game window than the whole game is ended
        self.play_box.protocol('WM_DELETE_WINDOW',root.destroy)

        # body font for most labels...


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    StartGame()
    root.mainloop()