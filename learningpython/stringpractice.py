from enum import Enum

class Align(Enum):
    MIDDLE=1,
    LEFT=2,
    RIGHT=3

def print_star(row, align:Align=Align.LEFT):
    asterix = "*"
    actual_row_count = row * 2
    for i in range(0, actual_row_count):
        half_width = 0  #  Default left assignment
        if i % 2 == 0:  # hide the even lines where spaces are not sync
            continue
        if align==Align.RIGHT:
            half_width = (actual_row_count - i)
        elif align == Align.MIDDLE:
            half_width = (actual_row_count - i)//2
        print(r" " * half_width, end="")
        print(asterix * i)
    return None


print_star(13, Align.MIDDLE)
