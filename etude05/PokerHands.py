# E5 - Poker Hands
#
# @author Max Huang
# @since 14 August 2018


# Import statements
import sys
from enum import Enum

class card_enum(Enum):
    ACE = 1

cards = [
    ['1', '']
]

cards = {
    # "one": ["1", "a", "A"],
    1: {"1", "a", "A"},
    2: "two"
}

print(cards.get("two"))

if "a" in cards.values():
    print("yes")