//
//  main.swift
//  PokerHands
//
//  Created by Max Huang on 21/08/18.
//  Copyright © 2018 Max Huang. All rights reserved.
//
//  Version 1.1

import Foundation

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
    
    // Assume input is valid. Changed to `false` when invalid input is detected.
    var validInput: Bool = true
    
    // Converts all input to lowercase for ease of String handling.
    let line = input.lowercased()
    
    if line.contains(" ") && !line.contains("/") && !line.contains("-") {
        // Separate based on whitespace.
        inputCards = line.split(separator: " ").map({String($0)})
    } else if line.contains("/") && !line.contains("-") && !line.contains(" ") {
        // Separate based on forward slash.
        inputCards = line.split(separator: "/").map({String($0)})
    } else if line.contains("-") && !line.contains("/") && !line.contains(" ") {
        // Separate based on dash.
        inputCards = line.split(separator: "-").map({String($0)})
    } else {
        // Invalid separator(s) used.
        validInput = false
        print("Invalid:", input)
    }
    
    // Remove all duplicates from the deck.
    inputCards = inputCards.reduce(into: [String]()) {
        if !$0.contains($1) {
            $0.append($1)
        }
    }
    
    // If the input so far is valid, continue.
    if validInput {
        if inputCards.count != 5 {
            // If too many or not enough cards are given as input.
            print("Invalid:", input)
        } else {
            var deck = [Cards]()
            for eachCard in inputCards {
                // Check if the card has a valid suit, if not then treat as
                // invalid input.
                if !eachCard.contains("c") && !eachCard.contains("d") &&
                    !eachCard.contains("h") && !eachCard.contains("s") {
                    print("Invalid:", input)
                    break
                }
                
                let startIndex = eachCard.startIndex
                let endIndex = eachCard.index(of: eachCard.last!)
                var card = String( eachCard[startIndex..<endIndex!] )
                let suit = eachCard.last!
                
                // If the card 'number' is not an integer, then find the
                // corresponding integer representation of that card in the
                // dictionary.
                if Int(card) == nil {
                    card = cardStr[card] as! String
                }
                deck.append(Cards(card: Int(card)!, suit: String(suit)))
            }
            
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
            
        }
        
    }
}
