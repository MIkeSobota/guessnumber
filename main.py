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

is_game_over = False
#starts the game
while not is_game_over:

    answer = randint(1,100)

    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    
    #ask user to choose difficulty
    choose_difficulty = False
    while choose_difficulty is False: 
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == "easy":
            attempts = 10
            print(f"You have 10 attempts to guess the number.")
            choose_difficulty = True
        elif difficulty == "hard":
            attempts = 5
            print(f"You have 5 attempts to guess the number.")
            choose_difficulty = True
        elif difficulty != "easy" or difficulty != "hard":
            print("Sorry, Try again.")

        
        print(f"The answer is : {answer}")

        #Check the amount of guesses untill out of guesses
        out_of_guess = False
        user_guess = []
        while not out_of_guess:
            make_guess = int(input("Make a guess: "))
            user_guess.append(make_guess)
            print(user_guess)

            #check user guess to see if it matches the generated number
            if make_guess == answer:
                print("You guessed correct!")
                is_game_over = True
                out_of_guess = True
            elif make_guess > answer:
                print("too high!")
            elif make_guess < answer:
                print("Too low")

                #check the difficulty and remaining guess attempts
                if difficulty == "easy" and attempts <= 1 or difficulty == "hard" and attempts <=1:
                    print("Sorry out of guesses!")
                    out_of_guess = True
                    is_game_over = True
                else:
                    attempts -= 1
                    print(
                        f"You have {attempts} remaining attempts to guess the number.")

        #Ask user to play again
        play_again = input(
            "Do you want to play again? Type 'y' for yes or 'n' for no: ")
        if play_again == "y" or play_again == "yes":
            is_game_over = False
        else:
            is_game_over = True
