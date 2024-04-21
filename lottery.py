import random as rd
import time
import math
import sys

from visual_helper import *

MAX_OPTION_LENGTH = 25

def isBadString(s: str):
    bad_chars = set("~/[];|&$<>\\\"'`")
    return any(char in bad_chars for char in s)


def performRoll(sample_space):
    # Play animation: each iteration one frame.
    for i in range(0, 60):
        running_winner = sample_space[i % len(sample_space)]
        winner_line = buildWinnerLine(running_winner)
        frame, line_count = assembleFrame(i % 2, winner_line)
        print(frame)

        # slow down as closer we get to the true winner
        time.sleep(math.exp(0.1 * i) * 0.001)
        cleanScreen(line_count)

    # It's time to reveal the true winner.
    rd.seed()
    winner = sample_space[rd.randrange(0, len(sample_space))]
    winner = "٩( ᐛ )و  " + winner + "  ٩( ᐛ )و"
    winner_line = buildWinnerLine(winner)
    frame, line_count = assembleFrame(astr.WINNER_ANIMATION_FRAME, winner_line)
    print(frame)


def main():
    # Runtime arguments.
    if len(sys.argv) < 2:
        print("Error: Please provide a file. Usage: lottery.py <filename>")
        sys.exit(1)
    file_path = sys.argv[1]

    # Read options to choose from.
    with open(file_path, "r") as f:
        sample_space = f.readlines()
        sample_space = [s.strip() for s in sample_space]  # remove \n
        f.close

        # Is any of the options too long?
        if any(len(s) > 25 for s in sample_space):
            print("Error: The maximum length for an option is " +
                  str(MAX_OPTION_LENGTH) + ".")
            sys.exit(1)

        # any bad strings?
        if any(isBadString(s) for s in sample_space):
          print("Error: Do not use special characters for your options.")
          sys.exit(1)

    performRoll(sample_space)


if __name__ == "__main__":
    main()
