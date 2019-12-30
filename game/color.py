class Color():
    '''the two colors of a standard playing card deck as full string literals'''
    colors=frozenset({'black', 'red'})

    def __init__(self, value: str):
        if not isinstance(value, str):
            raise TypeError('Color() value argument must be a string, not a '+str(type(value)))
        if value in Color.colors:
            self.value = value
        else:
            raise ValueError(value+' cannot be a Color')

    def __eq__(self, color) -> bool:
        if not isinstance(color, Color):
            raise TypeError('only a Color can be compared to a Color, not a '+str(type(color)))
        return self.value == color.value

    def __ne__(self, color) -> bool:
        return not self == color

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str('Color(\''+str(self.value)+'\')')
    
assert Color('black').value == 'black'
assert Color('red').value == 'red'
assert Color('black') == Color('black')
assert Color('black') != Color('red')
assert str(Color('black')) == 'black'
assert repr(Color('red')) == 'Color(\'red\')'
