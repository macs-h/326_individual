//
//  main.swift
//  PokerHands
//
//  Created by Max Huang on 21/08/18.
//  Copyright © 2018 Max Huang. All rights reserved.
//
//  Version 2.1

import Foundation

/**
    Custom exception to be thrown if there is invalid input.
 */
enum PHError: Error {
    case invalidInput
}

/**
    A dictionary holding the numerical values for the corresponding letters.
 */
let cardStr: NSDictionary = [ "a" : "1",
                              "t" : "10",
                              "j" : "11",
                              "q" : "12",
                              "k" : "13" ]

/**
 A struct to define how to hold each card.
 */
struct Cards {
    var card: Int
    var suit: String
}

/**
    Converts the numerical value of the card to a `String` value.

    - parameter card:   The numerical value of the card to be converted.
    - returns:  The corresponding `String` representation of that card.
 */
func getCardString(_ card:Int) -> String {
    if card == 1 {
        return "a"
    } else if card == 11 {
        return "j"
    } else if card == 12 {
        return "q"
    } else if card == 13 {
        return "k"
    } else {
        return String(card)
    }
}


while let input = readLine(strippingNewline: true) {
    
    // Holds the result of separating the input by 'separator' in an array.
    var inputCards = [String]()
    
    // Converts all input to lowercase for ease of String handling.
    let line = input.lowercased()
    
    do {
        if line.contains(" ") && !line.contains("/") && !line.contains("-") {
            if line.first == " " || line.last == " " {
                throw PHError.invalidInput
            }
            // Separate based on whitespace.
            inputCards = line.split(separator: " ").map({String($0)})
        } else if line.contains("/") && !line.contains("-") && !line.contains(" ") {
            if line.first == "/" || line.last == "/"{
                throw PHError.invalidInput
            }
            // Separate based on forward slash.
            inputCards = line.split(separator: "/").map({String($0)})
        } else if line.contains("-") && !line.contains("/") && !line.contains(" ") {
            if line.first == "-" || line.last == "-"{
                throw PHError.invalidInput
            }
            // Separate based on dash.
            inputCards = line.split(separator: "-").map({String($0)})
        } else {
            throw PHError.invalidInput
        }
        
        // Check there are 5 cards in the deck.
        guard inputCards.count == 5 else {
            throw PHError.invalidInput
        }
        
        // Remove all duplicates from the deck.
        inputCards = inputCards.reduce(into: [String]()) {
            if !$0.contains($1) {
                $0.append($1)
            }
        }
        
        // Check there are 5 cards in the deck, after removing any duplicates.
        guard inputCards.count == 5 else {
            throw PHError.invalidInput
        }
        
        var deck = [Cards]()
        for eachCard in inputCards {
            
            // Check that each card has a valid suit.
            guard eachCard.contains("c") || eachCard.contains("d") || eachCard.contains("h") || eachCard.contains("s") else {
                    throw PHError.invalidInput
            }
            
            let startIndex = eachCard.startIndex
            let endIndex = eachCard.index(of: eachCard.last!)
            var card = String( eachCard[startIndex..<endIndex!] )
            let suit = eachCard.last!
            
            // If the card 'number' is a letter, then find the corresponding
            // integer representation of that card in the dictionary.
            if Int(card) == nil {
                if let tmp = cardStr[card] as? String {
                    card = tmp
                } else {
                    // Invalid string.
                    throw PHError.invalidInput
                }
            }
            
            // Check that all cards in the deck are within the valid range.
            guard Int(card)! >= 1 && Int(card)! <= 13 else {
                throw PHError.invalidInput
            }
            
            deck.append(Cards(card: Int(card)!, suit: String(suit)))
            
        } // end for each loop.
        
        
        // Sort deck by card number. If the number is equal, then sort by suit.
        deck = deck.sorted(by: {
            if ($0.card == $1.card) {
                return $0.suit < $1.suit
            }
            return $0.card < $1.card
        })
        
        var finalDeck = [String]()
        var acesInDeck = [String]()
        for card in deck {
            if card.card == 1 {
                acesInDeck.append( (getCardString(card.card) + card.suit).uppercased())
            } else {
                finalDeck.append( (getCardString(card.card) + card.suit).uppercased())
            }
        }
        
        // This ensures that aces are always last in the deck (also sorted
        // based on suit).
        finalDeck += acesInDeck
        
        // Print off final result.
        print(finalDeck.joined(separator: " "))
        
    } catch PHError.invalidInput {
        // Handle the error as per etude specifications.
        print("Invalid:", input)
    } // end do-catch block.
    
} // end while loop.
