from solitaire.game.suit import Suit
from solitaire.game.rank import Rank

class Card():
    '''a standard playing card'''
    def __init__(self, suit: str, rank: str, facedown: bool = True):
        if not isinstance(suit, (str, Suit)):
            raise TypeError('Card() suit argument must be a string or a Suit, not a '+str(type(suit)))
        if isinstance(suit, str):
            self.suit = Suit(suit)
        else:
            self.suit = suit
        if not isinstance(rank, (str, Rank)):
            raise TypeError('Card() rank argument must be a string or a Rank, not a '+str(type(rank)))
        if isinstance(rank, str):
            self.rank = Rank(rank)
        else:
            self.rank = rank
        if isinstance(facedown, bool):
            self.facedown = facedown
        else:
            raise TypeError('Card() facedown argument must be a boolean, not a '+str(type(facedown)))

    def __hash__(self):
        return id(self)

    def __eq__(self, card) -> bool:
        return self.suit == card.suit and self.rank == card.rank and self.facedown == card.facedown

    def __ne__(self, card) -> bool:
        return not self == card

    def flip(self, link: bool = False):
        '''toggles between faceup and facedown'''
        self.facedown = not self.facedown
        if link:
            self.hidden = self.facedown
        return self

    def __str__(self) -> str:
        if self.facedown:
            return '**'
        else:
            return str(str(self.suit)+str(self.rank))

    def __repr__(self):
        return str('Card('+repr(self.suit)+','+repr(self.rank)+','+str(self.facedown)+')')

assert Card('spade','ace').suit == Suit('spade')
assert Card('heart','two').rank == Rank('two')
assert Card('diamond','five').facedown == True
assert Card('club','ten',False).facedown == False
assert Card('club','three').flip() == Card('club','three',False)
assert Card('heart','king',False).flip() == Card('heart','king',True)
assert str(Card('spade','seven')) == '**'
assert str(Card('heart','three',False)) == 'h3'
assert repr(Card('diamond','ace')) == 'Card(Suit(\'diamond\'),Rank(\'ace\'),True)'
assert repr(Card('club','five',False)) == 'Card(Suit(\'club\'),Rank(\'five\'),False)'
