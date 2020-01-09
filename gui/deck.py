from turtle import Turtle
from solitaire.game.deck import Deck
from solitaire.game.card import Card
from solitaire.gui.card_pile import GCardPile
from solitaire.gui.symbols import draw_text
from solitaire.gui.card_back import draw_blank_cell, draw_card_down_back

class GDeck(Deck):
    '''a graphical representation of a playing card deck'''
    COUNT_X_POS = 0
    COUNT_Y_POS = -1.3
    COUNT_SIZE = 0.3

    def __init__(self, rad: float, init_cards: (Card) = None, x: float = 0, y: float = 0):
        Deck.__init__(self, init_cards)
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
        self.rad = rad
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        return

    def __repr__(self) -> str:
        return 'GDeck('+repr(self.rad)+','+repr(self.init_cards)+','+repr(self.x)+','+repr(self.y)+')'

    def display(self) -> [Turtle]:
        self.width = self.rad * 2 * globals()['card_rat'] + self.rad * GDeck.COUNT_SIZE * 2
        self.height = self.rad * 2 + self.rad * GDeck.COUNT_SIZE * 2
        t = []
        if len(self) < 1:
            t.append(draw_blank_cell(self.rad, self.x, self.y))
        else:
            t.append(draw_card_down_back(self.rad, self.x, self.y))
        t.append(draw_text(str(len(self)), 'black', self.rad * GDeck.COUNT_SIZE, self.x + GDeck.COUNT_X_POS * self.rad, self.y + GDeck.COUNT_Y_POS * self.rad))
        return t

if __name__ == '__main__':
    GDeck(50, None, -150).display()
    GDeck(50, (), 0).display()
    GDeck(50, (Card('heart','seven'),Card('club','king'),Card('diamond','nine'),Card('heart','two'),Card('spade','jack')), 150).display()
