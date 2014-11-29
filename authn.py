import sys
import random
from deck import Deck

import flourishes

def get_random_deck(n=52):
    return Deck(n)

# destructively modifies deck
def apply_flourishes(deck, flourish_seq):
    for flourish in flourish_seq:
        flourish.apply(deck)

def main(n, flourish_seq, left_hand=True):
    auth_deck = get_random_deck(n)
    print("Please arrange your deck in the following order:")
    print(auth_deck)
    apply_flourishes(auth_deck, flourish_seq)
    # print("Deck is now in this state: ")
    # print(auth_deck)

    user_result = Deck.empty_deck()
    result_hand = 'LEFT' if left_hand else 'RIGHT'
    print("Enter the final deck configuration in your " + result_hand + " hand line by line")
    print("Separate the value and suit by a space (e.g. 10 Diamonds)")
    print("The cards should be entered from the top of the deck to the bottom")
    print("Type a period when finished")
    while True:
        inp = raw_input("Card: ")
        if inp is '.':
            break
        user_result.add_card(tuple(inp.split(" ")), False) # TODO: we should determine at runtime which hand to add it to

    if user_result.hand_equals(auth_deck, left_hand):
        print("You really are a cardist!")
    else:
        print("Ehh.. maybe you should keep practicing")
    # print("Expecting the deck to be: " + str(auth_deck))
    # print("And got: " + str(user_result))


if __name__ == '__main__':
    deck_size = int(sys.argv[1])
    flourish_seq = [flourishes.HotShot, flourishes.TopShot]
    main(deck_size, flourish_seq, False)
