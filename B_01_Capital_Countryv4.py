import csv
import random
from tkinter import *
from functools import partial  # To prevent unwanted windows
def get_capital_country():
    """"""
    file = open("country_capitals.csv", "r")
    all_cc = list(csv.reader(file, delimiter=","))
    file.close()

    # remove the first row
    all_cc.pop(0)
    print(all_cc[0][0])
    return all_cc
def get_question_cc():
    """
    Choose four colours from larger list ensuring that the scores are all different.
    :return: list of colours and score to beat (median of scores) and high score (for stats)
    """

    all_cc_list = get_capital_country()

    round_capital= []
    country_id = []

    # loop until we have four colours with different scores...
    while len(round_capital) < 4:
        potential_colour = random.choice(all_cc_list)

        # colour scores are being read as a string,
        # change them to an integer to compare / when adding to score list.
        if potential_colour[1] not in country_id:
            round_capital.append(potential_colour)

            # make score an integer and add it to the list of scores
            country_id.append(potential_colour[1])

    # change scores to integers...
    int_scores = [int(x) for x in country_id]



class StartGame:
    """
    Initial game interface (asks users how many questions
    they would like to play)
    """
    def __init__(self):
        """
        gets number of questions from user
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
            ["Country's Capitals 🌍", ("Arial", 16,"bold"), None],
            [intro_string, ("Arial",12), None],
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

        self.num_rounds_entry = Entry(self.entry_area_frame, font=("Arial",20,"bold"),
                                      width=7)
        self.num_rounds_entry.grid(row=0, column=0, padx=10,pady=10)

        # create play button...
        self.play_button = Button(self.entry_area_frame, font=("Arial",16,"bold"),
                                  fg="#FFFFFF", bg="#E6BD27",text="Play", width=6,
                                  command=self.check_rounds)
        self.play_button.grid(row=0, column=1)
        self.infinite_button = Button(self.entry_area_frame, font=("Arial",16,"bold"),
                                  fg="#FFFFFF", bg="#0057D8",text="Infinite", width=6,
                                  command=self.infinite_question)
        self.infinite_button.grid(row=0, column=2)

    def infinite_question(self):
        """
        puts player into infinite mode
        """
        infinite = "Infinite"


        # reset label and entry box (for when users come back to home screen)
        self.choose_label.config(fg="#009900",font=("Arial",12,"bold"))
        self.num_rounds_entry.config(bg="#FFFFFF")

        self.choose_label.config(text=f"You have chosen to play in infinite mode")
        # Invoke Play Class (and take across number of rounds)
        Play(infinite)
        # Hide root window (ie: hide rounds choice window).
        root.withdraw()

    def check_rounds(self):
        """
        checks users have entered 1 or more rounds
        """

        #retirieve temp to be converted
        questions_wanted = self.num_rounds_entry.get()

        # reset label and entry box (for when users come back to home screen)
        self.choose_label.config(fg="#009900",font=("Arial",12,"bold"))
        self.num_rounds_entry.config(bg="#FFFFFF")

        error = "Oops - please pick a whole number more than zero"
        has_errors = "no"

        #checks that amount to be converted is a number above absolute zero
        try:
            questions_wanted = int(questions_wanted)
            if questions_wanted > 0:
                # Invoke Play Class (and take across number of rounds)
                Play(questions_wanted)
                # Hide root window (ie: hide rounds choice window).
                root.withdraw()
            else:
                has_errors = "yes"

        except ValueError:
            has_errors= "yes"

        # display the error is necessary
        if has_errors == "yes":
            self.choose_label.config(text=error, fg="#990000",
                                     font=("Arial",10,"bold"))
            self.num_rounds_entry.config(bg="#F4CCCC")
            self.num_rounds_entry.delete(0,END)

class Play:
    def __init__(self,how_many):
        print(f"{how_many}")
        self.rounds_played = IntVar()
        self.rounds_played.set(0)
        self.rounds_wanted = IntVar()
        self.rounds_wanted.set(how_many)
        self.rounds_won = IntVar()
        self.play_box = Toplevel()
        self.game_frame = Frame(self.play_box)
        self.game_frame.grid(padx=10, pady=10)


        rounds_done = 1
        # if users press the x on the game window the entire game is ended
        self.play_box.protocol('WM_DELETE_WINDOW', root.destroy)

        # List for label details (text | font | background | row)
        play_labels_list = [
            [f"Round {rounds_done} of {how_many}", ("Arial", "16", "bold"), None, 0],
            ["Choose a Capital below.  Good luck. 🍀", ("Arial", "16"), "#D5E8D4", 2],
            ["You chose, result", ("Arial", "16"), "#D5E8D4", 4]
        ]

        play_labels_ref = []
        for item in play_labels_list:
            self.make_label = Label(self.game_frame, text=item[0], font=item[1],
                                    bg=item[2], wraplength=300, justify="left")
            self.make_label.grid(row=item[3], pady=10, padx=10)

            self.play_area_frame = Frame(self.game_frame)
            self.play_area_frame.grid(row=3)

            play_labels_ref.append(self.make_label)
        self.stats_button = Button(self.play_area_frame,font=("Arial",16,"bold"),
                                   text="Stats",fg="white",bg="black",width=6,
                                   command=self.to_stats)

        self.stats_button.grid(row=2,column=0)

        self.hints_button = Button(self.play_area_frame, font=("Arial", 16, "bold"),
                                   text="Hints", fg="black", bg="white", width=6,
                                   command=self.to_hints)

        self.hints_button.grid(row=2, column=1)

    def to_stats(self):
        """
        Retrieves everything we need to display the game / round statistics"""
        Stats()

    def to_hints(self):
        """"""



class Stats:
    def __init__(self):

        self.play_box = Toplevel()

        self.game_frame = Frame(self.play_box)
        self.game_frame.grid(padx=10, pady=10)
        print("Stats is clicked")



        #take important info from list
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    StartGame()
    root.mainloop()