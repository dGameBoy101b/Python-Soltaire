from turtle import Turtle
from solitaire.game.build_pile import BuildingPile
from solitaire.game.card import Card
from solitaire.gui.card_pile import GCardPile

class GBuildingPile(BuildingPile):
    '''a graphical representation of a solitaire building pile'''

    def __init__(self, rad: float, cards: [Card] = [], x: float = 0, y: float = 0):
        BuildingPile.__init__(self, *cards)
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
        return 'GBuildingPile('+repr(self.rad)+','+repr(self.cards)+','+repr(self.x)+','+repr(self.y)+')'

    def display(self) -> [Turtle]:
        return GCardPile(self.cards, self.rad, self.x, self.y).display()

if __name__ == '__main__':
    GBuildingPile(50, [], -50).display()
    GBuildingPile(50, [Card('spade','two'),Card('heart','ten'),Card('diamond','ten',False),Card('club','nine',False)], 50).display()
