from turtle import Turtle, delay
from solitaire.game.suit import Suit
from solitaire.game.color import Color
from solitaire.gui.symbols import draw_spade, draw_club, draw_heart, draw_diamond, draw_text, draw_square
from solitaire.gui.card_back import draw_card_up_back

def draw_ace_card_pip(suit: Suit, rad: float, x: float = 0, y: float = 0) -> [Turtle]:
    '''draw the pips of a face up ace playing card'''
    if isinstance(suit, str):
        suit = Suit(suit)
    if not isinstance(suit, Suit):
        raise TypeError('\'suit\' must be a Suit, not a '+str(type(suit)))
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
    size = 0.5
    pos = [0, 0]
    t = []
    if suit == Suit('spade'):
        t.append(draw_spade(rad * size, x + rad * pos[0], y + rad * pos[1]))
    elif suit == Suit('heart'):
        t.append(draw_heart(rad * size, x + rad * pos[0], y + rad * pos[1]))
    elif suit == Suit('club'):
        t.append(draw_club(rad * size, x + rad * pos[0], y + rad * pos[1]))
    elif suit == Suit('diamond'):
        t.append(draw_diamond(rad * size, x + rad * pos[0], y + rad * pos[1]))
    else:
        raise Exception('draw function for suit \''+str(suit)+'\' cannot be found')
    return t

def draw_two_card_pip(suit: Suit, rad: float, x: float = 0, y: float = 0) -> [Turtle]:
    '''draw the pips of a face up two playing card'''
    if isinstance(suit, str):
        suit = Suit(suit)
    if not isinstance(suit, Suit):
        raise TypeError('\'suit\' must be a Suit, not a '+str(type(suit)))
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
    size = 0.15
    pos = [[0, 0.4],
           [0, -0.4]]
    t = []
    for item in pos:
        if suit == Suit('spade'):
            t.append(draw_spade(rad * size, x + rad * item[0], y + rad * item[1]))
        elif suit == Suit('heart'):
            t.append(draw_heart(rad * size, x + rad * item[0], y + rad * item[1]))
        elif suit == Suit('club'):
            t.append(draw_club(rad * size, x + rad * item[0], y + rad * item[1]))
        elif suit == Suit('diamond'):
            t.append(draw_diamond(rad * size, x + rad * item[0], y + rad * item[1]))
        else:
            raise Exception('draw function for suit \''+str(suit)+'\' cannot be found')
    return t

def draw_three_card_pip(suit: Suit, rad: float, x: float = 0, y: float = 0) -> [Turtle]:
    '''draw the pips of a face up three playing card'''
    if isinstance(suit, str):
        suit = Suit(suit)
    if not isinstance(suit, Suit):
        raise TypeError('\'suit\' must be a Suit, not a '+str(type(suit)))
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
    size = 0.15
    pos = [[0, 0.4],
           [0, 0],
           [0, -0.4]]
    t = []
    for item in pos:
        if suit == Suit('spade'):
            t.append(draw_spade(rad * size, x + rad * item[0], y + rad * item[1]))
        elif suit == Suit('heart'):
            t.append(draw_heart(rad * size, x + rad * item[0], y + rad * item[1]))
        elif suit == Suit('club'):
            t.append(draw_club(rad * size, x + rad * item[0], y + rad * item[1]))
        elif suit == Suit('diamond'):
            t.append(draw_diamond(rad * size, x + rad * item[0], y + rad * item[1]))
        else:
            raise Exception('draw function for suit \''+str(suit)+'\' cannot be found')
    return t

def draw_four_card_pip(suit: Suit, rad: float, x: float = 0, y: float = 0) -> [Turtle]:
    '''draw the pips of a face up four playing card'''
    if isinstance(suit, str):
        suit = Suit(suit)
    if not isinstance(suit, Suit):
        raise TypeError('\'suit\' must be a Suit, not a '+str(type(suit)))
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
    size = 0.15
    pos = [[0.3, 0.4],
           [0.3, -0.4],
           [-0.3, 0.4],
           [-0.3, -0.4]]
    t = []
    for item in pos:
        if suit == Suit('spade'):
            t.append(draw_spade(rad * size, x + rad * item[0], y + rad * item[1]))
        elif suit == Suit('heart'):
            t.append(draw_heart(rad * size, x + rad * item[0], y + rad * item[1]))
        elif suit == Suit('club'):
            t.append(draw_club(rad * size, x + rad * item[0], y + rad * item[1]))
        elif suit == Suit('diamond'):
            t.append(draw_diamond(rad * size, x + rad * item[0], y + rad * item[1]))
        else:
            raise Exception('draw function for suit \''+str(suit)+'\' cannot be found')
    return t

def draw_five_card_pip(suit: Suit, rad: float, x: float = 0, y: float = 0) -> [Turtle]:
    '''draw the pips of a face up five playing card'''
    if isinstance(suit, str):
        suit = Suit(suit)
    if not isinstance(suit, Suit):
        raise TypeError('\'suit\' must be a Suit, not a '+str(type(suit)))
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
    size = 0.15
    pos = [[0.3, 0.4],
           [0.3, -0.4],
           [-0.3, 0.4],
           [-0.3, -0.4],
           [0, 0]]
    t = []
    for item in pos:
        if suit == Suit('spade'):
            t.append(draw_spade(rad * size, x + rad * item[0], y + rad * item[1]))
        elif suit == Suit('heart'):
            t.append(draw_heart(rad * size, x + rad * item[0], y + rad * item[1]))
        elif suit == Suit('club'):
            t.append(draw_club(rad * size, x + rad * item[0], y + rad * item[1]))
        elif suit == Suit('diamond'):
            t.append(draw_diamond(rad * size, x + rad * item[0], y + rad * item[1]))
        else:
            raise Exception('draw function for suit \''+str(suit)+'\' cannot be found')
    return t

def draw_six_card_pip(suit: Suit, rad: float, x: float = 0, y: float = 0) -> [Turtle]:
    '''draw the pips of a face up six playing card'''
    if isinstance(suit, str):
        suit = Suit(suit)
    if not isinstance(suit, Suit):
        raise TypeError('\'suit\' must be a Suit, not a '+str(type(suit)))
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
    size = 0.15
    pos = [[0.3, 0.5],
           [0.3, 0],
           [0.3, -0.5],
           [-0.3, 0.5],
           [-0.3, 0],
           [-0.3, -0.5]]
    t = []
    for item in pos:
        if suit == Suit('spade'):
            t.append(draw_spade(rad * size, x + rad * item[0], y + rad * item[1]))
        elif suit == Suit('heart'):
            t.append(draw_heart(rad * size, x + rad * item[0], y + rad * item[1]))
        elif suit == Suit('club'):
            t.append(draw_club(rad * size, x + rad * item[0], y + rad * item[1]))
        elif suit == Suit('diamond'):
            t.append(draw_diamond(rad * size, x + rad * item[0], y + rad * item[1]))
        else:
            raise Exception('draw function for suit \''+str(suit)+'\' cannot be found')
    return t

def draw_seven_card_pip(suit: Suit, rad: float, x: float = 0, y: float = 0) -> [Turtle]:
    '''draw the pips of a face up seven playing card'''
    if isinstance(suit, str):
        suit = Suit(suit)
    if not isinstance(suit, Suit):
        raise TypeError('\'suit\' must be a Suit, not a '+str(type(suit)))
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
    size = 0.15
    pos = [[0.3, 0.5],
           [0.3, 0],
           [0.3, -0.5],
           [-0.3, 0.5],
           [-0.3, 0],
           [-0.3, -0.5],
           [0, 0.25]]
    t = []
    for item in pos:
        if suit == Suit('spade'):
            t.append(draw_spade(rad * size, x + rad * item[0], y + rad * item[1]))
        elif suit == Suit('heart'):
            t.append(draw_heart(rad * size, x + rad * item[0], y + rad * item[1]))
        elif suit == Suit('club'):
            t.append(draw_club(rad * size, x + rad * item[0], y + rad * item[1]))
        elif suit == Suit('diamond'):
            t.append(draw_diamond(rad * size, x + rad * item[0], y + rad * item[1]))
        else:
            raise Exception('draw function for suit \''+str(suit)+'\' cannot be found')
    return t

def draw_eight_card_pip(suit: Suit, rad: float, x: float = 0, y: float = 0) -> [Turtle]:
    '''draw the pips of a face up eight playing card'''
    if isinstance(suit, str):
        suit = Suit(suit)
    if not isinstance(suit, Suit):
        raise TypeError('\'suit\' must be a Suit, not a '+str(type(suit)))
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
    size = 0.15
    pos = [[0.3, 0.5],
           [0.3, 0],
           [0.3, -0.5],
           [-0.3, 0.5],
           [-0.3, 0],
           [-0.3, -0.5],
           [0, 0.25],
           [0, -0.25]]
    t = []
    for item in pos:
        if suit == Suit('spade'):
            t.append(draw_spade(rad * size, x + rad * item[0], y + rad * item[1]))
        elif suit == Suit('heart'):
            t.append(draw_heart(rad * size, x + rad * item[0], y + rad * item[1]))
        elif suit == Suit('club'):
            t.append(draw_club(rad * size, x + rad * item[0], y + rad * item[1]))
        elif suit == Suit('diamond'):
            t.append(draw_diamond(rad * size, x + rad * item[0], y + rad * item[1]))
        else:
            raise Exception('draw function for suit \''+str(suit)+'\' cannot be found')
    return t

def draw_nine_card_pip(suit: Suit, rad: float, x: float = 0, y: float = 0) -> [Turtle]:
    '''draw the pips of a face up nine playing card'''
    if isinstance(suit, str):
        suit = Suit(suit)
    if not isinstance(suit, Suit):
        raise TypeError('\'suit\' must be a Suit, not a '+str(type(suit)))
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
    size = 0.15
    pos = [[0.3, 0.2],
           [0.3, 0.55],
           [0.3, -0.2],
           [0.3, -0.55],
           [-0.3, 0.2],
           [-0.3, 0.55],
           [-0.3, -0.2],
           [-0.3, -0.55],
           [0, 0]]
    t = []
    for item in pos:
        if suit == Suit('spade'):
            t.append(draw_spade(rad * size, x + rad * item[0], y + rad * item[1]))
        elif suit == Suit('heart'):
            t.append(draw_heart(rad * size, x + rad * item[0], y + rad * item[1]))
        elif suit == Suit('club'):
            t.append(draw_club(rad * size, x + rad * item[0], y + rad * item[1]))
        elif suit == Suit('diamond'):
            t.append(draw_diamond(rad * size, x + rad * item[0], y + rad * item[1]))
        else:
            raise Exception('draw function for suit \''+str(suit)+'\' cannot be found')
    return t

def draw_ten_card_pip(suit: Suit, rad: float, x: float = 0, y: float = 0) -> [Turtle]:
    '''draw the pips of a face up ten playing card'''
    if isinstance(suit, str):
        suit = Suit(suit)
    if not isinstance(suit, Suit):
        raise TypeError('\'suit\' must be a Suit, not a '+str(type(suit)))
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
    size = 0.15
    pos = [[0.3, 0.2],
           [0.3, 0.55],
           [0.3, -0.2],
           [0.3, -0.55],
           [-0.3, 0.2],
           [-0.3, 0.55],
           [-0.3, -0.2],
           [-0.3, -0.55],
           [0, 0.35],
           [0, -0.35]]
    t = []
    for item in pos:
        if suit == Suit('spade'):
            t.append(draw_spade(rad * size, x + rad * item[0], y + rad * item[1]))
        elif suit == Suit('heart'):
            t.append(draw_heart(rad * size, x + rad * item[0], y + rad * item[1]))
        elif suit == Suit('club'):
            t.append(draw_club(rad * size, x + rad * item[0], y + rad * item[1]))
        elif suit == Suit('diamond'):
            t.append(draw_diamond(rad * size, x + rad * item[0], y + rad * item[1]))
        else:
            raise Exception('draw function for suit \''+str(suit)+'\' cannot be found')
    return t

def draw_jack_card_pip(suit: Suit, rad: float, x: float = 0, y: float = 0) -> [Turtle]:
    '''draw the pips of a face up jack playing card'''
    if isinstance(suit, str):
        suit = Suit(suit)
    if not isinstance(suit, Suit):
        raise TypeError('\'suit\' must be a Suit, not a '+str(type(suit)))
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
    symbol_size = 0.2
    symbol_pos = [0, 0.4]
    text_size = 0.5
    text_pos = [0, -0.4]
    t = []
    if suit == Suit('spade'):
        t.append(draw_spade(rad * symbol_size, x + rad * symbol_pos[0], y + rad * symbol_pos[1]))
    elif suit == Suit('heart'):
        t.append(draw_heart(rad * symbol_size, x + rad * symbol_pos[0], y + rad * symbol_pos[1]))
    elif suit == Suit('club'):
        t.append(draw_club(rad * symbol_size, x + rad * symbol_pos[0], y + rad * symbol_pos[1]))
    elif suit == Suit('diamond'):
        t.append(draw_diamond(rad * symbol_size, x + rad * symbol_pos[0], y + rad * symbol_pos[1]))
    else:
        raise Exception('draw function for suit \''+str(suit)+'\' cannot be found')
    if suit.color() == Color('black'):
        t.append(draw_text('J', 'black', rad * text_size, x + rad * text_pos[0], y + rad * text_pos[1]))
    elif suit.color() == Color('red'):
        t.append(draw_text('J', 'red', rad * text_size, x + rad * text_pos[0], y + rad * text_pos[1]))
    else:
        raise Exception('draw function for suit \''+str(suit)+'\' cannot be found')
    return t

def draw_queen_card_pip(suit: Suit, rad: float, x: float = 0, y: float = 0) -> [Turtle]:
    '''draw the pips of a face up queen playing card'''
    if isinstance(suit, str):
        suit = Suit(suit)
    if not isinstance(suit, Suit):
        raise TypeError('\'suit\' must be a Suit, not a '+str(type(suit)))
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
    symbol_size = 0.2
    symbol_pos = [0, 0.4]
    text_size = 0.5
    text_pos = [0, -0.4]
    t = []
    if suit == Suit('spade'):
        t.append(draw_spade(rad * symbol_size, x + rad * symbol_pos[0], y + rad * symbol_pos[1]))
    elif suit == Suit('heart'):
        t.append(draw_heart(rad * symbol_size, x + rad * symbol_pos[0], y + rad * symbol_pos[1]))
    elif suit == Suit('club'):
        t.append(draw_club(rad * symbol_size, x + rad * symbol_pos[0], y + rad * symbol_pos[1]))
    elif suit == Suit('diamond'):
        t.append(draw_diamond(rad * symbol_size, x + rad * symbol_pos[0], y + rad * symbol_pos[1]))
    else:
        raise Exception('draw function for suit \''+str(suit)+'\' cannot be found')
    if suit.color() == Color('black'):
        t.append(draw_text('Q', 'black', rad * text_size, x + rad * text_pos[0], y + rad * text_pos[1]))
    elif suit.color() == Color('red'):
        t.append(draw_text('Q', 'red', rad * text_size, x + rad * text_pos[0], y + rad * text_pos[1]))
    else:
        raise Exception('draw function for suit \''+str(suit)+'\' cannot be found')
    return t

def draw_king_card_pip(suit: Suit, rad: float, x: float = 0, y: float = 0) -> [Turtle]:
    '''draw the pips of a face up king playing card'''
    if isinstance(suit, str):
        suit = Suit(suit)
    if not isinstance(suit, Suit):
        raise TypeError('\'suit\' must be a Suit, not a '+str(type(suit)))
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
    symbol_size = 0.2
    symbol_pos = [0, 0.4]
    text_size = 0.5
    text_pos = [0, -0.4]
    t = []
    if suit == Suit('spade'):
        t.append(draw_spade(rad * symbol_size, x + rad * symbol_pos[0], y + rad * symbol_pos[1]))
    elif suit == Suit('heart'):
        t.append(draw_heart(rad * symbol_size, x + rad * symbol_pos[0], y + rad * symbol_pos[1]))
    elif suit == Suit('club'):
        t.append(draw_club(rad * symbol_size, x + rad * symbol_pos[0], y + rad * symbol_pos[1]))
    elif suit == Suit('diamond'):
        t.append(draw_diamond(rad * symbol_size, x + rad * symbol_pos[0], y + rad * symbol_pos[1]))
    else:
        raise Exception('draw function for suit \''+str(suit)+'\' cannot be found')
    if suit.color() == Color('black'):
        t.append(draw_text('K', 'black', rad * text_size, x + rad * text_pos[0], y + rad * text_pos[1]))
    elif suit.color() == Color('red'):
        t.append(draw_text('K', 'red', rad * text_size, x + rad * text_pos[0], y + rad * text_pos[1]))
    else:
        raise Exception('draw function for suit \''+str(suit)+'\' cannot be found')
    return t

if __name__ == '__main__':
    delay(0)
    
    draw_card_up_back(100, -300, 200)
    draw_ace_card_pip('spade', 100, -300, 200)
    
    draw_card_up_back(100, -100, 200)
    draw_two_card_pip('heart', 100, -100, 200)
    
    draw_card_up_back(100, 100, 200)
    draw_three_card_pip('club', 100, 100, 200)
    
    draw_card_up_back(100, 300, 200)
    draw_four_card_pip('diamond', 100, 300, 200)
    
    draw_card_up_back(100, -400, 0)
    draw_five_card_pip('spade', 100, -400, 0)
    
    draw_card_up_back(100, -200, 0)
    draw_six_card_pip('heart', 100, -200, 0)
    
    draw_card_up_back(100, 0, 0)
    draw_seven_card_pip('club', 100, 0, 0)
    
    draw_card_up_back(100, 200, 0)
    draw_eight_card_pip('diamond', 100, 200, 0)
    
    draw_card_up_back(100, 400, 0)
    draw_nine_card_pip('spade', 100, 400, 0)
    
    draw_card_up_back(100, -300, -200)
    draw_ten_card_pip('heart', 100, -300, -200)
    
    draw_card_up_back(100, -100, -200)
    draw_jack_card_pip('club', 100, -100, -200)
    
    draw_card_up_back(100, 100, -200)
    draw_queen_card_pip('diamond', 100, 100, -200)
    
    draw_card_up_back(100, 300, -200)
    draw_king_card_pip('spade', 100, 300, -200)
