# these flourishes assumes deck[0] is the top of the deck and deck[-1] is the bottom
# each flourish returns a tuple (left, right), representing the deck remaining
# in the left hand, and the deck remaining in the right hand

# the print statements should be encapsulated in objects

from abc import ABCMeta, abstractmethod
import random


class Flourish(object):
    __metaclass__ = ABCMeta
    name_str = "Flourish Name"
    creator_str = "Some Person"
    source_lst = ["Book1", "Book2", "DVD1"]

    @abstractmethod
    def apply(deck):
        pass

    def __str__():
        string = ""
        string += name_str
        if creator_str != "Unknown":
            string += " by " + creator_str
        return string

# ___________FALSE____________ 

class Mol2(Flourish):
    
    @staticmethod
    def apply(deck):
        pass

    name_str = "Molecule 2"
    creator_str = "Dan and Dave Buck"
    source_lst = ["The System (DVD)"]

class Tornado(Mol2):
    
    name_str = "Tornado Cut"
    creator_str = "Ashford Kneitel"
    source_lst = ["Tornado Cut (DVD)", "Hit the Road (DVD)"]

# ___________TOP-RETENTION____________ 

class Mol3(Mol2):
    
    name_str = "Molecule 3"
    creator_str = "Dan and Dave Buck"
    source_lst = ["The System (DVD)", "The Trilogy (DVD)"]


# ___________BOTTOM-RETENTION____________ 


# ___________TOP-BOTTOM CONNECTING____________ 

class Charlier(Flourish):
    @staticmethod
    def apply(deck, hand = 'LEFT'):
        pack = deck.get_hand(hand) 
        i = random.randint(0, len(pack) - 2)
        cut = deck.pop_pack(0, i, hand)
        deck.insert_pack(cut, -1, hand)

    name_str = "Charlier Cut"
    creator_str = "Unknown"
    source_lst = []

class Rev(Flourish):
    @staticmethod
    def apply(deck, hand = 'LEFT'):
        Charlier.apply(deck, hand)

    name_str = "Revolution Cut"
    creator_str = "Brian Tudor"
    source_lst = ["Generation Extreme (DVD)", "Showoff 1 (DVD)"]

# ___________AERIAL/HAND-TRAVELING____________ 

class HotShot(Flourish):
    @staticmethod
    def apply(deck):
        deck.left_to_right(-1, 0)
        hand = deck.get_hand('LEFT') 
        i = random.randint(0, len(hand) - 3)
        cut = deck.pop_pack(0, i)
        deck.insert_pack(cut, -1)

    name_str = "Hot Shot Cut"
    creator_str = "Daryl"
    source_lst = ["Daryl's Encyclopedia of Card Sleights Vol. 8 (DVD)"]

class TopShot(Flourish):
    @staticmethod
    def apply(deck):
        card = deck.get(0)
        card.flip_over()
        deck.left_to_right(0, 0)

    name_str = "Top Shot"
    creator_str = "Lennart Green"
    source_lst = ["Classic Green Collection Vol. 1 (DVD)"]

class InstantReplay(Flourish):
    @staticmethod
    def apply(deck):        
        cut = deck.pop_pack(0, -1, 'RIGHT')
        deck.insert_pack(cut, 0, 'LEFT')

    name_str = "Instant Replay"
    creator_str = "Paul Harris"
    source_lst = ["The Art of Astonishment Vol. 3 (Book)"]

# ___________TURNOVER____________ 

class DBD(Flourish):
    @staticmethod
    def apply(deck):        
        deck.turnover(0, 1)
    
    name_str = "Diving Board Double"
    creator_str = "Lee Asher"
    source_lst = ["Diving Board Double (PDF)"]

class Erdnase(Flourish):
    @staticmethod
    def apply(deck):        
        deck.reverse(0, 1)

    name_str = "Erdnase Color Change"
    creator_str = "S.W. Erdnase"
    source_lst = ["The Expert at the Card Table (Book)"]


class Ego(Flourish):
    @staticmethod
    def apply(deck):        
        deck.reverse(0, 0)
        deck.move(0, -1)

    name_str = "Ego Change"
    creator_str = "Daniel Garcia"
    source_lst = ["Daniel Garcia Projects Vol. 1 (DVD)"]

# ___________OTHER____________ 
