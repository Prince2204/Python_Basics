from CardsConstant import *
from Cards import *
import random

class Deck:
    # Initialization method creates a deck of all cards
    def __init__(self):
        # This only happens once on creation of new Deck
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Cards(suit,rank))

    # This method shuffles the cards in Deck
    def shuffle(self):
        random.shuffle(self.deck)


    # this method to pick one card at a time
    def deal_one(self):
        return self.deck.pop()

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

'''
mydeck = Deck()
print(len(mydeck.all_cards))
print(mydeck.all_cards[0])
mydeck.shuffle()
print(mydeck.all_cards[0])

mycard=mydeck.deal_one()
print(mycard)
test_deck = Deck()
print(test_deck)
'''


