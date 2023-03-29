# Class cards
from CardsConstant import *

class Cards:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit + ' and value is ' +str(self.value)


#two_of_hearts=Cards("Hearts","Two")
#print(two_of_hearts)