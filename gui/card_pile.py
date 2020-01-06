from turtle import Turtle
from solitaire.game.card_pile import CardPile
from solitaire.game.card import Card
from solitaire.gui.card import GCard

class GCardPile(CardPile):
    '''a graphical representation of a pile of playing cards'''
    FACEDOWN_X_GAP = 0
    FACEDOWN_Y_GAP = -0.2
    FACEUP_X_GAP = 0
    FACEUP_Y_GAP = -0.4
    def __init__(self, cards: [Card], rad: int, x: float = 0, y: float = 0):
        CardPile.__init__(self, *cards)
        if not isinstance(rad, int):
            raise TypeError('\'rad\' must be an integer, not a '+str(type(rad)))
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
        return 'GCardPile('+repr(self.cards)+','+repr(rad)+','+repr(x)+','+repr(y)+')'

    def display(self, faceup_x_gap: float = None, faceup_y_gap: float = None, facedown_x_gap: float = None, facedown_y_gap: float = None) -> [Turtle]:
        if faceup_x_gap == None:
            faceup_x_gap = GCardPile.FACEUP_X_GAP
        if faceup_y_gap == None:
            faceup_y_gap = GCardPile.FACEUP_Y_GAP
        if facedown_x_gap == None:
            facedown_x_gap = GCardPile.FACEDOWN_X_GAP
        if facedown_y_gap == None:
            facedown_y_gap = GCardPile.FACEDOWN_Y_GAP
        if isinstance(faceup_x_gap, int):
            faceup_x_gap = float(faceup_x_gap)
        if not isinstance(faceup_x_gap, float):
            raise TypeError('\'faceup_x_gap\' must be a float, not a '+str(type(faceup_x_gap)))
        if isinstance(faceup_y_gap, int):
            faceup_y_gap = float(faceup_y_gap)
        if not isinstance(faceup_y_gap, float):
            raise TypeError('\'faceup_y_gap\' must be a float, not a '+str(type(faceup_y_gap)))
        if isinstance(facedown_x_gap, int):
            facedown_x_gap = float(facedown_x_gap)
        if not isinstance(facedown_x_gap, float):
            raise TypeError('\'facedown_x_gap\' must be a float, not a '+str(type(facedown_x_gap)))
        if isinstance(facedown_y_gap, int):
            facedown_y_gap = float(facedown_y_gap)
        if not isinstance(facedown_y_gap, float):
            raise TypeError('\'facedown_y_gap\' must be a float, not a '+str(type(facedown_y_gap)))
        t = []
        x_gap = 0.0
        y_gap = 0.0
        for i in range(len(self)):
            card = self.cards[i]
            if card.facedown:
                t.append(GCard(card.suit, card.rank, self.rad, card.facedown, self.x + x_gap, self.y + y_gap).display())
                x_gap += facedown_x_gap * self.rad
                y_gap += facedown_y_gap * self.rad
            else:
                t.extend(GCard(card.suit, card.rank, self.rad, card.facedown, self.x + x_gap, self.y + y_gap).display())
                x_gap += faceup_x_gap * self.rad
                y_gap += faceup_y_gap * self.rad
        return t

if __name__ == '__main__':
    GCardPile((Card('spade','ace',False), Card('heart','two',False), Card('club','queen',False), Card('diamond','king',False)), 50, -50).display()
    GCardPile((Card('spade','four',True), Card('heart','seven',True), Card('diamond','ten',False), Card('club','five',True)), 50, 50).display()
