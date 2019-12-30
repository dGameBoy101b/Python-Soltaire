from solitaire.game.card_pile import CardPile, IllegalMove
from solitaire.game.card import Card
from solitaire.extended_debug import error_test

class BuildingPile(CardPile):
    '''piles for building cards in decending order, alternating in color'''

    def topCard(self) -> Card:
        '''returns top card of pile'''
        if len(self) > 0:
            return self.cards[-1]
        else:
            return None

    def take(self, n: int = 1):
        if not isinstance(n, int):
            raise TypeError('BulidingPile.take() n argument must be an integer, not a '+str(type(n)))
        if len(self) < 1:
            raise IllegalMove('an empty build pile cannot be taken from')
        num = 0
        for card in self:
            if not card.facedown:
                num += 1
        if n > num:
            raise IllegalMove('only faceup cards may be taken from a build pile')
        cards = CardPile()
        for i in range(n):
            cards.add(self.topCard(), False)
            self.cards.pop()
        if len(self) > 0 and self.topCard().facedown:
            self.topCard().flip()
        return cards        

    def stack(self, card: Card):
        '''attempts to legally stack given card'''
        if not isinstance(card, Card):
            raise TypeError('BuildingPile.stack() card argument must be a Card, not a '+str(type(card)))
        if len(self) < 1:
            if card.rank.value != 'king':
                raise IllegalMove('building piles must start stacking cards with a king')
        else:
            color = self.topCard().suit.color()
            if color == card.suit.color():
                raise IllegalMove('building piles must stack cards in alternating colors')
            rank = self.topCard().rank.value
            if rank == 'king' and card.rank.value == 'queen':
                pass
            elif rank == 'queen' and card.rank.value == 'jack':
                pass
            elif rank == 'jack' and card.rank.value == 'ten':
                pass
            elif rank == 'ten' and card.rank.value == 'nine':
                pass
            elif rank == 'nine' and card.rank.value == 'eight':
                pass
            elif rank == 'eight' and card.rank.value == 'seven':
                pass
            elif rank == 'seven' and card.rank.value == 'six':
                pass
            elif rank == 'six' and card.rank.value == 'five':
                pass
            elif rank == 'five' and card.rank.value == 'four':
                pass
            elif rank == 'four' and card.rank.value == 'three':
                pass
            elif rank == 'three' and card.rank.value == 'two':
                pass
            elif rank == 'two' and card.rank.value == 'ace':
                pass
            else:
                raise IllegalMove('building piles must stack cards in decending ranks')
        self.add(card)
        return self
    
assert BuildingPile(('spade', 'king', False)).stack(Card('heart', 'queen', False)) == BuildingPile(('spade', 'king', False), ('heart', 'queen', False))
assert BuildingPile(('diamond', 'six'), ('heart', 'eight'), ('club', 'ace')).topCard() == Card('club', 'ace')
assert error_test.expect('BuildingPile(("heart","king",False)).stack(Card("diamond","queen",False))', IllegalMove, global_variables=globals())
assert error_test.expect('BuildingPile(("spade","king",False)).stack(Card("diamond","three",False))', IllegalMove, global_variables=globals())
assert BuildingPile(('spade', 'three'), ('spade', 'king', False), ('heart', 'queen', False)).take(2) == CardPile(('spade', 'king', False), ('heart', 'queen', False))
assert error_test.expect("BuildingPile(('diamond','four'),('club','ace'),('club','ten',False)).take(2)", IllegalMove, global_variables=globals())
assert error_test.expect("BuildingPile().take()", IllegalMove, global_variables=globals())
