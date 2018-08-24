# Étude 05 - Poker Hands
## Current Version: 2.0
### Changes
* Introduced using an enum to declare a new custom error class `PKError` which holds `invalidInput` as a case. This is thrown whenever an invalid input is detected and handled at the end of the `do-catch` block. Printing to `stdout` as specified in the etude PDF.
* This new approach to error handling is cleaner than having `if`/`else` statements with `break`.
* Improved error checking using `guard` statements - much more idiomatic Swift.
* Checking for invalid characters for both card number and suit - throws an error if invalid.


## Previous Versions
### Cases tested for: (v1.1)
* Checking for duplicate cards in the deck before processing. If duplicates are found, the deck is treated as invalid.

### Cases tested for: (v1.0)
* `<empty line>` or `<newline>`
* Normal string (e.g. `hello`)
* Consistent separators on one line (i.e. `/` or `-` or `<space>`)
* A deck of cards too short or too long (i.e. a deck that is not exactly 5 cards)
* Uppercase and lowercase for both cards and suits
* Inconsistent uppercase and lowercase (for both cards and suits) in one line
* Invalid suits (or non-existent suits)
* Special characters (e.g. `)`)
* Testing that both letters (and corresponding numbers) give the same result (for special cards like `T`, `A`, `J`, `Q`, and `K`)


## Installation Instructions
* Compilation: `swiftc main.swift`
* To run: `swift main.swift`
