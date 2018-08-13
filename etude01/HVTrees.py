# E1 - HV Trees
#
# @author Max Huang
# @since 08 August 2018


# Import statements
import sys
from enum import Enum
from tkinter import Tk, Canvas, Frame, BOTH

# Enums
Direction = Enum('Direction', 'horizontal vertical')

# Constants
WIDTH = 600
HEIGHT = 450

# Variables
x = WIDTH/2
y = HEIGHT/2
depth = 0

# Setting up the canvas.
root = Tk()
root.title("HV Trees")
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='white')
canvas.pack()


# Draws the line extending out from a given coordinate in a given direction.
#
# @param x - x coord.
# @param y - y coord.
# @param len - length of the line.
# @param dir - an enum specifying the direction of the line.
def draw(x, y, len, dir):
    global canvas, root
    if (dir == Direction.horizontal):
        canvas.create_line(x-len/2, y, x+len/2, y)
    else:
        canvas.create_line(x, y-len/2, x, y+len/2)


# A recursive function to draw the HV Tree.
#
# @param x - x coord.
# @param y - y coord.
# @param len - length of the line.
# @param depth - the current depth of the tree.
def line(x, y, len, depth):
    global order, factor

    if order == depth or len < 1:
        return
    else:
        if depth % 2 == 0:
            draw(x, y, len, dir = Direction.horizontal)
            depth += 1
            line(x+len/2, y, len*factor, depth)
            return line(x-len/2, y, len*factor, depth)
        else:
            draw(x, y, len, dir = Direction.vertical)
            depth += 1
            line(x, y+len/2, len*factor, depth)
            return line(x, y-len/2, len*factor, depth)


# MAIN
if __name__ == "__main__":
    # Command line arguments
    order = int(sys.argv[1])
    factor = float(sys.argv[2])
    if factor >= 0 or factor < 1:
        if order < 0:
            order = 0
        line(x, y, 300, depth)
        root.mainloop()
    else:
        print("Factor must be between 0 and 1")