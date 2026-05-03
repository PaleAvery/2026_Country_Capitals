from tkinter import *
from functools import partial # to prevent unwanted windows


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
        # images for use on 'end game' / 'play again' button
        self.earth = PhotoImage(file="earth-png-25612.png")

        # strings for labels
        intro_string = ("For each round you will be given the name of the country and you will be tasked"
                        " with clicking which capital is the capital for the country ")

        # choose_string = "Oops - please choose a whole number more than zero."
        choose_string = "how many Question's would you like to answer?"

        # list of labels to be made (text / Font / fg)
        start_labels_list = [
            ["Country's Capitals ", ("Arial", 16,"bold"), None],
            [intro_string, ("Arial",12), None],
            [choose_string, ("Arial", 12, "bold"), "#009900"]
        ]

        # create labels and add them to the reference list ...

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


        # reset label and entry box (for when users come back to home screen)
        self.choose_label.config(fg="#009900",font=("Arial",12,"bold"))
        self.num_rounds_entry.config(bg="#FFFFFF")

        self.choose_label.config(text=f"You have chosen to play in infinite mode")

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
                # temporary success message replace with call ro play game class
                self.choose_label.config(text=f"you have chosen to answer {questions_wanted} question(s)")
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

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country's Capitals")
    StartGame()
    root.mainloop()