# wordp13_game_engine
A Python implementation of the core logic for a Wordle-style word puzzle game.

This project was developed as part of the ENG 1P13 course at McMaster University and focuses on implementing the backend mechanics of a word guessing game using Python.

## Description

WordP13 is a text-based puzzle game where a player attempts to guess a hidden word.  
After each guess, the program evaluates the result and returns feedback symbols:

- `*` — correct letter in the correct position  
- `?` — correct letter but in the wrong position  
- `_` — letter not present in the target word  

The program loads word lists from text files, selects a random target word, and validates player guesses.

## Features

- Load word lists from external text files
- Randomly choose target words
- Validate guesses against a legal word list
- Word scoring algorithm similar to Wordle
- Letter tracking using Boolean arrays
- Modular function-based design

## Repository Structure

```
wordp13-game-engine/
│
├── wordp13.py
├── targets.txt
├── legal.txt
└── README.md
```

## Technologies Used

- Python
- File input/output
- String processing
- Algorithm design
- Boolean arrays
- Random number generation

## How to Run

Run the program with:
```
python wordp13.py
```
Make sure the files `targets.txt` and `legal.txt` are located in the same folder as the Python file.

## Author
Tanishq Sharda  
Engineering Physics Student  
McMaster University
