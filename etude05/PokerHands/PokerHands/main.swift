//
//  main.swift
//  PokerHands
//
//  Created by Max Huang on 21/08/18.
//  Copyright © 2018 Max Huang. All rights reserved.
//
//  Version 1.0

import Foundation

let cardStr: NSDictionary = [ "a" : "1",
                              "t" : "10",
                              "j" : "11",
                              "q" : "12",
                              "k" : "13" ]

struct Cards {
    var card: Int
    var suit: String
}

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

func prompt(_ prompt: String, strippingNewline: Bool = true) -> String? {
    print(prompt, terminator:"")
    return readLine(strippingNewline: strippingNewline)
}


while let input = prompt(""){
    
    var inputCards = [String]()
    var validInput: Bool = true
    
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
    
    if validInput {
        if inputCards.count != 5 {
            // If too many or not enough cards are given as input.
            print("Invalid:", input)
        } else {
            // Valid input and correct amount of cards given.
            // Do processing of cards.
            var deck = [Cards]()
            for eachCard in inputCards {
                if !eachCard.contains("c") && !eachCard.contains("d") &&
                    !eachCard.contains("h") && !eachCard.contains("s") {
                    print("Invalid:", input)
                    break
                }
                
                let startIndex = eachCard.startIndex
                let endIndex = eachCard.index(of: eachCard.last!)
                var card = String( eachCard[startIndex..<endIndex!] )
                let suit = eachCard.last!
                
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
            
            var finalArray = [String]()
            var aceArray = [String]()
            for card in deck {
                if card.card == 1 {
                    aceArray.append( (getCardString(card.card) + card.suit).uppercased())
                } else {
                    finalArray.append( (getCardString(card.card) + card.suit).uppercased())
                }
            }
            finalArray += aceArray
            
            // Print off final result.
            print(finalArray.joined(separator: " "))
            
        }
        
    }
}
