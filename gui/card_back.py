from turtle import Turtle

card_rat = 0.7

def draw_card_up_back(rad: float, x: float = 0, y: float = 0) -> Turtle:
    '''draw the background of a face up playing card'''
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
    rat = globals()['card_rat']
    t = Turtle(visible=False)
    t.penup()
    t.color('black', 'white')
    t.setpos(x - rad * rat, y - rad)
    t.pendown()
    t.begin_fill()
    t.setpos(x - rad * rat, y + rad)
    t.setpos(x + rad * rat, y + rad)
    t.setpos(x + rad * rat, y - rad)
    t.setpos(x - rad * rat, y - rad)
    t.end_fill()
    return t

def draw_card_down_back(rad: float, x: float = 0, y: float = 0) -> Turtle:
    '''draw the background of a face down playing card'''
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
    rat = globals()['card_rat']
    t = Turtle(visible=False)
    t.penup()
    t.color('black', 'blue')
    t.setpos(x - rad * rat, y - rad)
    t.pendown()
    t.begin_fill()
    t.setpos(x - rad * rat, y + rad)
    t.setpos(x + rad * rat, y + rad)
    t.setpos(x + rad * rat, y - rad)
    t.setpos(x - rad * rat, y - rad)
    t.end_fill()
    t.color('white')
    t.setpos(x + rad * rat, y + rad)
    t.penup()
    t.setpos(x - rad * rat, y + rad)
    t.pendown()
    t.setpos(x + rad * rat, y - rad)
    t.penup()
    t.setpos(x, y - rad)
    t.pendown()
    t.setpos(x, y + rad)
    t.penup()
    t.setpos(x - rad * rat, y)
    t.pendown()
    t.setpos(x + rad * rat, y)
    return t

def draw_blank_cell(rad: float, x: float = 0, y: float = 0) -> Turtle:
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
    rat = globals()['card_rat']
    t = Turtle(visible=False)
    t.penup()
    t.color('black', 'white')
    t.setpos(x - rad * rat, y - rad)
    t.pendown()
    t.begin_fill()
    t.setpos(x - rad * rat, y + rad)
    t.setpos(x + rad * rat, y + rad)
    t.setpos(x + rad * rat, y - rad)
    t.setpos(x - rad * rat, y - rad)
    t.end_fill()
    t.color('gray')
    t.setpos(x + rad * rat, y + rad)
    t.penup()
    t.setpos(x - rad * rat, y + rad)
    t.pendown()
    t.setpos(x + rad * rat, y - rad)
    t.penup()
    t.setpos(x, y - rad)
    t.pendown()
    t.setpos(x, y + rad)
    t.penup()
    t.setpos(x - rad * rat, y)
    t.pendown()
    t.setpos(x + rad * rat, y)
    return t

if __name__ == '__main__':
    draw_card_up_back(100, -300)
    draw_blank_cell(100, 0)
    draw_card_down_back(100, 300)
