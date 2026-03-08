"""
Tanishq Sharda
Fall 2024

This program allows the user to enter a games room where they are prompted
with the option to play a series of three games against the computer or quit,
where they can gain or lose points. After each game their points are accumulated,
and when they exit they are presented with their total score.
"""

import random


def print_signature():
    print("Tanishq Sharda")
    return 0


def games_room(name):
    """
    Main function for the Games Room. Accepts user's name and selection of game.

    Args:
        name (str): Player's name

    Returns:
        int: total points scored
    """
    print(f"Hi, {name}, welcome to the Games Room!")
    points = 0

    while True:
        print(f"\nYour current score is {points}")
        print("You may pick a game you would like to play from the menu:")
        print("1) Number Guess")
        print("2) Modified Rock Paper Scissors Lizard Spock")
        print("3) Coin Flip")
        print("4) Quit")

        player_choice = input("Enter a game number from the list: ")

        if player_choice == "1":
            guess = int(input("Guess a number between 2-12: "))
            points += play_number_guess(guess)

        elif player_choice == "2":
            move = input("Make your move: Rock, Paper, Scissors, Lizard, or Spock: ")
            points += play_mrpsls(move)

        elif player_choice == "3":
            points += play_coin()

        elif player_choice == "4":
            print("Thanks for playing the Games Room!")
            return points

        else:
            docked_points = random.randint(1, 8)
            points -= docked_points
            print(f"Invalid choice! You were docked {docked_points} points.")

    return points


def play_number_guess(guess):
    """
    Number Guess game function. Allows the player to guess a number
    (possible dice sum) between 2 and 12, compared to the actual sum
    of the dice roll. Points are awarded according to the proximity
    of the guess and result.

    Args:
        guess (int): Player's guessed number

    Returns:
        int: The points achieved in this round
    """
    print(f"Guess: {guess}")
    points = 0

    while guess < 2 or guess > 12:
        print("Please try again by entering a number within the given range.")
        guess = int(input("Guess a number between 2-12: "))

    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_sum = dice_1 + dice_2

    print("Sum of roll:", dice_sum)

    # Correct scoring order: exact first, then within 2, then within 4
    if dice_sum == guess:
        points = 10
    elif dice_sum - 2 <= guess <= dice_sum + 2:
        points = 5
    elif dice_sum - 4 <= guess <= dice_sum + 4:
        points = 1
    else:
        points = 0

    print(f"Game: Number Guess\nDice Sum: {dice_sum}\nYour Guess: {guess}\nPoints Received: {points}")
    return points


def play_mrpsls(move):
    """
    Game of Modified Rock Paper Scissors Lizard Spock.
    Allows player to select a move, generates a random computer move,
    and allocates points based on the scoring rules.

    Args:
        move (str): Player's move selection

    Returns:
        int: Points achieved in the round
    """
    points = 0

    while True:
        if move == "Rock" or move == "Paper" or move == "Scissors" or move == "Lizard" or move == "Spock":
            print(f"Your move: {move}")
            break
        else:
            print("Please try again, making a move from Rock, Paper, Scissors, Lizard, or Spock.")
            move = input("Make your move: Rock, Paper, Scissors, Lizard, or Spock: ")

    computer_play = random.randint(1, 5)

    if computer_play == 1:
        computer_move = "Rock"
    elif computer_play == 2:
        computer_move = "Paper"
    elif computer_play == 3:
        computer_move = "Scissors"
    elif computer_play == 4:
        computer_move = "Lizard"
    else:
        computer_move = "Spock"

    print("Computer's Move:", computer_move)

    if move == "Rock":
        if computer_move == "Rock":
            points = 5
        elif computer_move == "Scissors" or computer_move == "Spock":
            points = 10
        else:
            points = 0

    elif move == "Paper":
        if computer_move == "Rock" or computer_move == "Lizard":
            points = 10
        elif computer_move == "Paper":
            points = 5
        else:
            points = 0

    elif move == "Scissors":
        if computer_move == "Scissors":
            points = 5
        elif computer_move == "Paper" or computer_move == "Spock":
            points = 10
        else:
            points = 0

    elif move == "Spock":
        if computer_move == "Paper" or computer_move == "Lizard":
            points = 10
        elif computer_move == "Spock":
            points = 5
        else:
            points = 0

    elif move == "Lizard":
        if computer_move == "Rock" or computer_move == "Scissors":
            points = 10
        elif computer_move == "Lizard":
            points = 5
        else:
            points = 0

    print(f"Game: Modified Rock Paper Scissors Lizard Spock\nYour Move: {move}\nComputer's Move: {computer_move}\nPoints Received: {points}")
    return points


def play_coin():
    """
    Plays the Coin Flip game with the user. The computer randomly simulates
    repeating coin flips. Points are awarded based on the sequence of coin flips.

    Returns:
        int: Points achieved from the flip sequence
    """
    statement = ""
    number_tries = 0
    points = 0

    flip_coin = random.randint(0, 1)

    if flip_coin == 0:
        print("First Flip: Heads")
        statement += f"Try {number_tries}: Heads, "
        number_tries += 1
    else:
        print("First Flip: Tails")
        statement += f"Try {number_tries}: Tails, "
        number_tries += 1

    if flip_coin == 1:
        # First flip is tails: 2 points for each head until next tails
        while True:
            flip_coin_2 = random.randint(0, 1)

            if flip_coin_2 == 0:
                points += 2
                statement += f"Try {number_tries}: Heads, "
                number_tries += 1
            else:
                statement += f"Try {number_tries}: Tails"
                number_tries += 1
                break

    else:
        # First flip is heads: 1 point for each tail until 2 more heads appear
        heads_flipped = 0

        while heads_flipped < 2:
            flip_coin_2 = random.randint(0, 1)

            if flip_coin_2 == 1:
                statement += f"Try {number_tries}: Tails, "
                number_tries += 1
                points += 1
                print("Flip Result: Tails")
            else:
                heads_flipped += 1
                statement += f"Try {number_tries}: Heads, "
                number_tries += 1
                print("Flip Result: Heads")

    print(f"Game: Coin Flip\nFlip Results: {statement}\nPoints: {points}")
    return points


def main():
    print_signature()
    name = input("Please enter your name: ")
    points_total = games_room(name)
    print(f"Final score: {points_total}")


if __name__ == "__main__":
    main()
