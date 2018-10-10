//
//  main.swift
//  Threes
//
//  Created by Max Huang on 10/10/18.
//  Copyright © 2018 Max Huang. All rights reserved.
//

import Foundation

/**
    Returns the factors of a number, excluding 1.
 
    - parameter n: The number to find the factors of.
    - returns: An integer array holding the factors of the number.
 */
func factors(of n: Int) -> [Int] {
    precondition(n > 0, "n must be positive")
    let sqrtn = Int(Double(n).squareRoot())
    if sqrtn == 1 {
        return [n]
    }
    var factors: [Int] = []
    factors.reserveCapacity(2 * sqrtn)
    for i in 2...sqrtn {
        if n % i == 0 {
            factors.append(i)
        }
    }
    if factors.count > 0 {
        var j = factors.count - 1
        if factors[j] * factors[j] == n {
            j -= 1
        }
        while j >= 0 {
            factors.append(n / factors[j])
            j -= 1
        }
    }
    return factors
}

/**
    Validates that x, y, and z do not share any factors.
 
    - parameter array: The array holding three values (x, y, and z).
    - returns: False if there are common factors, otherwise True.
 */
func checkFactors(array: [Int]) -> Bool {
    var dictOfFactors = [Int:Int]()
    
    for num in array {
        for factor in factors(of: num) {
            if dictOfFactors[factor] != nil {
                return false
            }
            dictOfFactors[factor] = factor
        }
    }
    
    return true
}


// Variables for finding sets.
var validSets = [[Int]]()
var count = 0

/**
    Calculates y, given x and z. If found 70 sets, prints out the sets.
 
    - parameters:
        - x: The x value.
        - y: The y value.
    - returns: True if found 70 sets, otherwise false.
 */
func getY(_ x: Int, _ z: Int) -> Bool {
    let y2 = 1 + pow(Double(z), 4.0) - pow(Double(x), 2.0)
    
    let tmp = sqrt(y2)
    if (Int(y2) > 0) && (tmp.truncatingRemainder(dividingBy: 1) == 0) {
        let y = Int(tmp)
        
        if (y > x){
            if checkFactors(array: [x, y, z]) {
                validSets.append([x, y, z])
                count += 1
                if count == 70 {
                    var index = 1
                    
                    // Print the set.
                    for row in validSets {
                        print("\(index) \(row[0]) \(row[1]) \(row[2])")
                        index += 1
                    }
                    return true
                }
            }
        }
    }
    return false
}

/**
    Finds the sets for increasing x.
 */
func setsForX() {
    validSets = [[Int]]()
    count = 0
    for x in 3...20000 {
        for z in 2..<x {
            if getY(x, z) {
                return
            }
        }
    }
}

/**
    Finds the sets for increasing z.
 */
func setsForZ() {
    validSets = [[Int]]()
    count = 0
    for z in 2...20000 {
        for x in z+1...z*z {
            if getY(x, z) {
                return
            }
        }
    }
}

setsForX()
print()
setsForZ()

exit(0)
