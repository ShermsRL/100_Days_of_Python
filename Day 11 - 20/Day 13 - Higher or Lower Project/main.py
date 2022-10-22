#import art and game_data and random module and clear(do last)
import art
import game_data
import random
from replit import clear

data_1 = random.choice(game_data.data)
data_2 = random.choice(game_data.data)
if data_1 == data_2:
  data_2 = random.choice(game_data.data)
score = 0

#Have a function to print out the details of the dict and concatenate tgt
def char_details(random_data):
  """Return the neccessary char details and combine them together."""
  return (f"{random_data['name']} , {random_data['description']} , {random_data['country']}")

#function to compare the 2 dictionary followers
#For the sherman tmr, try returning 0 and 1 to compare the result
  """Function to compare the follower count and let user know if he is correct."""
def compare_follower(a_follower, b_follower, guess_input):
  if a_follower > b_follower and guess_input == 'A':
    return 1
  elif b_follower > a_follower and guess_input == 'B':
    return 1
  else:
    return 0

def game_start(char1, char2):
  """Function that print out the character details, take user input and check if user is correct."""
  print(f"Compare A: {char_details(data_1)}")
  print(art.vs)
  print(f"Against B: {char_details(data_2)}")
  guess = input("Who has more followers? Type 'A' or 'B': ").upper()
  result = compare_follower(data_1['follower_count'], data_2['follower_count'], guess)
  return result

#print title art
print (art.logo)

game_over = False
while game_over == False:
  if game_start(data_1, data_2) == 1:
    score += 1
    data_1 = data_2
    data_2 = random.choice(game_data.data)
    clear()
    print(f"Thats correct, your current score is {score}")
  else:
    clear()
    print(art.logo)
    print(f"Thats wrong, your final score is {score} ")
    game_over = True




