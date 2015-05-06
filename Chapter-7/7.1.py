__author__ = 'Jithu Jim'

class Card(object):
    def __init__(self,rank,suit):
        self.suitList = ["Clubs","Diamonds","Hearts","Spades"]
        self.rankList = ["Ace","1","2","3","4","5","6","7","8","9","10","Jack","Queen","King","narf"]

        self.rank = rank
        self.suit = suit

    def get_suit(self):
        return self.suitList[self.suit]

    def get_rank(self):
        return self.rankList[self.rank]

    def __str__(self):
        return '( '+str(self.rankList[self.rank]) + ' of ' + str(self.suitList[self.suit])   + ' )'

class BlackJack(Card):
    def __init__(self,rank,suit):
        super(BlackJack,self).__init__(rank,suit)

    def int_value(self):
        r = super(BlackJack,self).get_rank()
        if (r == 1):
            return 11
        if (r < 10):
            return r
        return 10

    def is_ace(self):
        return super(BlackJack,self).get_rank() == "Ace"

b = BlackJack(0,1)
print(b.is_ace())
print(b.int_value())