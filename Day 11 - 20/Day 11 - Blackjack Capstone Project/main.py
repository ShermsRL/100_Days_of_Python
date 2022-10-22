import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []

#Start a game
def start_game():
    start = input(
        "Do you want to play a game of blackjack? Type 'y' to continue and 'n' to stop: "
    ).lower()
    if start == 'y':
        clear()
        print(logo)

        #Player and computer starting hand
        draw_card(player_cards)
        print(f"Your cards: {player_cards}")
        draw_card(computer_cards)
        print(f"Computer first card: {computer_cards[0]}")

        if sum_of_user(player_cards) == 21 and len(player_cards) == 2: #First turn blackjack
          print("Blackjack! You Win!")
          start_game()
        else:
        # If player first turn blackjack, no need to check if want to draw card
          while input("Type 'y' to get another card, type 'n' to pass: ").lower(
          ) == 'y':
              draw_card(player_cards)
              sum_of_user(player_cards)
              print(f"Your cards: {player_cards}")

        while sum_of_user(computer_cards) <= 17:
            draw_card(computer_cards)

        
        compare_winner(player_cards, computer_cards)
        

    else:
        print("Come again next time!")


########################################################################################################
# Functions


def draw_card(deck):
    """Add a card to the selected deck"""
    if len(deck) == 0:
      deck.append(random.choices(cards, k=2))
    else:
      deck.append(random.choice(cards))


def sum_of_user(deck):
    """Calculate the total points of the player"""
    #edit to sum function
    sum = 0
    for cards in range(0, len(deck)):
        sum += deck[cards]
    return sum


def compare_winner(player, computer):
    #Try to optimize blackjack comparison code
    """Compare whether the player or AI wins"""
    if sum_of_user(player) > 21:
        print("You lose")
    elif sum_of_user(computer) == 21 and len(computer) == 2:
        print("Computer Blackjack, you lose.")
    elif sum_of_user(computer) > sum_of_user(player) and sum_of_user(
            computer) <= 21:
        print("You lose")
    elif sum_of_user(computer) == sum_of_user(player):
        print("Draw")
    elif sum_of_user(computer) < sum_of_user(player) or sum_of_user(
            computer) >= 22:
        print("You Win")

    print(f"Computer final cards: {computer}")
    print (sum_of_user(player))
    start_game()


start_game()
