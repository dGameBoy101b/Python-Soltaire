from turtle import Turtle, delay
from solitaire.game.discard_pile import DiscardPile
from solitaire.game.card import Card
from solitaire.gui.card_back import draw_blank_cell
from solitaire.gui.card_pile import GCardPile
from solitaire.gui.card import GCard
from solitaire.gui.symbols import draw_text

class GDiscardPile(DiscardPile, GCardPile):
    '''a graphical representation of a discard pile'''

    COUNT_X_POS = 0
    COUNT_Y_POS = -1.3
    COUNT_SIZE = 0.3

    def __init__(self, rad: float, init_cards: [Card] = [], x: float = 0, y: float = 0):
        DiscardPile.__init__(self, *init_cards)
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
        return

    def __repr__(self) -> str:
        return 'GDiscardPile('+repr(self.rad)+','+repr(self.cards)+','+repr(self.x)+','+repr(self.y)+')'

    def display(self) -> [Turtle]:
        t = []
        if len(self) < 1:
            t.append(draw_blank_cell(self.rad, self.x, self.y))
        else:
            t.append(GCard(self.topCard().suit, self.topCard().rank, self.rad, self.topCard().facedown, self.x, self.y).display())
        t.append(draw_text(str(len(self)), 'black', self.rad * GDiscardPile.COUNT_SIZE, self.x + GDiscardPile.COUNT_X_POS * self.rad, self.y + GDiscardPile.COUNT_Y_POS * self.rad))
        return t

if __name__ == '__main__':
    delay(0)
    GDiscardPile(50, [], -50).display()
    GDiscardPile(50, [Card('spade','ace',False),Card('heart','ace',False),Card('spade','ten',False),Card('diamond','seven',False),Card('heart','queen',False),Card('club','two',False)], 50).display()
