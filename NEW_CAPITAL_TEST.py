import csv
import random

def round_ans(val):
    """
    rounds numbers to nearest integer
    :param val: number to be rounded.
    :return: rounded number ( an integer)
    """
    var_rounded = (val * 2 +1) // 2
    raw_rounded = "{:.2f}".format(var_rounded)
    return int(raw_rounded)

file = open("country_capitals.csv","r")
all_colours = list(csv.reader(file,delimiter=","))
file.close()

all_colours.pop(0)

round_capitals = []
country_tocap = []

while len(round_capitals) <4:
    potential_capital = random.choice(all_colours)
    round_capitals.append(potential_capital)
    country_tocap.append(potential_capital[1])


print(round_capitals)
print(country_tocap)

# find target score(median)

# change scores to integers
