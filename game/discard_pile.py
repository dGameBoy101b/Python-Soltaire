from solitaire.game.card_pile import CardPile, IllegalMove
from solitaire.game.card import Card
from solitaire.extended_debug import error_test

class DiscardPile(CardPile):
    '''piles where discarded cards go and can be recycled back into the deck'''

    def __init__(self, *init_cards: tuple):
        self.cards = []
        for card in init_cards:
            if not isinstance(card, (tuple, Card)):
                raise TypeError('DiscardPile() *init_cards argument must contain only tuple or Card types, not '+str(type(card)))
            if isinstance(card, tuple):
                self.cards.append(Card(card[0], card[1], False))
            else:
                self.cards.append(Card(card.suit, card.rank, False))

    def topCard(self) -> Card:
        return self.cards[-1]

    def take(self, n: int = 1) -> CardPile:
        if not isinstance(n, int):
            raise TypeError('DiscardPile.take() n argument must be an integer, not a '+str(type(n)))
        if n > len(self):
            raise IndexError('Can only .take() up to '+str(len(self))+' cards, not '+str(n))
        cards = CardPile()
        for i in range(n):
            cards.add(self.topCard())
            self.cards.pop()
        return cards

    def reset(self) -> CardPile:
        if len(self) < 1:
            raise IllegalMove('DiscardPile() must have at least 1 Card to use .reset()')
        cards = self.cards
        self.cards = []
        return CardPile(*cards)

    def stack(self, *cards: tuple):
        if not isinstance(cards, (tuple, CardPile)):
            raise TypeError('DiscardPile.stack() *cards argument must be a tuple or a CardPile, not a '+str(type(cards)))
        if len(cards) < 1:
            raise IndexError('DiscardPile.stack() *cards argument must contain at least 1 Card, not '+str(len(cards)))
        for card in cards:
            if not isinstance(card, (Card, tuple)):
                raise TypeError('DiscardPile.stack() *cards argument must contain only Card types or tuple types, not '+str(type(card))+' types')
            if isinstance(card, tuple):
                self.add(Card(card[0], card[1], False))
            else:
                self.add(Card(card.suit, card.rank, False))
        return self

    def __str__(self) -> str:
        if len(self) > 0:
            return str(self.topCard())
        else:
            return '[]'

    def __repr__(self) -> str:
        display = 'DiscardPile('
        if len(self) > 0:
            for card in self.cards:
                display += repr(card) + ','
            return display[0:-1] + ')'
        else:
            return display + ')'
        
assert len(DiscardPile()) == 0
assert len(DiscardPile(('spade', 'ace'))) == 1
assert DiscardPile(('diamond', 'eight'), ('club', 'jack')).topCard() == Card('club', 'jack', False)
assert DiscardPile(('spade', 'three'), ('heart', 'king')).reset() == CardPile(('spade', 'three', False), ('heart', 'king', False))
assert str(DiscardPile()) == '[]'
assert repr(DiscardPile()) == 'DiscardPile()'
assert str(DiscardPile(('diamond', 'six'), ('club', 'ace'))) == 'cA'
assert repr(DiscardPile(('spade', 'two'), ('spade', 'queen'))) == 'DiscardPile(Card(Suit(\'spade\'),Rank(\'two\'),False),Card(Suit(\'spade\'),Rank(\'queen\'),False))'
assert DiscardPile().stack(('diamond', 'four'), ('heart', 'jack')) == DiscardPile(('diamond', 'four'), ('heart', 'jack'))
assert error_test.expect('DiscardPile().reset()',IllegalMove,global_variables=globals())
assert error_test.expect('DiscardPile().stack()',IndexError,global_variables=globals())
