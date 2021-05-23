"""Black Jack Assignment 5 - Code Written by Pradeep Patel
start date Tuesday, March 23, 2021 -- End date Monday, April 05, 2021
From April 05, 2021 onwards worked on Bonus/Extra leg of the assignment completed on April 09, 2021
"""

#Blackjack / Twenty-one

#The possible card values range from 1 to 10 and unlike a real
#deck, the probably of drawing a card is equal

#The game begins by dealing two visible cards to the player, and two cards to the dealer.
#However, in the case of the dealer, one card is visible to other player while the other is hidden.

#The player decides whether to "hit" (draw another card), or "stand" which ends their turn.
#The player may hit any number of times. Should the total of the cards exceed 21, the player
#"busts" and loses the game to the dealer. If the player reaches 21, the player stands
#The dealer's turn begins by revealing the hidden card. The dealer must continue to hit if the
#total is 16 or less, and must stand if the value is 17 or more The dealer busts if their total is
#over 21 and the player wins. The dealer wins all ties (i.e. if both the dealer and the player reach
#21, the dealer wins). The program indicates who the winner is and asks to play again. It is up to
#you as the developer on how you will choose to handle invalid user input, but note the program
#cannot crash upon invalid input. Options can involve asking the user again or exiting the program
#with a user-friendly message.

#Bonus / Extra
#Introduce face cards (king, queen, jack) to the card deck
#Introduce the Ace which can either take the value of 1 or 11. Let's say the user is dealt a 10
#and an ace, that would equal 21. If the user has 3, gets an ace, the total is 14. If the user hits
#and busts, then the ace is considered to have the value of 1.
#NOTE: No additional marks are awarded for completing Bonus/Extra. If you are still interested in
#implementing these bonus features, aim to complete the basic requirements of the assignment first
#before you begin to attempt the bonus material. Save a separate working copy of the basic features
#in case you do not manage to complete the additional features. Some students may underestimate the
#level of effort required for this. To ensure the highest grades, you can always submit the
#functioning basic version if you cannot finish the advanced features. Good luck!

#This assignment is inspired and modified from:
#https://programmingbydoing.com/a/project-blackjack.html

#The program code starts from below:
import random

def input_start(new_gam):
    """function to check, validate and accept starting a new game"""
    while True:
        try:
            new_gam = input("Do you wish to start a new game?"
                " Acceptable values are (y/n) only: ")
            if new_gam in ["Y", "y"]:
                return "Y"
            if new_gam in ["N", "n"]:
                return "N"
        except ValueError:
            continue

def pull_hand(card_deck):
    """function to pull a card from the deck and assign a card to player or dealer"""
    random.shuffle(card_deck)
    return card_deck.pop()

def hit_stan():
    """function to check, validate and accept hit or stand"""
    while True:
        try:
            hit_stnd = input("Do you wish to Hit(H) or Stand(S)?"
                " Acceptable values are (H/S) only: ")
            if hit_stnd in ["H", "h"]:
                return "H"
            if hit_stnd in ["S", "s"]:
                return "S"
        except ValueError:
            continue

def who_win(pla_cards, dea_cards):
    """function to check, validate and decide who has won"""
    result = ""
    if pla_cards > 21:
        result = "\nYou Busted!! Dealer Wins !!        "
    elif dea_cards > 21:
        result = "\nDealer Busts.. You Win !!          "
    elif pla_cards > dea_cards:
        result = "\nHurray.. You Win !!                "
    elif pla_cards < dea_cards:
        result = "\nDealer Wins...                     "
    elif pla_cards == dea_cards:
        result = "\nYou have tied.. The Dealer Wins...!"
    return result

def face_crd_chk(crds, sum_crds):
    """function to check if the pulled card is a face card and then assign/add value accordingly"""
    if crds[-1] not in ['Jack', 'Queen', 'King', 'Ace']:
        sum_crds += crds[-1]
    if crds[-1] in ['Jack', 'Queen', 'King']:
        sum_crds += 10
    if crds[-1] == 'Ace':
        if sum_crds < 11:
            sum_crds += 11
        else:
            sum_crds += 1
    return sum_crds

def black_jack():
    """defining function for the actual game black jack.."""
    print("\nWelcome to Blackjack.")
    while True:

        print(f'{"-":-^80}\n')

        new_game = ""
        new_game = input_start(new_game)
        if new_game == "N":
            print("\nThanks for playing Blackjack - Bye..!!")
            break

        card_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']*4

        pl_crds = []
        sum_pl_crds = 0
        dl_crds = []
        sum_dl_crds = 0
        for _ in range(2):
            pl_crds.append(pull_hand(card_deck))
            sum_pl_crds = face_crd_chk(pl_crds, sum_pl_crds)
            dl_crds.append(pull_hand(card_deck))
            sum_dl_crds = face_crd_chk(dl_crds, sum_dl_crds)
        print(f"\nYou draw {pl_crds[0]} & {pl_crds[1]}. Your total is {sum_pl_crds}.")
        if sum_pl_crds > 21:
            print("\nYou Bust!! Dealer Wins !!! ")
            continue
        print(f"\nThe dealer draws a {dl_crds[0]} and a hidden card.\n")

        while sum_pl_crds < 21:
            hit_stand = hit_stan()
            if hit_stand == "H":
                pl_crds.append(pull_hand(card_deck))
                sum_pl_crds = face_crd_chk(pl_crds, sum_pl_crds)
                print(f"\nHit! You draw a {pl_crds[-1]}. Your total is {sum_pl_crds}.\n")
                if sum_pl_crds > 21:
                    print(f"Your total is {sum_pl_crds}")
                    print("\nYou Bust!! Dealer Wins !!! ")
                    break
            else:
                break
        if sum_pl_crds > 21:
            continue
        print(f"\nDealer's hidden card is {dl_crds[1]}, and has a total of {sum_dl_crds}.")
        if sum_dl_crds > 16:
            print(f"\nYour total is {sum_pl_crds} and Dealer's total is {sum_dl_crds}.")
            print(f"{who_win(sum_pl_crds, sum_dl_crds)}")
            continue
        while sum_dl_crds <= 16:
            dl_crds.append(pull_hand(card_deck))
            sum_dl_crds = face_crd_chk(dl_crds, sum_dl_crds)
            input("\nPress Enter to continue...")
            print(f"\nHit! Dealer draws {dl_crds[-1]} now dealer's total is {sum_dl_crds}.")
            if sum_dl_crds > 21 or sum_dl_crds > 16:
                print(f"\nYour total is {sum_pl_crds} and Dealer's total is {sum_dl_crds}.")
                print(f"{who_win(sum_pl_crds, sum_dl_crds)}")
            continue

def main():
    """calling the game under main function to remove the upper case naming pylint errors"""
    black_jack()

if __name__ == '__main__':
    main()
