#!/usr/bin/env python3

# E14 - Epidemic (pt 2)
#
# @author Max Huang
# @since 25 September 2018
# @version 1.0

import sys
import math
import random
import copy
import time
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

def checkNeighboursOf(grid, node):
    sickCount = 0
    immuneCount = 0
    sickNearby = False

    for neighbour in node.neighbours:
        if grid[neighbour[0]][neighbour[1]].state == S.SICK:
            sickCount += 1
            sickNearby = True
        elif grid[neighbour[0]][neighbour[1]].state == S.IMMUNE:
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

    return sickCount, immuneCount, sickNearby

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

def getTime(time_elapsed):
    hours, rem = divmod(time_elapsed, 3600)
    minutes, seconds = divmod(rem, 60)
    return "{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds)

#*****************************************************************************80

if __name__ == '__main__':
    start_time = time.time()

    #?------------------------------------------------------------------------80
    # When checking neighbours, if the neighbour does not exist then treat it
    #  as if that neighbour is immune.
    #
    # The minimum amount of sick cells required is the perimeter of immune
    #  cells divided by 4. The ceiling of: (Immune.count)/4
    #
    # When placing sick cells, first place at cells which have an immune
    #  neighbour count of >= 3 because impossible to infect those cells.
    # Place remainder of sick cells randomly - generate this enough times until
    #  either the board is completely infected or you need to increase the
    #  starting number of sick cells by 1.
    #
    # As soon as there is no change on an infection cycle, break out from the
    #  loop.
    #
    # Two sick cells should not be adjacent to each other.
    #?------------------------------------------------------------------------80

    while True:
        inputGrid = []
        actualGrid = []
        noInput = False
        mustBeSick = []
        randInitGrid = []
        initialGrid = []

        #& Getting input.
        while True:
            try:
                line = input()
                if line == "":
                    break
                col = list(line)
                inputGrid.append(col)
                actualGrid.append([0]*len(col))
            except EOFError:
                noInput = True
                break

        #& Assigning nodes to `actualGrid`.
        for row in range(len(inputGrid)):
            for col in range(len(inputGrid[row])):
                neighbours = updateNeighbours(row, col)

                if inputGrid[row][col] == "I":
                    actualGrid[row][col] = Node(S.IMMUNE, neighbours, 0)
                elif inputGrid[row][col] == ".":
                    actualGrid[row][col] = Node(S.NONSICK, neighbours, 0)

        #& Check immune count and calculate min number of sick cells required.
        minSickCells = 0
        for row in range(len(actualGrid)):
            for col in range(len(actualGrid[row])):
                if actualGrid[row][col].state != S.IMMUNE:
                    sickCount, immuneCount, sickNearby = checkNeighboursOf(actualGrid, actualGrid[row][col])
                    actualGrid[row][col].immuneCount = immuneCount

                    #& If cell has 3 or more immune cells around it, add to
                    #& the array of cells that must be infected.
                    if immuneCount >= 3:
                        mustBeSick.append([row, col])
                    minSickCells += immuneCount

        minSickCells = math.ceil(minSickCells/4)

        #& -------------------------------------------------------------------80
        #& For this current grid, loop till you find the right solution

        #& Infect the initial cells that MUST be sick.
        numSickCells = minSickCells

        for cell in mustBeSick:
            row = cell[0]
            col = cell[1]
            actualGrid[row][col].state = S.SICK
            numSickCells -= 1

        #& Infect the grid with the rest of the available sick cells, randomly.

        count = 0
        while True:
            randInitGrid = copy.deepcopy(actualGrid)
            fullyInfected = True
            sickLeft = numSickCells

            while sickLeft > 0:
                r = random.randint(0, len(randInitGrid)-1)
                c = random.randint(0, len(randInitGrid[0])-1)

                cell = randInitGrid[r][c]
                sickCount, immuneCount, sickNearby = checkNeighboursOf(randInitGrid, randInitGrid[r][c])

                #& If sick or immune and no sick neighbours
                if cell.state != S.NONSICK:
                    r = random.randint(0, len(randInitGrid)-1)
                    c = random.randint(0, len(randInitGrid[0])-1)
                else:
                    randInitGrid[r][c].state = S.SICK
                    sickLeft -= 1

            initialGrid = copy.deepcopy(randInitGrid)

            #& Infection cycle.
            while True:
                noChange = True
                for row in range(len(randInitGrid)):
                    for col in range(len(randInitGrid[row])):
                        sickCount, immuneCount, sickNearby = checkNeighboursOf(randInitGrid, randInitGrid[row][col])

                        if sickCount >= 2 and randInitGrid[row][col].state == S.NONSICK:
                            randInitGrid[row][col].state = S.SICK
                            noChange = False
                if noChange:
                    break

            #& Check if fully infected.
            for row in range(len(randInitGrid)):
                for col in range(len(randInitGrid[row])):
                    if randInitGrid[row][col].state == S.NONSICK:
                        fullyInfected = False

            count += 1
            if count % 12000 == 0:
                print("UP at: {} | min: {}".format(count, minSickCells))
                minSickCells += 1
                numSickCells += 1
            if fullyInfected:
                break

        actualGrid = randInitGrid

        #---------------------------------------------------------------------80

        print(minSickCells)

        for row in range(len(initialGrid)):
            for col in range(len(initialGrid[row])):
                print(initialGrid[row][col].state.value, end=" ")
            print()
        print()

        if noInput:
            print(getTime(time.time() - start_time))
            exit(0)