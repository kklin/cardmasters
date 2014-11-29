# these flourishes assumes deck[0] is the top of the deck and deck[-1] is the bottom
# each flourish returns a tuple (left, right), representing the deck remaining
# in the left hand, and the deck remaining in the right hand

# the print statements should be encapsulated in objects

from abc import ABCMeta, abstractmethod

class Flourish(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def apply(deck):
        pass

class HotShot(Flourish):
    @staticmethod
    def apply(deck):
        deck.left_to_right(-1, 0)

    def __str__():
        return "HotShot"

class TopShot(Flourish):
    @staticmethod
    def apply(deck):
        deck.left_to_right(0, 0)

    def __str__():
        return "TopShot"
