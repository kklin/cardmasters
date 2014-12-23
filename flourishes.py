# these flourishes assumes deck[0] is the top of the deck and deck[-1] is the bottom
# each flourish returns a tuple (left, right), representing the deck remaining
# in the left hand, and the deck remaining in the right hand

# the print statements should be encapsulated in objects

from abc import ABCMeta, abstractmethod
import random

class Flourish(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def apply(deck):
        pass

class Charlier(Flourish):
    @staticmethod
    def apply(deck, hand = 'LEFT'):
        pack = deck.get_hand(hand) 
        i = random.randint(0, len(pack) - 2)
        cut = deck.pop_pack(0, i, hand)
        deck.insert_pack(cut, -1, hand)

    def __str__():
        return "Charlier Cut"

class Rev(Flourish):
    @staticmethod
    def apply(deck, hand = 'LEFT'):
        Charlier.apply(deck, hand)

    def __str__():
        return "Revolution Cut by Brian Tudor"

class HotShot(Flourish):
    @staticmethod
    def apply(deck):
        deck.left_to_right(-1, 0)
        hand = deck.get_hand('LEFT') 
        i = random.randint(0, len(hand) - 3)
        cut = deck.pop_pack(0, i)
        deck.insert_pack(cut, -1)

    def __str__():
        return "Hot Shot Cut by Daryl"

class TopShot(Flourish):
    @staticmethod
    def apply(deck):
        card = deck.get(0)
        card.flip_over()
        deck.left_to_right(0, 0)


    def __str__():
        return "Top Shot by Lennart Green"

class InstantReplay(Flourish):
    @staticmethod
    def apply(deck):        
        cut = deck.pop_pack(0, -1, 'RIGHT')
        deck.insert_pack(cut, 0, 'LEFT')

    def __str__():
        return "Instant Replay by Paul Harris (Right to Left)"

class DBD(Flourish):
    @staticmethod
    def apply(deck):        
        deck.turnover(0, 1)

    def __str__():
        return "Divingboard Double by Lee Asher"

class Erdnase(Flourish):
    @staticmethod
    def apply(deck):        
        deck.reverse(0, 1)

    def __str__():
        return "Erdnase Color Change by S.W. Erdnase"

class Ego(Flourish):
    @staticmethod
    def apply(deck):        
        deck.reverse(0, 0)
        deck.move(0, -1)

    def __str__():
        return "Ego Change by Daniel Garcia"