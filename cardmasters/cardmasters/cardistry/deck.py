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
        v1, v2 = self.val, other.val
        s1, s2 = self.suit, other.suit
        face = ['Jack', 'Queen', 'King', 'Ace']
        for f in face:
            if self.val == f:
                v1 = 11 + face.index(f)
            if other.val == f:
                v2 = 11 + face.index(f)
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        for s in suits:
            if s1 == s:
                s1 = suits.index(s)
            if s2 == s:
                s2 = suits.index(s)
        _cmp = int(v1) - int(v2)
        if _cmp == 0:
            if s1 - s2 == 0:
                if not (self.faceup is other.faceup):
                    return 1
            return s1 - s2
        return _cmp

    def same_val(self, other):
        return self.val == other.val

    def flip_over(self):
        self.faceup = not self.faceup


# The orientation of the deck can be confusing. I've defined the first element
# of the list to be the top card if the face of the cards were facing the floor
# TODO: define another class to represent cards

class Deck(object):
    def __init__(self, n = 52, copy = None):
        if copy:
            self.cards_lh = list(copy.cards_lh)
            self.cards_rh = list(copy.cards_rh)
        else:
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
        ret += "\nRight Hand:\n"
        for card in self.cards_rh:
            ret += str(card) + "\n"
        return ret

    def hand_equals(self, other, left_hand):
        if left_hand == 'LEFT':
            return self.cards_lh == other.cards_lh
        return self.cards_rh == other.cards_rh

    def equals(self, other):
        return self.hand_equals(other, 'LEFT') and self.hand_equals(other, 'RIGHT')

    def size(self):
        return len(self.get_hand('LEFT')) + len(self.get_hand('RIGHT'))

    def copy(self):
        return Deck(copy = self)

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

    # Moves card at index LEFT from left hand to index RIGHT in right hand
    def left_to_right(self, left, right):
        to_move = self.cards_lh.pop(left)
        self.cards_rh.insert(right, to_move)

    # Moves card at index RIGHT from right hand to index LEFT in left hand
    def right_to_left(self, right, left):
        to_move = self.cards_rh.pop(right)
        self.cards_lh.insert(left, to_move)


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

    def insert_pack(self, pack, i, hand = 'LEFT'):
        pack.reverse()
        deck = self.get_hand(hand)
        if i < 0:
            i = len(deck) + i + 1
        for card in pack:
            deck.insert(i, card)

    def reverse(self, i1, i2, hand = 'LEFT'):
        deck = self.pop_pack(i1, i2, hand)
        self.insert_pack(deck, i1, hand)

    # Turns over cards I1 to I2 in HAND
    def turnover(self, i1, i2, hand = 'LEFT'):
        self.reverse(i1, i2, hand)
        deck = self.get_pack(i1, i2, hand)
        for card in deck:
            card.flip_over()

    # This is destructive!!
    def execute_flourishes(self, flourishes):
        for flourish in flourishes:
            flourish.apply(self)
