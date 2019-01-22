import collections

#构建一个简单的类表示纸牌
Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck():
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]


    def __len__(self):
        return len(self._cards)


    def __getitem__(self,position):
        return self._cards[position]

    def __contains__(self,card):
        return card in self._cards


beer_card = Card('7','diamonds')
print(beer_card) # Card(rank='7', suit='diamonds')

deck = FrenchDeck()
print(len(deck)) # 52

print(deck[0]) # Card(rank='2', suit='spades') 调用__getitem__方法

#因为实现了__getitem__方法，这一摞纸牌变为可迭代的了
for card in deck:
    print(card)


print(beer_card in deck) #True,调用__contains__方法

# 对纸牌进行排序
suit_values = dict(spades = 3,hearts = 2,diamonds = 1,clubs = 0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck,key = spades_high):
    print(card)




