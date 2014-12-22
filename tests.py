import unittest, flourishes, deck

class flourishTests(unittest.TestCase):

    def setUp(self):
        n = 10
        self.deck = deck.Deck(n)
        self.osize = n

    def tearDown(self):
        self.assertTrue(self.osize == self.deck.size())

    def test_hotshot(self):
        bottom = self.deck.get(self.osize - 1)
        top = self.deck.get(0)
        secondbottom = self.deck.get(self.osize - 2)
        flourishes.HotShot.apply(self.deck)

        # Tests that BOTTOM travelled to right hand
        self.assertTrue(self.deck.get(0, 'RIGHT') == bottom)
        
        # Tests that original TOP card is under SECONDBOTTOM in lefthand
        hand = self.deck.get_hand('LEFT')
        i = hand.index(secondbottom)
        self.assertTrue(top == self.deck.get(i + 1))

    def test_topshot(self):
        top = self.deck.get(0)
        flourishes.TopShot.apply(self.deck)
        self.assertTrue(self.deck.get(0, 'RIGHT') == top)
        self.assertTrue(self.deck.get(0, 'RIGHT').faceup)

    def test_ir(self):
        orig = self.deck.copy()
        pack = self.deck.pop_pack(0, 3)
        self.deck.insert_pack(pack, 0, 'RIGHT')
        print(self.deck)
        self.assertTrue(not orig.equals(self.deck))
        flourishes.InstantReplay.apply(self.deck)
        print(self.deck)
        self.assertTrue(orig.equals(self.deck))


if __name__ == '__main__':
    unittest.main()
