#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from random import randint
from art import logo

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS

def check_answer(user_guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if user_guess > 100 or user_guess < 1:
        print("Invalid input. Please guess between 1 and 100.")
        return turns
    elif user_guess > answer:
        print("Too high!")
        return turns -1
    elif user_guess < answer:
        print("Too low.")
        return turns -1
    else:
        print(f"You guessed correct! The answer was {answer}")
        play_again()

def play_again():
    go_again = input("Do you want to play again? Type 'y' for yes. 'n' for no. ")
    if go_again == "y" or go_again == "yes":
        game()
    else:
        return

def game():

    print(logo)
    print()
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)
    #print(answer)

    #set default turn based on difficulty selected
    turns = set_difficulty()

    user_guess = 0
    while user_guess != answer:
        print(f"You have {turns} attempts to guess the answer.")
        user_guess = int(input("Make a guess: "))
        turns = check_answer(user_guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. You lose")
            play_again()
            return
        elif user_guess != answer:
            print("Guess again.")


game()
