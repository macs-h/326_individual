#!/bin/bash

# Test script for Poker Hands.

printf "Compiling main.swift...\n"
swiftc PokerHands/PokerHands/main.swift 2> .compiletime_errors.txt

if [ -s .compiletime_errors.txt ]
then
    printf "Compile time warnings and/or errors:\n"
    echo   "------------------------------------"
    cat .compiletime_errors.txt
else
    printf "No compile time warnings or errors.\n"

    cat input.txt | ./main 1> output.txt 2> .runtime_output.txt

    if [ -s .runtime_output.txt ]
    then
        printf "Run time warnings and/or errors:\n"
        echo   "------------------------------------"
        cat .runtime_output.txt
    else
        printf "No run time warnings or errors.\n"
        echo   "------------------------------------"
        printf "Diff on ACTUAL vs EXPECTED output...\n"

        diff output.txt expected_output.txt
    fi
fi


