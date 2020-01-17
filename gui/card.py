from turtle import Turtle, delay
from solitaire.game.suit import Suit
from solitaire.game.rank import Rank
from solitaire.game.card import Card
from solitaire.gui.card_back import draw_card_up_back, draw_card_down_back, card_rat
from solitaire.gui.card_edge import draw_card_left_edge
from solitaire.gui.card_pips import (draw_ace_card_pip, draw_two_card_pip,
draw_three_card_pip, draw_four_card_pip, draw_five_card_pip, draw_six_card_pip,
draw_seven_card_pip, draw_eight_card_pip, draw_nine_card_pip, draw_ten_card_pip,
draw_jack_card_pip, draw_queen_card_pip, draw_king_card_pip)

class GCard(Card):
    '''a graphical representation of a playing card'''

    def __init__(self, suit: str, rank: str, rad: float, facedown: bool = True, x: float = 0, y: float = 0):
        Card.__init__(self, suit, rank, facedown)
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

    def display(self) -> [Turtle]:
        self.width = self.rad * globals()['card_rat'] * 2
        self.height = self.rad * 2
        if self.facedown:
            return draw_card_down_back(self.rad, self.x, self.y)
        t = [draw_card_up_back(self.rad, self.x, self.y)]
        t.extend(draw_card_left_edge(self.suit, self.rank, self.rad, self.x, self.y))
        if self.rank == Rank('ace'):
            t.extend(draw_ace_card_pip(self.suit, self.rad, self.x, self.y))
        elif self.rank == Rank('two'):
            t.extend(draw_two_card_pip(self.suit, self.rad, self.x, self.y))
        elif self.rank == Rank('three'):
            t.extend(draw_three_card_pip(self.suit, self.rad, self.x, self.y))
        elif self.rank == Rank('four'):
            t.extend(draw_four_card_pip(self.suit, self.rad, self.x, self.y))
        elif self.rank == Rank('five'):
            t.extend(draw_five_card_pip(self.suit, self.rad, self.x, self.y))
        elif self.rank == Rank('six'):
            t.extend(draw_six_card_pip(self.suit, self.rad, self.x, self.y))
        elif self.rank == Rank('seven'):
            t.extend(draw_seven_card_pip(self.suit, self.rad, self.x, self.y))
        elif self.rank == Rank('eight'):
            t.extend(draw_eight_card_pip(self.suit, self.rad, self.x, self.y))
        elif self.rank == Rank('nine'):
            t.extend(draw_nine_card_pip(self.suit, self.rad, self.x, self.y))
        elif self.rank == Rank('ten'):
            t.extend(draw_ten_card_pip(self.suit, self.rad, self.x, self.y))
        elif self.rank == Rank('jack'):
            t.extend(draw_jack_card_pip(self.suit, self.rad, self.x, self.y))
        elif self.rank == Rank('queen'):
            t.extend(draw_queen_card_pip(self.suit, self.rad, self.x, self.y))
        elif self.rank == Rank('king'):
            t.extend(draw_king_card_pip(self.suit, self.rad, self.x, self.y))
        else:
            raise Exception('pip draw functions could not be matched to the rank '+str(self.rank))
        t.extend(draw_card_left_edge(self.suit, self.rank, self.rad, self.x, self.y))
        return t

    def __eq__(self, other) -> bool:
        return isinstance(other, GCard) and self.suit == other.suit and self.rank == other.rank and self.facedown == other.facedown and self.rad == other.rad and self.x == other.x and self.y == other.y

    def __ne__(self, other) -> bool:
        return not self == other

    def __repr__(self) -> str:
        return str('GCard('+repr(self.suit)+','+repr(self.rank)+','+repr(self.rad)+','+repr(self.facedown)+','+repr(self.x)+','+repr(self.y)+')')
        
if __name__ == '__main__':
    assert GCard('spade', 'ace', 50, False).suit == Suit('spade')
    assert GCard('spade', 'ace', 50, False).rank == Rank('ace')
    assert GCard('spade', 'ace', 50, False).rad == 50
    assert GCard('spade', 'ace', 50, False).facedown == False
    assert GCard('spade', 'ace', 50, False).x == 0
    assert GCard('spade', 'ace', 50, False).y == 0
    assert GCard('spade', 'ace', 50, False) == GCard('spade', 'ace', 50, False)
    assert repr(GCard('spade', 'ace', 50, False)) == 'GCard(Suit(\'spade\'),Rank(\'ace\'),50.0,False,0.0,0.0)'
    delay(0)
    GCard('spade', 'ace', 50, False, -50).display()
    GCard('heart', 'king', 50, True, 50).display()
