import ascii_strings as astr

ANSI_COLOR_ESCAPE_LENGTH = len("\033[33m\033[0m")


def getLineLength() -> int:
    return len(astr.STR_HEADER.splitlines()[0])


# Takes the different parts for the output and merge them to a single string.
def assembleFrame(animation_frame: int, winner_line: str = ""):
    s = ""
    s = s + astr.STR_HEADER + "\n"
    s = s + winner_line + "\n"
    s = s + astr.STR_PADDING + "\n"
    s = s + astr.STR_ANIMATION[animation_frame] + "\n"
    s = s + astr.STR_FOOTER
    line_count = s.count("\n") + 1
    return s, line_count


# Embeds the winner name into a string that fits the animation.
def buildWinnerLine(winner: str) -> str:
    line_length = getLineLength()
    winner_line = "\033[33m" + winner + "\033[0m"
    padding = (line_length - 2 * astr.FRAME_BORDER_STENGTH - len(winner_line)
               + ANSI_COLOR_ESCAPE_LENGTH) / 2

    # If the necessary padding is uneven, increase the length of the winner
    # by one to avoid that.
    if padding != int(padding):
        winner_line = winner_line + " "
    padding = int(padding)
    winner_line = "==" + " " * padding + winner_line + " " * padding + "=="
    return winner_line


def cleanScreen(line_count: int):
    print("\033[" + str(line_count) + "A", end="")
    print("\033[K", end="")
