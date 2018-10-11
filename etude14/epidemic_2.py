#!/usr/bin/env python3

# E14 - Epidemic (pt 2)
#
# @author Max Huang
# @since 25 September 2018
# @version 1.0

import sys
import math
from enum import Enum

class S(Enum):
    SICK = 'S'
    IMMUNE = 'I'
    NONSICK = '.'

class Node:
    def __init__(self, state, neighbours, immuneCount):
        self.state = state
        self.neighbours = neighbours
        self.immuneCount = immuneCount

    def __str__(self):
        # return self.state.value
        return str(self.immuneCount)

#*****************************************************************************80

def checkNeighboursOf(node):
    global actualGrid
    sickCount = 0
    immuneCount = 0

    for neighbour in node.neighbours:
        if actualGrid[neighbour[0]][neighbour[1]].state == S.SICK:
            sickCount += 1
        elif actualGrid[neighbour[0]][neighbour[1]].state == S.IMMUNE:
            immuneCount += 1

    neighbourCount = len(node.neighbours)
    if neighbourCount == 3:
        #& Edge node
        immuneCount += 1
    elif neighbourCount == 2:
        #& Corner node
        immuneCount += 2
    elif neighbourCount == 1:
        immuneCount += 3

    return sickCount, immuneCount

#*****************************************************************************80

def updateNeighbours(row, col):
    neighbours = []

    if row-1 >= 0:
        #& Yes top.
        neighbours.append([row-1, col])
    if row+1 <= len(inputGrid)-1:
        #& Yes bottom.
        neighbours.append([row+1, col])
    if col-1 >= 0:
        #& Yes left.
        neighbours.append([row, col-1])
    if col+1 <= len(inputGrid[row])-1:
        #& Yes right.
        neighbours.append([row, col+1])
    return neighbours

#*****************************************************************************80

if __name__ == '__main__':

    #?------------------------------------------------------------------------80
    # When checking neighbours, if the neighbour does not exist then treat it
    #  as if that neighbour is immune.
    #
    # The minimum amount of sick cells required is the perimeter of immune
    #  cells divided by 4. The ceiling of: (Immune.count)/4
    #
    #? When placing sick cells, first place at cells which have an immune
    #?  neighbour count of >= 3 because impossible to infect those cells.
    #? Place remainder of sick cells randomly - generate this enough times until
    #?  either the board is completely infected or you need to increase the
    #?  starting number of sick cells by 1.
    #?
    # As soon as there is no change on an infection cycle, break out from the
    #  loop.
    #?
    #? Two sick cells should not be adjacent to each other.
    #?------------------------------------------------------------------------80

    while True:
        inputGrid = []
        actualGrid = []
        noInput = False
        mustBeSick = []

        #& Getting input.
        while True:
            try:
                line = input()
                if line == "":
                    break
                col = line.split()
                inputGrid.append(col)
                actualGrid.append([0]*len(col))
            except EOFError:
                noInput = True
                break

        #& Assigning nodes to `actualGrid`.
        for row in range(len(inputGrid)):
            for col in range(len(inputGrid[row])):
                neighbours = updateNeighbours(row, col)

                # if inputGrid[row][col] == "S":
                #     actualGrid[row][col] = Node(S.SICK, neighbours, 0)
                if inputGrid[row][col] == "I":
                    actualGrid[row][col] = Node(S.IMMUNE, neighbours, 0)
                elif inputGrid[row][col] == ".":
                    actualGrid[row][col] = Node(S.NONSICK, neighbours, 0)

        #& Check immune count and calculate min number of sick cells required.
        minSickCells = 0
        # gridSize = 0
        for row in range(len(actualGrid)):
            for col in range(len(actualGrid[row])):
                if actualGrid[row][col].state != S.IMMUNE:
                    sickCount, immuneCount = checkNeighboursOf(actualGrid[row][col])
                    actualGrid[row][col].immuneCount = immuneCount

                    #& If cell has 3 or more immune cells around it, add to
                    #& the array of cells that must be infected.
                    if immuneCount >= 3:
                        # print("--", row, col, immuneCount)
                        mustBeSick.append([row, col])
                    minSickCells += immuneCount
                    # gridSize += 1

        # print("Perimeter:", minSickCells)
        minSickCells = math.ceil(minSickCells/4)
        print("{} -> required".format(minSickCells))

        #& -------------------------------------------------------------------80
        #& For this current grid, loop till you find the right solution

        #& Infect the initial cells that MUST be sick.
        numSickCells = minSickCells
        for cell in mustBeSick:
            # print(cell)
            actualGrid[cell[0]][cell[1]].state = S.SICK
            # print(cell[0], cell[1])
            # print(actualGrid[cell[0]][cell[1]].state)
            numSickCells -= 1

        print("{} -> remaining".format(numSickCells))

        #!--------------------------------------------------------------------80
        #& Infect the grid with the rest of the available sick cells, randomly.



        #!--------------------------------------------------------------------80

        #& Infection cycle.
        while True:
            noChange = True
            for row in range(len(actualGrid)):
                for col in range(len(actualGrid[row])):
                    sickCount, immuneCount = checkNeighboursOf(actualGrid[row][col])

                    # actualGrid[row][col].immuneCount = immuneCount
                    if sickCount >= 2 and actualGrid[row][col].state == S.NONSICK:
                        actualGrid[row][col].state = S.SICK
                        noChange = False
            if noChange:
                break

        #& -------------------------------------------------------------------80

        # Print out the final grid.
        # print("--- Final grid ---")
        print("{} -> used".format(minSickCells-numSickCells))
        print("--------------")
        for row in range(len(actualGrid)):
            for col in range(len(actualGrid[row])):
                print(actualGrid[row][col].state.value, end=" ")
            print()
        print()

        if noInput:
            exit(0)