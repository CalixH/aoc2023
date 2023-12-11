import sys
from decimal import Decimal

cardorder = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

class Main:

    def __init__(self, string):
        self.string = string

    def __lt__(self, other):
        uniq1 = list(set([c for c in self.string]))
        uniq2 = list(set([c for c in other.string]))
        if len(uniq1) < len(uniq2):
            return False
        if len(uniq1) > len(uniq2):
            return True
        if len(uniq1) == 2:
            c0, c1 = uniq1
            d0, d1 = uniq2
            selfmax = max(self.string.count(c0), self.string.count(c1))
            othermax = max(other.string.count(d0), other.string.count(d1))
            if selfmax > othermax:
                return False
            if othermax > selfmax:
                return True
            comp = zip(self.string, other.string)
            for i in comp:
                if cardorder.index(i[0]) > cardorder.index(i[1]):
                    return True
                if cardorder.index(i[0]) < cardorder.index(i[1]):
                    return False
        if len(uniq1) == 3:
            c0, c1, c2 = uniq1
            d0, d1, d2 = uniq2
            selfmax = max(self.string.count(c0), self.string.count(c1), self.string.count(c2))
            othermax = max(other.string.count(d0), other.string.count(d1), self.string.count(d2))
            if selfmax > othermax:
                return False
            if othermax > selfmax:
                return True
            comp = zip(self.string, other.string)
            for i in comp:
                if cardorder.index(i[0]) > cardorder.index(i[1]):
                    return True
                if cardorder.index(i[0]) < cardorder.index(i[1]):
                    return False
        comp = zip(self.string, other.string)
        for i in comp:
            if cardorder.index(i[0]) > cardorder.index(i[1]):
                return True
            if cardorder.index(i[0]) < cardorder.index(i[1]):
                return False

            

input = sys.stdin.readlines()
cards = []
bids = []
finalcards = []
finalbids = []
for i in input:
    cards.append(i.strip().split(" ")[0])
    bids.append(i.strip().split(" ")[1])
while len(cards) > 0:
    mincard = Main(cards[0])
    for i in cards:
        j = Main(i)
        if j < mincard:
            mincard = j
    finalcards.append(mincard.string)
    finalbids.append(bids[cards.index(mincard.string)])
    bids.pop(cards.index(mincard.string))
    cards.remove(mincard.string)
sum = Decimal(0)
for i, c in enumerate(finalbids):
    sum += (i+1) * Decimal(c)
print(sum)
print(finalcards)
    
