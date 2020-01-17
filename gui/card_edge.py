from turtle import Turtle, delay
from solitaire.game.color import Color
from solitaire.game.suit import Suit
from solitaire.game.rank import Rank
from solitaire.gui.symbols import draw_spade, draw_heart, draw_club, draw_diamond, draw_text
from solitaire.gui.card_back import card_rat, draw_card_up_back
from solitaire.gui.card_pips import draw_ace_card_pip

def draw_card_left_edge(suit: Suit, rank: Rank, rad: float, x: float = 0, y: float = 0) -> [Turtle]:
    '''draw the upper left corner edge symbols of a playing card'''
    if isinstance(suit, str):
        suit = Suit(suit)
    if not isinstance(suit, Suit):
        raise TypeError('\'suit\' must be a Suit, not a '+str(type(suit)))
    if isinstance(rank, str):
        rank = Rank(rank)
    if not isinstance(rank, Rank):
        raise TypeError('\'rank\' must be a Rank, not a '+str(type(rank)))
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
    margin = 0.05
    symbol_size = 0.075
    text_size = 0.125
    symbol_transform = (symbol_size * rad, x + rad * (symbol_size - globals()['card_rat'] + margin), y + rad * (1 - symbol_size - margin))
    text_transform = (text_size * rad, x + rad * (text_size - globals()['card_rat'] + margin), y + rad * (1 - text_size - 2 * symbol_size - margin))
    t = []
    if suit == Suit('spade'):
        t.append(draw_spade(*symbol_transform))
    elif suit == Suit('heart'):
        t.append(draw_heart(*symbol_transform))
    elif suit == Suit('club'):
        t.append(draw_club(*symbol_transform))
    elif suit == Suit('diamond'):
        t.append(draw_diamond(*symbol_transform))
    else:
        raise Exception('draw function for suit \''+str(suit)+'\' cannot be found')
    if suit.color() == Color('black'):
        t.append(draw_text(str(rank), 'black', *text_transform, 'left'))
    elif suit.color() == Color('red'):
        t.append(draw_text(str(rank), 'red', *text_transform, 'left'))
    else:
        raise Exception('draw function for color of suit \''+str(suit)+'\' cannot be found')
    return t

if __name__ == '__main__':
    delay(0)
    draw_card_up_back(100, 0, 0)
    draw_card_left_edge('spade', 'ace', 100, 0, 0)
    draw_ace_card_pip('spade', 100, 0, 0)
