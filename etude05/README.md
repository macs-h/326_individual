# Étude 05 - Poker Hands

## Current Version: 2.1.1
### Changes
* Invalides a deck that has multiple whitespaces as separators between any two sets of cards.


## Installation Instructions
* Compilation: `swiftc main.swift`
* To run: `swift main.swift`


## Previous Versions
### Version 2.1
* Check that the deck consists of 5 cards before checking for duplicates. If there are duplicates, return as invalid.
* Ensures that the separators used only exist **between** the cards and not at the front or end of the deck, otherwise it is considered invalid.
* Refactored "PKError" to "PHError" - incorrect naming in version 2.0

### Version 2.0
* Introduced using an enum to declare a new custom error class `PKError` which holds `invalidInput` as a case. This is thrown whenever an invalid input is detected and handled at the end of the `do-catch` block. Printing to `stdout` as specified in the etude PDF.
* This new approach to error handling is cleaner than having `if`/`else` statements with `break`.
* Improved error checking using `guard` statements - much more idiomatic Swift.
* Checking for invalid characters for both card number and suit - throws an error if invalid.

### Version 1.1
* Checking for duplicate cards in the deck before processing. If duplicates are found, the deck is treated as invalid.

### Version 1.0
* `<empty line>` or `<newline>`
* Normal string (e.g. `hello`)
* Consistent separators on one line (i.e. `/` or `-` or `<space>`)
* A deck of cards too short or too long (i.e. a deck that is not exactly 5 cards)
* Uppercase and lowercase for both cards and suits
* Inconsistent uppercase and lowercase (for both cards and suits) in one line
* Invalid suits (or non-existent suits)
* Special characters (e.g. `)`)
* Testing that both letters (and corresponding numbers) give the same result (for special cards like `T`, `A`, `J`, `Q`, and `K`)
