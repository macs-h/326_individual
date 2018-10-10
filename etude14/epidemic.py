#!/usr/bin/env python3

# E14 - Epidemic
#
# @author Max Huang
# @since 25 September 2018
# @version 1.0

import sys
from enum import Enum

class S(Enum):
    SICK = 'S'
    IMMUNE = 'I'
    NONSICK = '.'

class Node:
    def __init__(self, state, neighbours):
        self.state = state
        self.neighbours = neighbours

    def __str__(self):
        return self.state.value

#*****************************************************************************80

def checkNeighboursOf(node):
    global actualGrid
    count = 0
    for neighbour in node.neighbours:
        if actualGrid[neighbour[0]][neighbour[1]].state == S.SICK:
            count += 1
    return count

#*****************************************************************************80

def updateNeighbours(row, col):
    neighbours = []
    #& Check left
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

    while True:
        inputGrid = []
        actualGrid = []
        noInput = False
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

        for row in range(len(inputGrid)):
            for col in range(len(inputGrid[row])):
                neighbours = updateNeighbours(row, col)

                if inputGrid[row][col] == "S":
                    actualGrid[row][col] = Node(S.SICK, neighbours)
                elif inputGrid[row][col] == "I":
                    actualGrid[row][col] = Node(S.IMMUNE, neighbours)
                elif inputGrid[row][col] == ".":
                    actualGrid[row][col] = Node(S.NONSICK, neighbours)

        #& Infect
        while True:
            noChange = True
            for row in range(len(actualGrid)):
                for col in range(len(actualGrid[row])):
                    if checkNeighboursOf(actualGrid[row][col]) >= 2 and actualGrid[row][col].state == S.NONSICK:
                        actualGrid[row][col].state = S.SICK
                        noChange = False
            if noChange:
                break


        # Print out the final grid.
        for row in range(len(actualGrid)):
            for col in range(len(actualGrid[row])):
                print(actualGrid[row][col], end=" ")
            print()
        print()

        if noInput:
            exit(0)