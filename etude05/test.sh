#!/bin/bash

printf "Compiling main.swift\n"
swiftc PokerHands/PokerHands/main.swift
cat input.txt | swift PokerHands/PokerHands/main.swift 1> output.txt

printf "Running diff on ACTUAL vs EXPECTED output...\n"
diff output.txt expected_output.txt