

import random
import os


def a_number():
    n = random.randint(1, 100)
    return n


def play_game():
    print("Welcome to number Guessing game")
    num = a_number()
    level = ["easy", "hard"]
    ask_level = input("Easy or hard: ")
    if ask_level.lower() == level[0]:
        i = 1
        while i <= 10:
            print(f" {i} chance")
            trial = int(input("Guess a number between 1 and 100:"))
            if num > trial:
                print("Too low")
                i += 1
            elif num < trial:
                print("Too high")
                i += 1
            else:
                print("You won")
                break
        else:
            print("you lose")
    elif ask_level.lower() == level[1]:
        i = 1
        while i <= 5:
            print(f" {i} chance.")
            trial = int(input("Guess a number between 1 and 100:"))
            if num > trial:
                print("Too low")
                i += 1
            elif num < trial:
                print("Too high")
                i += 1
            else:
                print("You won")
                break
        else:
            print("You lose")
    else:
        return 0


is_game_on = True
while is_game_on:
    if input("Do you want to play another game:y/n") == "y":
        play_game()
        os.system('cls')
    else:
        is_game_on = False




