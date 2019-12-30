class Rank():
    '''the thirteen suits of a standard playing card deck (Ace-low) as short string literals'''
    ranks = ('ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king')
    shorthand = dict({'ace':'A', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', 'ten':'10', 'jack':'J','queen':'Q', 'king':'K'})
    longhand = dict({'A':'ace', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '10':'ten', 'J':'jack', 'Q':'queen', 'K':'king'})

    def __init__(self, value: str):
        if not isinstance(value, str):
            raise TypeError('Rank() value argument must be a string, not a '+str(type(value)))
        if value in Rank.shorthand:
            self.value = value
        elif value in Rank.longhand:
            self.value = Rank.longhand[value]
        else:
            raise ValueError(value+' is not a Rank')

    def __eq__(self, rank) -> bool:
        if not isinstance(rank, (Rank, str)):
            raise TypeError('only a Rank can be compared to a Rank, not a '+str(type(rank)))
        if isinstance(rank, str):
            rank = Rank(rank)
        return Rank.ranks.index(self.value) == Rank.ranks.index(rank.value)

    def __ne__(self, rank) -> bool:
        return not self == rank

    def __gt__(self, rank) -> bool:
        if not isinstance(rank, (Rank, str)):
            raise TypeError('only a Rank can be compared to a Rank, not a '+str(type(rank)))
        if isinstance(rank, str):
            rank = Rank(rank)
        return Rank.ranks.index(self.value) > Rank.ranks.index(rank.value)

    def __lt__(self, rank) -> bool:
        if not isinstance(rank, (Rank, str)):
            raise TypeError('only a Rank can be compared to a Rank, not a '+str(type(rank)))
        if isinstance(rank, str):
            rank = Rank(rank)
        return Rank.ranks.index(self.value) < Rank.ranks.index(rank.value)

    def __ge__(self,rank) -> bool:
        return self > rank or self == rank

    def __le__(self, rank) -> bool:
        return self < rank or self == rank

    def __str__(self) -> str:
        return str(Rank.shorthand[self.value])

    def __repr__(self) -> str:
        return str('Rank(\''+str(self.value)+'\')')
    
assert Rank('ace').value == 'ace'
assert Rank('seven').value == 'seven'
assert Rank('king') > Rank('ace')
assert Rank('ten') < Rank('jack')
assert Rank('three') == Rank('three')
assert Rank('five') != Rank('nine')
assert Rank('four') >= Rank('two')
assert Rank('six') <= Rank('six')
assert str(Rank('queen')) == 'Q'
assert repr(Rank('two')) == 'Rank(\'two\')'
