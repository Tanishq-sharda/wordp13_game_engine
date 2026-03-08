
"""
Tanishq Sharda
Fall 2024

This program contains four functions that implement the core logic
for a game of WordP13, similar to the game Wordle.
"""

import random


def print_signature():
    """
    Prints signature 
    """
    print("Tanishq Sharda")
    print("Fall 2024")


def load_words(filename):
    """
    Reads a file containing words and returns a list of valid words.

    Args:
        filename (str): Name of the file containing words, one per line.

    Returns:
        list: A list of words if all words are valid.
        bool: False if the file is empty or contains invalid words.
    """
    try:
        with open(filename, "r") as file:
            words = [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return False

    if not words:
        return False

    word_length = len(words[0])

    for word in words:
        if len(word) != word_length or not word.isalpha():
            return False

    return words


def choose_word(word_list):
    """
    Selects a random index from a given list of words.

    Args:
        word_list (list): List of words to choose from.

    Returns:
        int: Randomly selected index from the list.
        bool: False if the list is empty.
    """
    if len(word_list) == 0:
        return False

    return random.randint(0, len(word_list) - 1)


def update_letters(letters, target, guess):
    """
    Updates a Boolean list containing the status of each letter
    in the alphabet based on the user's guess and target word.

    Args:
        letters (list): A list of Booleans representing letters A-Z.
        target (str): The target word.
        guess (str): The guessed word.

    Returns:
        list: The updated letters list.
    """
    target = target.lower()
    guess = guess.lower()

    for letter in guess:
        if letter not in target:
            index = ord(letter) - ord("a")
            letters[index] = False

    return letters


def score_guess(guess, target, words):
    """
    Compares a user's guess to the target word and returns an evaluation string.

    '*' = correct letter in the correct place
    '?' = correct letter in the wrong place
    '_' = incorrect letter

    Args:
        guess (str): User's guess.
        target (str): Target word.
        words (list): List of legal words.

    Returns:
        str: A string showing the result of the comparison.
        bool: False if the guess is invalid.
    """
    guess = guess.lower()
    target = target.lower()
    words_lower = [word.lower() for word in words]

    if guess not in words_lower or len(guess) != len(target):
        return False

    result = []

    for i in range(len(guess)):
        if guess[i] == target[i]:
            result.append("*")
        else:
            result.append("_")

    for i in range(len(guess)):
        if result[i] == "_":
            if guess[i] in target and guess[i] != target[i]:
                result[i] = "?"

    return "".join(result)


def main():
    """
    Main program for testing signature output.
    """
    print_signature()


if __name__ == "__main__":
    main()