# Étude 05 - Poker Hands
## Current Version: 1.1
### Additional test case
* Checking for duplicate cards in the deck before processing. If duplicates are found, the deck is treated as invalid.

## Previous Versions
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
