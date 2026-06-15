import csv
import random
from os import remove
from tkinter import *
from functools import partial  # To prevent unwanted windows



hintsused=0# helper functions go here
def get_capitals():

    file = open("country_capitals_utf_8.csv", "r",encoding='utf-8')

    all_capitals = list(csv.reader(file))

    file.close()

    # remove headings
    all_capitals.pop(0)



    return all_capitals


def get_round_questions():

    all_capital_list = get_capitals()

    round_questions = random.sample(all_capital_list, 4)



    return round_questions


def round_ans(val):
    """
    Rounds numbers to nearest integer
    :param val: number to be rounded.
    :return: Rounded number (an integer)
    """
    var_rounded = (val * 2 + 1) // 2
    raw_rounded = "{:.0f}".format(var_rounded)
    return int(raw_rounded)


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

        # Strings for labels
        intro_string = ("In each round you will be given a country and you must guess "
                        "which capital belongs to that country. "
                        )

        # choose_string = "Oops - Please choose a whole number more than zero."
        choose_string = "How many rounds do you want to play?"

        # List of labels to be made (text | font | fg)
        start_labels_list = [
            ["Country's Capitals", ("Arial", "16", "bold"), None],
            [intro_string, ("Arial", "12"), None],
            [choose_string, ("Arial", "12", "bold"), "#009900"]
        ]

        # Create labels and add them to the reference list...

        start_label_ref = []
        for count, item in enumerate(start_labels_list):
            make_label = Label(self.start_frame, text=item[0], font=item[1],
                               fg=item[2],
                               wraplength=350, justify="left", pady=10, padx=20)
            make_label.grid(row=count)

            start_label_ref.append(make_label)

        # extract choice label so that it can be changed to an
        # error message if necessary.
        self.choose_label = start_label_ref[2]

        # Frame so that entry box and button can be in the same row.
        self.entry_area_frame = Frame(self.start_frame)
        self.entry_area_frame.grid(row=3)

        self.num_rounds_entry = Entry(self.entry_area_frame, font=("Arial", 20, "bold"),
                                      width=14)
        self.num_rounds_entry.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

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
        self.Difficulty_button.grid(row=0, column=0, columnspan=3)

    def difficulty(self):
        """
        this will be my hard mode difficulty this will rely on having to type in the answers this is
        more difficult because recall is more complex than recognition
        this will also remove hints
        """
        global is_hard
        if is_hard:

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
        # retrieve temp to be converted
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


        # reset label and entry box (for when users come back to home screen)
        self.choose_label.config(fg="#009900", font=("Arial", 12, "bold"))
        self.num_rounds_entry.config(bg="#FFFFFF")

        self.choose_label.config(text=f"You have chosen to play in infinite mode")
        # Invoke Play Class (and take across number of rounds)
        if is_hard:
            # Invoke Play Class (and take across number of rounds)
            hard_game(-1)
            self.num_rounds_entry.delete(0, END)
            self.choose_label.config(text="How many rounds do you want to play?")
            # Hide root window (ie: hide rounds choice window).
            root.withdraw()
            print("hard mode infinite picked")
        else:
            # Invoke Play Class (and take across number of rounds)
            easy_game(-1)
            # Hide root window (ie: hide rounds choice window).
            self.num_rounds_entry.delete(0, END)
            self.choose_label.config(text="How many rounds do you want to play?")
            root.withdraw()
            print("easy mode infinite picked")















    # this class will refer to the game components for components such as stats and hints etc
class easy_game:
    # this component will store the gui of my code such as the 4 boxes of options and the next round button
    def __init__(self,how_many):
        """"""
        # Integers / String Variables
        self.was_hint_used = False
        self.hints_used = IntVar()
        self.target_score = IntVar()

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

        self.game_frame = Frame(self.play_box)
        self.game_frame.grid(padx=10, pady=10)

        # if users press the x on the game window the entire game is ended
        self.play_box.protocol('WM_DELETE_WINDOW', root.destroy)

        # body font for most labels...
        body_font = ("Arial", "12")

        # List for label details (text | font | background | row)
        play_labels_list = [
            ["Round # of #", ("Arial", "16", "bold"), None, 0],
            ["Score to beat: #", body_font, "#FFF2CC", 1],
            ["Choose a colour below.  Good luck. 🍀", body_font, "#D5E8D4", 2],
            ["You chose, result", body_font, "#D5E8D4", 4]
        ]

        play_labels_ref = []
        for item in play_labels_list:
            self.make_label = Label(self.game_frame, text=item[0], font=item[1],
                                    bg=item[2], wraplength=300, justify="left")
            self.make_label.grid(row=item[3], pady=10, padx=10)

            play_labels_ref.append(self.make_label)

        # Retrieve Labels so they can be configured later
        self.heading_label = play_labels_ref[0]
        self.target_label = play_labels_ref[1]
        self.choose_label = play_labels_ref[2]
        self.results_label = play_labels_ref[3]

        # set up colour buttons...
        self.colour_frame = Frame(self.game_frame)
        self.colour_frame.grid(row=3)

        self.colour_button_ref = []
        self.button_colours_list = []

        # create four buttons in a 2 x 2 grid
        for item in range(0, 4):
            self.colour_button = Button(self.colour_frame, font=("Arial", 12),
                                        text="Colour Name", width=15,
                                        command=partial(self.round_results, item))
            self.colour_button.grid(row=item // 2,
                                    column=item % 2,
                                    padx=5, pady=5)
            self.colour_button_ref.append(self.colour_button)

        # Frame to hold hints and stats buttons
        self.hints_stats_frame = Frame(self.game_frame)
        self.hints_stats_frame.grid(row=6)

        # list for buttons (frame | text | bg | command | width | row | column)
        control_button_list = [
            [self.game_frame, "Next Round", "#0057D8", self.new_round, 21, 5, None],
            [self.hints_stats_frame, "Hints", "#FF8000", self.to_hints, 10, 0, 0],
            [self.hints_stats_frame, "Stats", "#333333", self.to_stats, 10, 0, 1],
            [self.game_frame, "End", "#990000", self.close_play, 21, 7, None]
        ]

        # create buttons and add to list
        control_ref_list = []
        for item in control_button_list:
            make_control_button = Button(item[0], text=item[1], bg=item[2],
                                         command=item[3], font=("Arial", 16, "bold"),
                                         fg="#FFFFFF", width=item[4])
            make_control_button.grid(row=item[5], column=item[6], padx=5, pady=5)

            control_ref_list.append(make_control_button)

        # Retrieve next, stats and end button so that they can be configured
        self.next_button = control_ref_list[0]
        self.hints_button = control_ref_list[1]
        self.stats_button = control_ref_list[2]
        self.end_game_button = control_ref_list[3]

        self.stats_button.config(state=NORMAL)



        # Once interface has been created, invoke new
        # round function for first round.
        self.new_round()

    def new_round(self):

        rounds_played = self.rounds_played.get()
        rounds_wanted = self.rounds_wanted.get()

        # get 4 random country/capital pairs
        self.round_colour_list = get_round_questions()

        #print("ROUND LIST:", self.round_colour_list)

        # pick correct answer
        self.correct_answer = random.randint(0, 3)

        #print(random)
        # get country
        country = self.round_colour_list[self.correct_answer][0]
        #print(self.correct_answer)
        # labels
        #print(self.round_colour_list[self.correct_answer])
        #print(self.colour_button_ref)

        # Exclude all instances of 'a'
        wrong_capitals = [item for item in self.round_colour_list if item != self.round_colour_list[self.correct_answer]]
        print(wrong_capitals)
        if rounds_wanted != -1:
            self.heading_label.config(
                text=f"Round {rounds_played + 1} of {rounds_wanted}"
            )

            self.target_label.config(
                text=f"What is the capital of {country}?"
            )

            self.results_label.config(
                text="Choose a capital",
                bg="#F0F0F0"
            )
        else:
            self.heading_label.config(
                text=f"Round {rounds_played + 1} of Infinite"
            )

            self.target_label.config(
                text=f"What is the capital of {country}?"
            )

            self.results_label.config(
                text="Choose a capital",
                bg="#F0F0F0"
            )

        # put capitals on buttons
        for count, item in enumerate(self.colour_button_ref):
            capital = self.round_colour_list[count][1]

            item.config(
                text=capital,
                state=NORMAL
            )

        self.next_button.config(state=DISABLED)
        self.hints_button.config(state=NORMAL)
        self.was_hint_used = False

    def round_results(self, user_choice):

        chosen_capital = self.round_colour_list[user_choice][1]
        correct_capital = self.round_colour_list[self.correct_answer][1]


        rounds_played = self.rounds_played.get()
        rounds_played += 1
        self.rounds_played.set(rounds_played)

        rounds_won = self.rounds_won.get()

        if chosen_capital == correct_capital:
            result_text = f"Correct! {chosen_capital} is right."
            result_bg = "#82B366"

            rounds_won += 1
            self.rounds_won.set(rounds_won)

        else:
            result_text = f"Wrong! The answer was {correct_capital}"
            result_bg = "#F8CECC"

        self.results_label.config(text=result_text, bg=result_bg)
        self.hints_button.config(state=DISABLED)
        self.next_button.config(state=NORMAL)


        for item in self.colour_button_ref:
            item.config(state=DISABLED)
        rounds_wanted = self.rounds_wanted.get()
        if rounds_played == rounds_wanted and rounds_wanted!= "Infinite":
            success_rate = rounds_won / rounds_played * 100
            success_string = (f"Success rate"
                              f"{rounds_won}/{rounds_played}"
                              f"({success_rate:.2f}%)")
            # configure end game labels / buttons
            self.heading_label.config(text="Game Over")
            self.target_label.config(text=success_string)
            self.choose_label.config(text="Please click the stats"
                                          "button for more info ")
            self.next_button.config(state=DISABLED, text="Game Over")
            self.stats_button.config(bg="#990000")
            self.end_game_button.config(text="Play Again", bg="#006600",
                                        compound="right")
    def close_play(self):
        # reshow root (ie: choose rounds) and end current
        # game / allow new game to star
        root.deiconify()

        self.play_box.destroy()

    def to_hints(self):

        wrong_indexes = []
        self.hints_used =+1
        for i in range(4):
            if i != self.correct_answer:
                wrong_indexes.append(i)

        # pick 2 wrong answers
        buttons_to_disable = random.sample(wrong_indexes, 2)

        # disable them
        for index in buttons_to_disable:
            self.colour_button_ref[index].config(state=DISABLED)

        # prevent multiple hint uses this round

        self.was_hint_used = True

        self.hints_button.config(text=f"Hints {self.hints_used}")
        self.hints_button.config(state=DISABLED)


    def to_stats(self):
        """
        Retrieves everything we need to display the game / round statistics"""
        # IMPORTANT: retrieve number of rounds
        # won as a number (rather than the 'self' container)

        rounds_played = self.rounds_played.get()
        rounds_won = self.rounds_won.get()
        stats_bundle = [rounds_won, self.all_scores_list,
                        self.all_high_score_list,rounds_played,self.hints_used,self.was_hint_used,self.rounds_wanted]

        Stats(self, stats_bundle)


    # this class will refer to the game components for stats and not hints and also close play and more
class hard_game:

    def __init__(self, how_many):

        self.rounds_played = IntVar()
        self.rounds_played.set(0)



        self.rounds_wanted = IntVar()
        self.rounds_wanted.set(how_many)

        self.rounds_won = IntVar()
        self.rounds_won.set(0)

        self.all_scores_list = []
        self.all_high_score_list = []
        self.was_hint_used = False


        self.play_box = Toplevel()

        self.play_box.protocol('WM_DELETE_WINDOW', root.destroy)

        self.start_frame = Frame(self.play_box)
        self.start_frame.grid(padx=10, pady=10)

        # Heading labels
        self.title_label = Label(
            self.start_frame,
            text="Country Capitals 🌍 HARD MODE",
            font=("Arial", 16, "bold")
        )
        self.title_label.grid(row=0)

        self.heading_label = Label(
            self.start_frame,
            text="Loading...",
            font=("Arial", 12)
        )
        self.heading_label.grid(row=1)

        self.results_label = Label(
            self.start_frame,
            text="Type a capital and press Enter",
            font=("Arial", 12),
            wraplength=350
        )
        self.results_label.grid(row=2, pady=10)

        # Entry frame
        self.entry_area_frame = Frame(self.start_frame)
        self.entry_area_frame.grid(row=3)

        self.answer_entry = Entry(
            self.entry_area_frame,
            font=("Arial", 20, "bold"),
            width=15
        )
        self.answer_entry.grid(row=0, column=0, padx=10)

        # Press Enter to submit
        self.answer_entry.bind("<Return>", self.on_enter)

        self.submit_button = Button(
            self.entry_area_frame,
            text="Submit",
            font=("Arial", 14, "bold"),
            bg=("green"),
            fg=("white"),
            command=self.check_answer
        )

        self.submit_button.grid(row=0, column=1)

        self.next_button = Button(
            self.start_frame,
            text="Next Round",
            bg="#0057D8",
            fg="white",
            font=("Arial", 14, "bold"),
            width=20,
            command=self.new_round,
            state=DISABLED
        )
        self.next_button.grid(row=4, pady=10)

        # Stats / End buttons
        self.button_frame = Frame(self.start_frame)
        self.button_frame.grid(row=5, pady=10)

        self.stats_button = Button(
            self.button_frame,
            text="Stats",
            bg="blue",
            fg="white",
            font=("Arial", 14, "bold"),
            command=self.to_stats,
            width=10
        )
        self.stats_button.grid(row=0, column=0, padx=5)

        self.end_button = Button(
            self.button_frame,
            text="End",bg="#990000",fg="white",
            font=("Arial", 14, "bold"),
            command=self.close_play,
            width=10
        )
        self.end_button.grid(row=0, column=1, padx=5)

        self.new_round()

    def new_round(self):
        self.answer_entry.config(state=NORMAL)
        self.submit_button.config(state=NORMAL)
        self.next_button.config(state=DISABLED)

        self.answer_entry.delete(0, END)
        self.answer_entry.focus()

        self.round_colour_list = get_round_questions()

        self.correct_answer = random.randint(0, 3)

        self.country = self.round_colour_list[self.correct_answer][0]
        self.capital = self.round_colour_list[self.correct_answer][1]

        rounds_played = self.rounds_played.get()
        rounds_wanted = self.rounds_wanted.get()

        if rounds_wanted == -1:
            round_text = f"Round {rounds_played + 1} of Infinite"
        else:
            round_text = f"Round {rounds_played + 1} of {rounds_wanted}"

        self.heading_label.config(
            text=f"{round_text}\n\nWhat is the capital of {self.country}?"
        )

        self.answer_entry.delete(0, END)
        self.answer_entry.focus()

    def on_enter(self, event):
        self.check_answer()

    def check_answer(self):

        user_answer = self.answer_entry.get().strip().lower()
        correct_answer = self.capital.strip().lower()

        rounds_played = self.rounds_played.get() + 1
        self.rounds_played.set(rounds_played)

        if user_answer == correct_answer:

            self.rounds_won.set(self.rounds_won.get() + 1)

            self.results_label.config(
                text=f"Correct! {self.capital} is right.",
                bg="#82B366"
            )

        else:

            self.results_label.config(
                text=f"Wrong! The answer was {self.capital}",
                bg="#F8CECC"
            )
        self.submit_button.config(state=DISABLED)
        self.answer_entry.config(state=DISABLED)
        self.next_button.config(state=NORMAL)

        rounds_wanted = self.rounds_wanted.get()

        if rounds_wanted != -1 and rounds_played >= rounds_wanted:

            success_rate = (
                self.rounds_won.get() / rounds_played * 100
            )

            self.heading_label.config(text="Game Over")

            self.results_label.config(
                text=f"Success Rate: {self.rounds_won.get()}/{rounds_played} ({success_rate:.0f}%)"
            )

            self.answer_entry.config(state=DISABLED)
            self.submit_button.config(state=DISABLED)



    def close_play(self):

        root.deiconify()
        self.play_box.destroy()

    def to_stats(self):
        rounds_played = self.rounds_played.get()
        rounds_won = self.rounds_won.get()

        stats_bundle = [
            rounds_won,
            self.all_scores_list,
            self.all_high_score_list,
            rounds_played,
            0,  # hints used
            False,  # was hint used
            self.rounds_wanted
        ]

        Stats(self, stats_bundle)





class Stats:
    """
    Displays stats for Colour Quest Game
    """
    def __init__(self, partner, all_stats_info):

        # disable buttons to prevent program crashing
        if not is_hard:
            partner.end_game_button.config(state=DISABLED)
            partner.stats_button.config(state=DISABLED)

            partner.hints_button.config(state=DISABLED)


            # Extract information from master list...
            rounds_won = all_stats_info[0]
            high_scores = all_stats_info[2]
            rounds_played = all_stats_info[3]
            hintsused = all_stats_info[4]
            self.was_hint_used = all_stats_info[5]

            print(all_stats_info)


            self.stats_box = Toplevel()

            # disable help button
            partner.stats_button.config(state=DISABLED)

            # If users press cross at top, closes help and
            # 'releases' help button
            self.stats_box.protocol('WM_DELETE_WINDOW',
                                    partial(self.close_stats, partner))

            self.stats_frame = Frame(self.stats_box, width=350)
            self.stats_frame.grid()

            # Math to populate Stats dialogue...

            if rounds_won != 0:
                print(f" {rounds_won} / {rounds_played} *100")
                success_rate = rounds_won / rounds_played * 100
                score = (rounds_won * 100)  -(rounds_won*hintsused)

            else:
                success_rate = 0
                score = 0
            print(f" {rounds_won} / {rounds_played} *100")


            max_possible = rounds_played *100



            # Strings for Stats labels...
            hint_string = (f"You have used {hintsused} hints.")
            success_string = (f"Success Rate: {rounds_won} / {rounds_played}"
                              f" ({success_rate:.0f}%)")
            total_score_string = f"Total Score: {score}"
            max_possible_string = f"Maximum Possible Score: {max_possible}"


            # custom comment text and formatting
            if score == max_possible:
                comment_string = ("Amazing!  You got the highest "
                                  "possible score!")
                comment_colour = "#D5E8D4"

            elif score == 0:
                comment_string = ("Oops - You've lost every round!  "
                                  "You might want to look at the hints!")
                comment_colour = "#F8CECC"
                best_score_string = f"Best Score: n/a"
            else:
                comment_string = ""
                comment_colour = "#F0F0F0"



            heading_font = ("Arial", "16", "bold")
            normal_font = ("Arial", "14")
            comment_font = ("Arial", "13")

            # Label list (text | font | 'Sticky')
            all_stats_strings = [
                ["Statistics", heading_font, ""],
                [success_string, normal_font, "W"],
                [hint_string, normal_font,"W"],
                [total_score_string, normal_font, "W"],
                [max_possible_string, normal_font, "W"],
                [comment_string, comment_font, "W"],
                ["\nRound Stats", heading_font, ""]

            ]

            stats_label_ref_list = []
            for count, item in enumerate(all_stats_strings):
                self.stats_label = Label(self.stats_frame, text=item[0], font=item[1], wraplength=300,
                                         anchor="w", justify="left",
                                         padx=30, pady=5)
                self.stats_label.grid(row=count, sticky=item[2], padx=10)
                stats_label_ref_list.append(self.stats_label)

            # Configure comment label background (for all won / all lost)
            stats_comment_label = stats_label_ref_list[4]
            stats_comment_label.config(bg=comment_colour)

            self.dismiss_button = Button(self.stats_frame,
                                         font=("Arial", 16, "bold"),
                                         text="Dismiss", bg="#333333",
                                         fg="#FFFFFF", width=20,
                                         command=partial(self.close_stats,
                                                         partner))
            self.dismiss_button.grid(row=8, padx=10, pady=10)

        # closes help dialogue (used by button and x at top of dialogue)


        else:

            partner.end_button.config(state=DISABLED)
            partner.stats_button.config(state=DISABLED)

            rounds_won = all_stats_info[0]

            rounds_played = all_stats_info[3]

            self.was_hint_used = all_stats_info[5]

            self.stats_box = Toplevel()

            self.stats_box.protocol(
                'WM_DELETE_WINDOW',
                partial(self.close_stats_hard, partner)
            )
            # make the frame to store the stats buttons
            self.stats_frame = Frame(self.stats_box, width=350)
            self.stats_frame.grid()
            # i added this to avoid divide by zero errors as the rounds won would be zero making it indivisible
            if rounds_won != 0:
                success_rate = rounds_won / rounds_played * 100
                score = rounds_won * 100
            else:
                success_rate = 0
                score = 0
            # the max score which is just the maximum possible score
            max_possible = rounds_played * 100

            hint_string = "Hints are disabled in Hard Mode."
            success_string = (
                f"Success Rate: {rounds_won} / {rounds_played}"
                f" ({success_rate:.0f}%)"
            )
            total_score_string = f"Total Score: {score}"
            max_possible_string = f"Maximum Possible Score: {max_possible}"

            if score == max_possible and rounds_played > 0:
                comment_string = (
                    "Amazing! You got the highest possible score!"
                )
                comment_colour = "#D5E8D4"

            elif score == 0:
                comment_string = (
                    "Maybe try easy mode"
                )
                comment_colour = "#F8CECC"

            else:
                comment_string = ""
                comment_colour = "#F0F0F0"

            heading_font = ("Arial", "16", "bold")
            normal_font = ("Arial", "14")
            comment_font = ("Arial", "13")

            all_stats_strings = [
                ["Statistics (Hard Mode)", heading_font, ""],
                [success_string, normal_font, "W"],
                [hint_string, normal_font, "W"],
                [total_score_string, normal_font, "W"],
                [max_possible_string, normal_font, "W"],
                [comment_string, comment_font, "W"],
                ["\nRound Stats", heading_font, ""]
            ]

            stats_label_ref_list = []

            for count, item in enumerate(all_stats_strings):
                self.stats_label = Label(
                    self.stats_frame,
                    text=item[0],
                    font=item[1],
                    wraplength=300,
                    anchor="w",
                    justify="left",
                    padx=30,
                    pady=5
                )

                self.stats_label.grid(
                    row=count,
                    sticky=item[2],
                    padx=10
                )

                stats_label_ref_list.append(self.stats_label)

            stats_comment_label = stats_label_ref_list[4]
            stats_comment_label.config(bg=comment_colour)
            # creates the dismiss button
            self.dismiss_button = Button(
                self.stats_frame,
                font=("Arial", 16, "bold"),
                text="Dismiss",
                bg="#333333",
                fg="#FFFFFF",
                width=20,
                command=partial(self.close_stats_hard, partner)
            )
            # grids the dismiss part of the stats
            self.dismiss_button.grid(row=8, padx=10, pady=10)

    def close_stats(self, partner):
        # Put help button back to normal...
        partner.end_game_button.config(state=NORMAL)
        partner.stats_button.config(state=NORMAL)
        if not self.was_hint_used:
            partner.hints_button.config(state=NORMAL)
        else:
            partner.hints_button.config(state=DISABLED)
        self.stats_box.destroy()

    def close_stats_hard(self, partner):
        # reenables the buttons for hard mode after stats was closed
        partner.end_button.config(state=NORMAL)
        partner.stats_button.config(state=NORMAL)

        self.stats_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Capitals")
    StartGame()
    root.mainloop()