# E5 - Poker Hands
#
# @author Max Huang
# @since 14 August 2018
# @version 1.0

# Import statements
import sys
from enum import Enum

moreInput = True

if __name__ == "__main__":
    while moreInput:
        CL = input("Input: ")
        if CL == "":
            moreInput = False