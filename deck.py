import random
import itertools

class Card(object):

    #VAL and SUIT must be string values
    def __init__(self, val, suit):
        self.val = val
        self.suit = suit
        self.faceup = False

    def __str__(self):
        return self.val + " of " + self.suit

    def __cmp__(self, other):
        #Cards must be the same card to be considered equal
        if self.val == other.val and self.suit == other.suit:
            return 0
        elif self.val > other.val:
            return 1
        elif self.val < other.val:
            return -1

    def same_val(self, other):
        return self.val == other.val

    def flip_over(self):
        self.faceup = not self.faceup


# The orientation of the deck can be confusing. I've defined the first element
# of the list to be the top card if the face of the cards were facing the floor
# TODO: define another class to represent cards

class Deck(object):
    def __init__(self, n):
        suits = ['Clubs', 'Hearts', 'Spades', 'Diamonds']
        values = map(str, list(range(2, 11))) + ['Jack', 'Queen', 'King', 'Ace']
        deck = list(itertools.product(values, suits))
        obj_deck = map(lambda x: Card(x[0], x[1]), deck)
        self.cards_lh = random.sample(obj_deck, n)
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
            ret += str(card) + "\n"
        ret += "Right Hand:\n"
        for card in self.cards_rh:
            ret += str(card) + "\n"
        return ret

    def get_hand(self, hand):
        if hand == 'LEFT':
            deck = self.cards_lh
        else:
            deck = self.cards_rh
        return deck

    def get(self, index, hand = 'LEFT'):
        return self.get_hand(hand)[index]

    #Moves card at index FRM to index TO within HAND
    def move(self, frm, to, hand = 'LEFT'):
        deck = self.get_hand(hand)
        if frm < 0:
            frm = len(deck) + frm
        if to < 0:
            to = len(deck) + to
        c = deck.pop(frm)
        deck.insert(to, c)

    # Returns a list containing cards index I1 to index I2 from HAND 
    def get_pack(self, i1, i2, hand = 'LEFT'):
        deck = self.get_hand(hand)
        if i1 < 0:
            i1 = len(deck) + i1
        if i2 < 0:
            i2 = len(deck) + i2
        return deck[i1 : i2 + 1]
    
    # Removes cards index I1 to index I2 from HAND and then returns them as a list in the same order
    def pop_pack(self, i1, i2, hand = 'LEFT'):
        pack = self.get_pack(i1, i2, hand)
        deck = self.get_hand(hand)
        for card in pack:
            deck.remove(card)
        return pack

    # Turns over cards I1 to I2 in HAND
    def turnover(self, i1, i2, hand = 'LEFT'):
        deck = self.pop_pack(i1, i2, hand)
        deck.reverse()
        if i1 < 0:
            i1 = len(deck) + i1
        k = i1
        for card in deck:
            card.flip_over()
            self.get_hand(hand).insert(k, card)
            k += 1

    # Moves card at index LEFT from left hand to index RIGHT in right hand
    def left_to_right(self, left, right):
        to_move = self.cards_lh.pop[left]
        self.cards_rh.insert(right, to_move)

    # Moves card at index RIGHT from right hand to index LEFT in left hand
    def right_to_left(self, right, left):
        to_move = self.cards_rh.pop[right]
        self.cards_lh.insert(left, to_move)

    def hand_equals(self, other, left_hand):
        if left_hand == 'LEFT':
            return self.cards_lh == other.cards_lh
        return self.cards_rh == other.cards_rh

    def equals(self, other):
        return hand_equals(other, 'LEFT') and hand_equals(other, 'RIGHT')
