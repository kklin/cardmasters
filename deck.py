import random
import itertools

# The orientation of the deck can be confusing. I've defined the first element
# of the list to be the top card if the face of the cards were facing the floor
# TODO: define another class to represent cards

class Deck(object):
    def __init__(self, n):
        suits = ['Clubs', 'Hearts', 'Spades', 'Diamonds']
        values = map(str, list(range(2,10))) + ['Jack', 'Queen', 'King', 'Ace']
        deck = list(itertools.product(values, suits))
        self.cards_lh = random.sample(deck, n)
        self.cards_rh = []

    @staticmethod
    def empty_deck():
        return Deck(0)

    def add_card(self, card, left_hand=True):
        if left_hand:
            self.cards_lh.append(card)
        else:
            self.cards_rh.append(card)


    def __str__(self):
        ret = "Left Hand:\n"
        for card in self.cards_lh:
            ret += card[0] + " of " + card[1] + "\n"
        ret += "Right Hand:\n"
        for card in self.cards_rh:
            ret += card[0] + " of " + card[1] + "\n"
        return ret

    def left_to_right(self, left, right):
        to_move = self.cards_lh[left]
        self.cards_lh = self.cards_lh[:left] + self.cards_lh[left+1:]
        self.cards_rh = self.cards_rh[:right] + [to_move] + self.cards_rh[right:]

    def right_to_left(self, right, left):
        to_move = self.cards_rh[right]
        self.cards_rh = self.cards_rh[:right] + self.cards_rh[right+1:]
        self.cards_lh = self.cards_rh[:left] + [to_move] + self.cards_lh[left:]

    def hand_equals(self, other, left_hand):
        if left_hand:
            return self.cards_lh == other.cards_lh
        return self.cards_rh == other.cards_rh

    def equals(self, other):
        return hand_equals(other, 'LEFT') and hand_equals(other, 'RIGHT')
