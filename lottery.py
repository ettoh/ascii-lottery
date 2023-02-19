import random as rd
import time
import math
import os

import ascii_strings as astr


def assembleFrame(animation_frame: str, winner_line: str) -> str:
    s = ""
    s = s + astr.HEADER + "\n"
    s = s + winner_line + "\n"
    s = s + astr.PADDING + "\n"
    s = s + astr.ANIMATION[animation_frame] + "\n"
    s = s + astr.FOOTER
    return s


# constants
INPUT_FILE_PATH = "input.txt"
LINE_LENGTH = 47
LINE_COUNT = assembleFrame(0, "").count("\n") + 1


def cleanScreen(lcount):
    print("\033[" + str(lcount) + "A", end="")
    print("\033[K", end="")


def performRoll(sample_space):
    # init random generator
    rd.seed()

    # choose a random item
    selected_sample = sample_space[rd.randrange(0, len(sample_space))]

    # Play a sound in the background
    # TODO what if the soundfile does not exist? 
    # TODO custom soundfile
    # os.system('afplay sound.wav &')

    for i in range(0, 60):
        s = "\033[33m" + sample_space[i % len(sample_space)] + "\033[0m"

        spacing = (LINE_LENGTH - 4 - len(s) + 9) / 2
        if spacing != int(spacing):
            s = s + " "
        spacing = int(spacing)
        winner_line = "==" + " " * spacing + s + " " * spacing + "=="
        print(assembleFrame(i % 2, winner_line))

        # clear previous output
        cleanScreen(LINE_COUNT)
        time.sleep(math.exp(0.1 * i) * 0.001)

    s = "٩( ᐛ )و  \033[33m" + selected_sample + "\033[0m  ٩( ᐛ )و"
    spacing = (LINE_LENGTH - 4 - len(s) + 9) / 2
    if spacing != int(spacing):
        s = s + " "
    spacing = int(spacing)
    winner_line = "==" + " " * spacing + s + " " * spacing + "=="
    print(assembleFrame(2, winner_line))


# read options to randomly choose from
# TODO check if file was opened correctly
# TODO custom input file
f = open(INPUT_FILE_PATH, "r")
sample_space = f.readlines()
sample_space = [s.strip() for s in sample_space]  # remove \n
f.close

# name roll
performRoll(sample_space)

# number roll
numbers = ["0", "1", "1", "2", "1", "2", "2", "π", "0",
           "max(x2, 1)", "-1", "x0 + 1", "ghost mode", "/2", "ngo", "the MArXisTs", "barter"]
input() # wait until user input
cleanScreen(LINE_COUNT + 1)
performRoll(numbers)
