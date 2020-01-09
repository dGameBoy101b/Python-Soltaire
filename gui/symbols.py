from turtle import Turtle

def draw_diamond(rad: float, x: float = 0, y: float = 0, color = 'red') -> Turtle:
    '''draw a playing card diamond'''
    if isinstance(x, int):
        x = float(x)
    if not isinstance(x, float):
        raise TypeError('\'x\' must be a float, not a '+str(type(x)))
    if isinstance(y, int):
        y = float(y)
    if not isinstance(y, float):
        raise TypeError('\'y\' must be a float, not a '+str(type(y)))
    if isinstance(rad, int):
        rad = float(rad)
    if not isinstance(rad, float):
        raise TypeError('\'rad\' must be a float, not a '+str(type(rad)))
    if rad <= 0:
        raise ValueError('\'rad\' must be greater than 0, not '+str(rad))
    rat = 0.7
    t = Turtle(visible=False)
    t.color(color)
    t.penup()
    t.setpos(rad * rat + x, y)
    t.begin_fill()
    t.setpos(x, rad + y)
    t.setpos(x - rad * rat, y)
    t.setpos(x, y - rad)
    t.end_fill()
    return t

def draw_heart(rad: float, x: float = 0, y: float = 0, color = 'red') -> Turtle:
    '''draw a playing card heart'''
    if isinstance(x, int):
        x = float(x)
    if not isinstance(x, float):
        raise TypeError('\'x\' must be a float, not a '+str(type(x)))
    if isinstance(y, int):
        y = float(y)
    if not isinstance(y, float):
        raise TypeError('\'y\' must be a float, not a '+str(type(y)))
    if isinstance(rad, int):
        rad = float(rad)
    if not isinstance(rad, float):
        raise TypeError('\'rad\' must be a float, not a '+str(type(rad)))
    if rad <= 0:
        raise ValueError('\'rad\' must be greater than 0, not '+str(rad))
    t = Turtle(visible=False)
    t.color(color)
    t.penup()
    t.setpos(x, y + 0.5 * rad)
    t.setheading(90)
    t.begin_fill()
    t.circle(0.5 * rad, 200)
    t.setpos(x, y - rad)
    t.setpos(x, y + 0.5 * rad)
    t.setheading(90)
    t.circle(-0.5 * rad, 200)
    t.setpos(x, y - rad)
    t.end_fill()
    return t

def draw_club(rad: float, x: float = 0, y: float = 0, color = 'black') -> Turtle:
    '''draw a playing card club'''
    if isinstance(x, int):
        x = float(x)
    if not isinstance(x, float):
        raise TypeError('\'x\' must be a float, not a '+str(type(x)))
    if isinstance(y, int):
        y = float(y)
    if not isinstance(y, float):
        raise TypeError('\'y\' must be a float, not a '+str(type(y)))
    if isinstance(rad, int):
        rad = float(rad)
    if not isinstance(rad, float):
        raise TypeError('\'rad\' must be a float, not a '+str(type(rad)))
    if rad <= 0:
        raise ValueError('\'rad\' must be greater than 0, not '+str(rad))
    t = Turtle(visible=False)
    t.color(color)
    t.penup()
    t.setpos(x, y + rad)
    t.begin_fill()
    t.setheading(180)
    t.circle(0.45 * rad, 145)
    t.left(180)
    t.circle(0.45 * rad, 290)
    t.setheading(270)
    t.circle(-0.5 * rad, 90)
    t.setpos(x, t.pos()[1])
    t.setpos(x, y + rad)
    t.setheading(0)
    t.circle(-0.45 * rad, 145)
    t.left(180)
    t.circle(-0.45 * rad, 290)
    t.setheading(270)
    t.circle(0.5 * rad, 90)
    t.setpos(x, t.pos()[1])
    t.end_fill()
    return t

def draw_square(rad: float, x: float = 0, y: float = 0) -> Turtle:
    '''draw a square'''
    if isinstance(x, int):
        x = float(x)
    if not isinstance(x, float):
        raise TypeError('\'x\' must be a float, not a '+str(type(x)))
    if isinstance(y, int):
        y = float(y)
    if not isinstance(y, float):
        raise TypeError('\'y\' must be a float, not a '+str(type(y)))
    if isinstance(rad, int):
        rad = float(rad)
    if not isinstance(rad, float):
        raise TypeError('\'rad\' must be a float, not a '+str(type(rad)))
    if rad <= 0:
        raise ValueError('\'rad\' must be greater than 0, not '+str(rad))
    t = Turtle(visible=False)
    t.penup()
    t.setpos(x + rad, y + rad)
    t.pendown()
    t.setpos(x + rad, y - rad)
    t.setpos(x - rad, y - rad)
    t.setpos(x - rad, y + rad)
    t.setpos(x + rad, y + rad)
    return t

def draw_spade(rad: float, x: float = 0, y: float = 0, color = 'black') -> Turtle:
    '''draw a playing card spade'''
    if isinstance(x, int):
        x = float(x)
    if not isinstance(x, float):
        raise TypeError('\'x\' must be a float, not a '+str(type(x)))
    if isinstance(y, int):
        y = float(y)
    if not isinstance(y, float):
        raise TypeError('\'y\' must be a float, not a '+str(type(y)))
    if isinstance(rad, int):
        rad = float(rad)
    if not isinstance(rad, float):
        raise TypeError('\'rad\' must be a float, not a '+str(type(rad)))
    if rad <= 0:
        raise ValueError('\'rad\' must be greater than 0, not '+str(rad))
    t = Turtle(visible=False)
    t.color(color)
    t.penup()
    t.setpos(x, y - rad)
    t.begin_fill()
    t.setheading(180)
    t.forward(0.6 * rad)
    t.left(180)
    t.circle(0.5 * rad, 90)
    t.left(150)
    t.circle(-0.45 * rad, 200)
    t.setpos(x, y + rad)
    t.setpos(x, y - rad)
    t.setheading(0)
    t.forward(0.6 * rad)
    t.left(180)
    t.circle(-0.5 * rad, 90)
    t.right(150)
    t.circle(0.45 * rad, 200)
    t.setpos(x, y + rad)
    t.end_fill()
    return t

def draw_text(text: str, color, rad: float, x: float = 0, y: float = 0, align: str = 'center') -> Turtle:
    if not isinstance(text, str):
        raise TypeError('\'text\' must be a string, not a '+str(type(text)))
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
    if not isinstance(align, str):
        raise TypeError('\'align\' must be a string, not a '+str(type(align)))
    if len(text) < 1:
        raise ValueError('\'text\' must contain at least 1 character')
    if rad <= 0:
        raise ValueError('\'rad\' must be greater than 0, not '+str(rad))
    if not align in {'left', 'center', 'right'}:
        raise ValueError('\'align\' must be one of \'left\', \'center\', or \'right\', not '+str(align))
    t = Turtle(visible=False)
    t.color(color)
    t.penup()
    if align == 'left':
        t.setpos(x - rad, y - rad)
    elif align == 'right':
        t.setpos(x + rad, y - rad)
    else:
        t.setpos(x, y - rad)
    t.write(text, align=align, font=('Arial', int(rad * 1.5), 'normal'))
    return t

if __name__ == '__main__':
    draw_square(100, -100, 100)
    draw_spade(100, -100, 100)
    
    draw_square(100, 100, 100)
    draw_heart(100, 100, 100)
    
    draw_square(100, -100, -100)
    draw_club(100, -100, -100)
    
    draw_square(100, 100, -100)
    draw_diamond(100, 100, -100)
    
    draw_square(100, -300, 0)
    draw_text('A', 'black', 100, -300, 0)
    
    draw_square(100, 300, 0)
    draw_text('y', 'red', 100, 300, 0)
