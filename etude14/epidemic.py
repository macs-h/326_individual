#!/usr/bin/env python3

# E14 - Epidemic
#
# @author Max Huang
# @since 19 September 2018
# @version 1.0

import sys
from enum import Enum

class S(Enum):
    SICK = 'S'
    IMMUNE = 'I'
    NONSICK = '.'

class Node:
    def __init__(self, state, left, right, top, bottom):
        self.state = state
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def toString(self):
        return self.state.value

    def __str__(self):
        # return self.state.name
        return self.state.value

#*****************************************************************************80

if __name__ == '__main__':
    # Get input from stdin.
    inputGrid = []
    actualGrid = []


    while True:
        try:
            line = input()
            print(line)
            col = line.split()
            inputGrid.append(col)
            actualGrid.append([0]*len(col))
        except:
            break

    print()
    print(actualGrid)
    print()
    for row in range(len(inputGrid)):
        # print(len(inputGrid))
        # print(row)
        # len(inputGrid)-1
        for col in range(len(inputGrid[row])):
            # print(len(inputGrid[row]))
            if row == 0:
                #& Top row.
                if col == 0:
                    #& Top left.
                    if inputGrid[row][col] == "I":
                        actualGrid[row][col] = Node(S.IMMUNE, None, actualGrid[row][col+1], None, actualGrid[row+1][col])
                    elif inputGrid[row][col] == "S":
                        actualGrid[row][col] = Node(S.SICK, None, actualGrid[row][col+1], None, actualGrid[row+1][col])
                    elif inputGrid[row][col] == ".":
                        actualGrid[row][col] = Node(S.NONSICK, None, actualGrid[row][col+1], None, actualGrid[row+1][col])
                elif col == len(inputGrid[row])-1:
                    #& Top right.
                    if inputGrid[row][col] == "I":
                        actualGrid[row][col] = Node(S.IMMUNE, actualGrid[row][col-1], None, None, actualGrid[row+1][col])
                    elif inputGrid[row][col] == "S":
                        actualGrid[row][col] = Node(S.SICK, actualGrid[row][col-1], None, None, actualGrid[row+1][col])
                    elif inputGrid[row][col] == ".":
                        actualGrid[row][col] = Node(S.NONSICK, actualGrid[row][col-1], None, None, actualGrid[row+1][col])
                else:
                    #& Top row
                    if inputGrid[row][col] == "I":
                        actualGrid[row][col] = Node(S.IMMUNE, actualGrid[row][col-1], actualGrid[row][col+1], None, actualGrid[row+1][col])
                    elif inputGrid[row][col] == "S":
                        actualGrid[row][col] = Node(S.SICK, actualGrid[row][col-1], actualGrid[row][col+1], None, actualGrid[row+1][col])
                    elif inputGrid[row][col] == ".":
                        actualGrid[row][col] = Node(S.NONSICK, actualGrid[row][col-1], actualGrid[row][col+1], None, actualGrid[row+1][col])

            elif row == len(inputGrid)-1:
                #& Bottom row.
                if col == 0:
                    #& Bottom left.
                    if inputGrid[row][col] == "I":
                        actualGrid[row][col] = Node(S.IMMUNE, None, actualGrid[row][col+1], actualGrid[row-1][col], None)
                    elif inputGrid[row][col] == "S":
                        actualGrid[row][col] = Node(S.SICK, None, actualGrid[row][col+1], actualGrid[row-1][col], None)
                    elif inputGrid[row][col] == ".":
                        actualGrid[row][col] = Node(S.NONSICK, None, actualGrid[row][col+1], actualGrid[row-1][col], None)
                elif col == len(inputGrid[row])-1:
                    #& Bottom right.
                    if inputGrid[row][col] == "I":
                        actualGrid[row][col] = Node(S.IMMUNE, actualGrid[row][col-1], None, actualGrid[row-1][col], None)
                    elif inputGrid[row][col] == "S":
                        actualGrid[row][col] = Node(S.SICK, actualGrid[row][col-1], None, actualGrid[row-1][col], None)
                    elif inputGrid[row][col] == ".":
                        actualGrid[row][col] = Node(S.NONSICK, actualGrid[row][col-1], None, actualGrid[row-1][col], None)
                else:
                    #& Bottom row.
                    if inputGrid[row][col] == "I":
                        actualGrid[row][col] = Node(S.IMMUNE, actualGrid[row][col-1], actualGrid[row][col+1], actualGrid[row-1][col], None)
                    elif inputGrid[row][col] == "S":
                        actualGrid[row][col] = Node(S.SICK, actualGrid[row][col-1], actualGrid[row][col+1], actualGrid[row-1][col], None)
                    elif inputGrid[row][col] == ".":
                        actualGrid[row][col] = Node(S.NONSICK, actualGrid[row][col-1], actualGrid[row][col+1], actualGrid[row-1][col], None)

            else:
                #& Other rows.
                if col == 0:
                    #& First column.
                    if inputGrid[row][col] == "I":
                        actualGrid[row][col] = Node(S.IMMUNE, None, actualGrid[row][col+1], actualGrid[row-1][col], actualGrid[row+1][col])
                    elif inputGrid[row][col] == "S":
                        actualGrid[row][col] = Node(S.SICK, None, actualGrid[row][col+1], actualGrid[row-1][col], actualGrid[row+1][col])
                    elif inputGrid[row][col] == ".":
                        actualGrid[row][col] = Node(S.NONSICK, None, actualGrid[row][col+1], actualGrid[row-1][col], actualGrid[row+1][col])
                elif col == len(inputGrid[row])-1:
                    #& Middle columns
                    if inputGrid[row][col] == "I":
                        actualGrid[row][col] = Node(S.IMMUNE, actualGrid[row][col-1], None, actualGrid[row-1][col], actualGrid[row+1][col])
                    elif inputGrid[row][col] == "S":
                        actualGrid[row][col] = Node(S.SICK, actualGrid[row][col-1], None, actualGrid[row-1][col], actualGrid[row+1][col])
                    elif inputGrid[row][col] == ".":
                        actualGrid[row][col] = Node(S.NONSICK, actualGrid[row][col-1], None, actualGrid[row-1][col], actualGrid[row+1][col])
                else:
                    #& Last column.
                    if inputGrid[row][col] == "I":
                        actualGrid[row][col] = Node(S.IMMUNE, actualGrid[row][col-1], actualGrid[row][col+1], actualGrid[row-1][col], actualGrid[row+1][col])
                    elif inputGrid[row][col] == "S":
                        actualGrid[row][col] = Node(S.SICK, actualGrid[row][col-1], actualGrid[row][col+1], actualGrid[row-1][col], actualGrid[row+1][col])
                    elif inputGrid[row][col] == ".":
                        actualGrid[row][col] = Node(S.NONSICK, actualGrid[row][col-1], actualGrid[row][col+1], actualGrid[row-1][col], actualGrid[row+1][col])


                        
    #?----------------------

    for row in range(len(actualGrid)):
        for col in range(len(actualGrid[row])):
            print(actualGrid[row][col], end=" ")
        print()





    #!------------------------------------------------------------------------80
    # # Process the input.
    # gridLen = len(inputGrid) + 2
    # # actualGrid = [[None for i in range(gridLen + 2)] for j in range(gridLen + 2)]
    # print()
    # actualGrid = [[None]*(gridLen)]*(gridLen)
    # actualGrid = []*gridLen
    # # for row in actualGrid:
    # #     row.append([]*gridLen)

    # for row in actualGrid:
    #     print(row)

    # for row in range(gridLen):
    #     #& If FIRST row, make IMMUNE.
    #     if row == 0:
    #         for col in range(len(actualGrid[row])):
    #             #& If first, no need for pointers to sides.
    #             if col == 0:
    #                 #& Top LEFT corner.
    #                 actualGrid[row][col] = Node(S.IMMUNE, None, actualGrid[row][col+1], None, actualGrid[row+1][col])
    #             elif col == gridLen-1:
    #                 #& Top RIGHT corner.
    #                 actualGrid[row][col] = Node(S.IMMUNE, actualGrid[row][col-1], None, None, actualGrid[row+1][col])
    #             else:
    #                 #& Top row.
    #                 actualGrid[row][col] = Node(S.IMMUNE, actualGrid[row][col-1], actualGrid[row][col+1], None, actualGrid[row+1][col])

    #     #& If LAST row, make IMMUNE.
    #     elif row == gridLen-1:
    #         for col in range(len(actualGrid[row])):
    #             #& If last, no need for pointers to sides.
    #             if col == 0:
    #                 #& Bottom LEFT corner.
    #                 actualGrid[row][col] = Node(S.IMMUNE, None, actualGrid[row][col+1], actualGrid[row-1][col], None)
    #             elif col == gridLen-1:
    #                 #& Bottom RIGHT corner.
    #                 actualGrid[row][col] = Node(S.IMMUNE, actualGrid[row][col-1], None, actualGrid[row-1][col], None)
    #             else:
    #                 print(row, col)
    #                 #& Bottom row.
    #                 actualGrid[row][col] = Node(S.IMMUNE, actualGrid[row][col-1], actualGrid[row][col+1], actualGrid[row-1][col], None)

    #     else:
    #         print(row)
    #         for col in range(len(actualGrid[row])):

    #             #& If not first or last row.
    #             if col == 0:
    #                 #& If FIRST col, make IMMUNE.
    #                 print("-", row, col)
    #                 actualGrid[row][col] = Node(S.SICK, None, actualGrid[row][col+1], actualGrid[row-1][col], actualGrid[row+1][col])
    #             elif col == gridLen-1:
    #                 #& If LAST col, make IMMUNE.
    #                 print("--", row, col)
    #                 actualGrid[row][col] = Node(S.SICK, actualGrid[row][col-1], None, actualGrid[row-1][col], actualGrid[row+1][col])

    # print()
    # # n = Node(S.SICK, None, None, None, None)
    # for row in range(gridLen):
    #     for col in range(len(actualGrid[row])):
    #         print(actualGrid[row][col], end=" ")
    #         # print(n)
    #     print("\n", end="")

