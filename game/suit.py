from solitaire.game.color import Color

class Suit():
    '''the four suits of a standard playing card deck as full string literals'''
    suits = frozenset({'spade', 'heart', 'club', 'diamond'})
    shorthand = {'spade':'s', 'heart':'h', 'club':'c', 'diamond':'d'}
    longhand = {'s':'spade', 'h':'heart', 'c':'club', 'd':'diamond'}

    def __init__(self, value:str):
        if not isinstance(value, str):
            raise TypeError('Suit() value argument must be a string, not a '+str(type(value)))
        if value in Suit.shorthand:
            self.value = value
        elif value in Suit.longhand:
            self.value = Suit.longhand[value]
        else:
            raise ValueError(value+' is not a Suit')

    def __hash__(self):
        return id(self)

    def __eq__(self,suit) -> bool:
        if not isinstance(suit, Suit):
            raise TypeError('only a Suit can be compared to a Suit, not a '+str(type(value)))
        return self.value == suit.value

    def __ne__(self,suit) -> bool:
        return not self == suit

    def color(self):
        '''determines color of suit'''
        if self.value == 'spade' or self.value == 'club':
            return Color('black')
        else:
            return Color('red')

    def __str__(self) -> str:
        return str(Suit.shorthand[self.value])

    def __repr__(self) -> str:
        return str('Suit(\''+str(self.value)+'\')')
    
assert Suit('spade').value == 'spade'
assert Suit('heart').value == 'heart'
assert Suit('club').value == 'club'
assert Suit('diamond').value == 'diamond'
assert Suit('spade').color() == Color('black')
assert Suit('heart').color() == Color('red')
assert Suit('club') == Suit('club')
assert Suit('diamond') != Suit('heart')
assert str(Suit('spade')) == 's'
assert repr(Suit('heart')) == 'Suit(\'heart\')'
