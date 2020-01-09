from turtle import Turtle
from solitaire.game.end_pile import EndPile
from solitaire.game.card import Card
from solitaire.game.suit import Suit
from solitaire.gui.card_pile import GCardPile
from solitaire.gui.card import GCard
from solitaire.gui.card_back import draw_blank_cell, card_rat
from solitaire.gui.symbols import draw_spade, draw_heart, draw_club, draw_diamond

class GEndPile(EndPile, GCardPile):
    '''a graphical representation of a solitaire end pile'''

    SYMBOL_SIZE = 0.6

    def __init__(self, suit: Suit, rad: float, cards: [Card] = [], x: float = 0, y: float = 0):
        EndPile.__init__(self, suit, *cards)
        if isinstance(rad, int):
            rad = float(rad)
        if not isinstance(rad, float):
            raise TypeError('\'rad\' must be a float, not a '+str(type(rad)))
        if isinstance(x, int):
            x = float(x)
        if not isinstance(x, float):
            raise TypeError('\'x\' must be a float, not a '+str(type(x)))
        if isinstance(y, int):
            y = float(y)
        if not isinstance(y, float):
            raise TypeError('\'y\' must be a float, not a '+str(type(y)))
        if rad <= 0:
            raise ValueError('\'rad\' must be greater than 0, not '+str(rad))
        self.rad = rad
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        return

    def __repr__(self) -> str:
        return 'GEndPile('+repr(self.suit)+','+repr(self.rad)+','+repr(self.cards)+','+repr(self.x)+','+repr(self.y)+')'

    def display(self) -> [Turtle]:
        self.width = self.rad * 2 * globals()['card_rat']
        self.height = self.rad * 2
        t = []
        if len(self) < 1:
            t.append(draw_blank_cell(self.rad, self.x, self.y))
            if self.suit == Suit('spade'):
                t.append(draw_spade(self.rad * GEndPile.SYMBOL_SIZE, self.x, self.y, 'gray'))
            elif self.suit == Suit('heart'):
                t.append(draw_heart(self.rad * GEndPile.SYMBOL_SIZE, self.x, self.y, 'gray'))
            elif self.suit == Suit('club'):
                t.append(draw_club(self.rad * GEndPile.SYMBOL_SIZE, self.x, self.y, 'gray'))
            elif self.suit == Suit('diamond'):
                t.append(draw_diamond(self.rad * GEndPile.SYMBOL_SIZE, self.x, self.y, 'gray'))
            else:
                raise Exception('could not find draw function for suit '+str(self.suit))
        else:
            t.append(GCard(self.topCard().suit, self.topCard().rank, self.rad, self.topCard().facedown, self.x, self.y).display())
        return t

if __name__ == '__main__':
    assert GEndPile('diamond', 100).rad == 100
    assert GEndPile('diamond', 100).x == 0
    assert GEndPile('diamond', 100).y == 0
    assert GEndPile('diamond', 100).width == 0
    assert GEndPile('diamond', 100).height == 0
    assert repr(GEndPile('diamond', 100)) == 'GEndPile(Suit(\'diamond\'),100.0,[],0.0,0.0)'
    test = GEndPile('spade', 50, [], -200)
    test.display()
    assert test.width == 100 * globals()['card_rat']
    assert test.height == 100
    GEndPile('heart', 50, [], -100).display()
    GEndPile('club', 50, [], 100).display()
    GEndPile('diamond', 50, [], 200).display()
    GEndPile('spade', 50, [Card('spade','ace',False),Card('spade','two',False),Card('spade','three',False)]).display()
