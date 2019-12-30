from solitaire.game.card_pile import CardPile, IllegalMove
from solitaire.game.card import Card
from solitaire.game.suit import Suit
from solitaire.extended_debug import error_test

class EndPile(CardPile):
    '''piles for submitting cards of the same suit, in ascending order'''

    def __init__(self, suit: Suit, *cards):
        if isinstance(suit, str):
            suit = Suit(suit)
        if not isinstance(suit, Suit):
            raise TypeError('\'suit\' must be a valid suit, not a '+str(type(suit)))
        self.suit = suit
        CardPile.__init__(self, *cards)

    def topCard(self) -> Card:
        '''returns top card of pile'''
        return self.cards[len(self) - 1]

    def stack(self, card: Card):
        '''attempts to legally stack given card'''
        if isinstance(card, tuple):
            card = Card(*card)
        if not isinstance(card, Card):
            raise TypeError('EndPile.stack() card argument must be a Card, not a '+str(type(card)))
        if self.suit != card.suit:
            raise IllegalMove('end piles must stack cards of the same suit')
        if len(self) > 0:
            rank = self.topCard().rank.value
            if rank == 'ace' and card.rank.value == 'two':
                pass
            elif rank == 'two' and card.rank.value == 'three':
                pass
            elif rank == 'three' and card.rank.value == 'four':
                pass
            elif rank == 'four' and card.rank.value == 'five':
                pass
            elif rank == 'five' and card.rank.value == 'six':
                pass
            elif rank == 'six' and card.rank.value == 'seven':
                pass
            elif rank == 'seven' and card.rank.value == 'eight':
                pass
            elif rank == 'eight' and card.rank.value == 'nine':
                pass
            elif rank == 'nine' and card.rank.value == 'ten':
                pass
            elif rank == 'ten' and card.rank.value == 'jack':
                pass
            elif rank == 'jack' and card.rank.value == 'queen':
                pass
            elif rank == 'queen' and card.rank.value == 'king':
                pass
            else:
                raise IllegalMove('end piles must stack cards in ascending rank')
        elif card.rank.value == 'ace':
            pass
        else:
            raise IllegalMove('end piles must stack \'ace\' ranked cards first')
        self.add(Card(card.suit, card.rank, False))
        return self

    def __repr__(self) -> str:
        display = 'EndPile(' + repr(self.suit) + ','
        for card in self.cards:
            display += repr(card) + ','
        return display[0:-1] + ')'

    def __str__(self) -> str:
        if len(self) > 0:
            return str(self.topCard())
        else:
            return '[]'
        
assert len(EndPile('spade')) == 0
assert len(EndPile('heart').stack(('heart','ace'))) == 1
assert error_test.expect('EndPile("diamond").stack(("club","ace"))' ,IllegalMove, global_variables=globals())
assert error_test.expect('EndPile("spade").stack(("spade","six"))', IllegalMove, global_variables=globals())
assert error_test.expect('EndPile("heart").stack(("heart","ace")).stack(("heart","three"))', IllegalMove, global_variables=globals())
assert repr(EndPile('diamond')) == "EndPile(Suit('diamond'))"
assert repr(EndPile('club', ('club', 'A', False), ('club', 'two', False))) == "EndPile(Suit('club'),Card(Suit('club'),Rank('ace'),False),Card(Suit('club'),Rank('two'),False))"
assert str(EndPile('spade')) == '[]'
assert str(EndPile('heart', ('heart', 'ace', False), ('heart', 'two', False))) == 'h2'
