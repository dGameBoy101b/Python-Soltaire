from solitaire.game.card import Card

class IllegalMove(Exception):
    '''attempted action breaks the rules of solitaire'''

class CardPile():
    '''an ordered pile of standard playing cards'''
    def __init__(self, *cards: tuple):
        for card in cards:
            if not isinstance(card, (tuple, Card)):
                raise TypeError('each item in CardPile() *cards argument must be a Card or tuple, not a '+str(type(card)))
        self.cards = []
        for card in cards:
            if isinstance(card, tuple):
                self.cards.append(Card(*card))
            else:
                self.cards.append(card)

    def __len__(self) -> int:
        return len(self.cards)

    def __repr__(self):
        display = 'CardPile('
        if len(self) > 0:
            for card in self.cards:
                display += repr(card) + ','
            return display[0:-1] + ')'
        else:
            return display + ')'

    def __str__(self) -> str:
        if len(self) > 0:
            display=''
            for card in self.cards:
                display += str(card) + ','
            return display[0:-1]
        else:
            return '[]'

    def add(self, card, totop = True):
        '''adds card to pile'''
        if not isinstance(card, (tuple, Card)):
            raise TypeError('CardPile.add() card argument must be a Card or a tuple, not a '+str(type(card)))
        if isinstance(card, tuple):
            card = Card(*card)
        if not isinstance(totop, bool):
            raise TypeError('CardPile.add() card argument must be a boolean, not a '+str(type(totop)))
        if totop:
            self.cards.append(card)
        else:
            self.cards.insert(0, card)
        return self

    def take(self, fromtop=True) -> Card:
        '''removes card from pile and returns it'''
        if not isinstance(fromtop, bool):
            raise TypeError('CardPile.take() fromtop argument must be a boolean, not a '+str(type(fromtop)))
        if len(self) < 1:
            raise IllegalMove('CardPile must contain at least one Card to use .take()')
        if fromtop:
            card = self.cards.pop()
        else:
            card = self.cards.pop(0)
        return card

    def __eq__(self, cardpile) -> bool:
        return self.cards == cardpile.cards

    def __ne__(self, cardpile) -> bool:
        return not self == cardpile

    def __contains__(self, card: Card) -> bool:
        return card in self.cards

    def __iter__(self):
        return iter(self.cards)

assert len(CardPile()) == 0
assert len(CardPile(('spade', 'ace'))) == 1
assert len(CardPile(('heart', 'four'), ('diamond', 'seven'))) == 2
assert CardPile(('diamond', 'two', False)).add(('club', 'ten', False)) == CardPile(('diamond', 'two', False), ('club', 'ten', False))
assert CardPile(('spade', 'queen')).add(('heart', 'seven'), False) == CardPile(('heart', 'seven'), ('spade', 'queen'))
assert CardPile(('spade', 'three'), ('diamond', 'jack')).take() == Card('diamond', 'jack')
assert CardPile(('heart', 'eight'), ('spade', 'seven')).take(False) == Card('heart', 'eight')
assert repr(CardPile()) == 'CardPile()'
assert repr(CardPile(('spade', 'ace'), ('heart', 'two'))) == 'CardPile(Card(Suit(\'spade\'),Rank(\'ace\'),True),Card(Suit(\'heart\'),Rank(\'two\'),True))'
assert str(CardPile())=='[]'
assert str(CardPile(('heart', 'four'))) == '**'
assert str(CardPile(('diamond', 'king', False), ('club', 'seven', False))) == 'dK,c7'
