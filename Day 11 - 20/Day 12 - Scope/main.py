#Number Guessing Game Objectives:

# Include an ASCII art logo. ✔️
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from replit import clear
import random

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

def start_game():
  print(logo)
  print("Welcome to Guess the number!")
  print("I am thinking of a number between 1 and 100")
  difficulty_level(input("Choose a difficulty. Type 'easy' or 'hard': ").lower(), random.choice(numbers))

def difficulty_level(difficulty, number):
  if difficulty == "easy":
    attempts = 10
  else:
    attempts = 5

  guess = ""
  while attempts != 0 and guess != number:
    guess = int(input(f"You have {attempts} remaining to guess the number.\n Guess the number."))
    attempts -= 1
    if guess > number:
      print("Too high")
    elif guess < number:
      print("Too low")
    else: 
      print("Correct")
      replay()
      

    if attempts == 0:
      print("You run out of attempts!")
      replay()

def replay():
  replay = input("Do you want to play again? Type 'y' to play again, 'n' to end: ").lower()
  if replay == 'y':
    clear()
    start_game()
  else:
    print("Come play next time!")
      

start_game()
