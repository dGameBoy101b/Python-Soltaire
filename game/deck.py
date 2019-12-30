from solitaire.game.card_pile import CardPile
from solitaire.game.card import Card
from solitaire.extended_debug import random_test
import random

class Deck(CardPile):
    '''a standard deck of cards: initializes unshuffled'''
    suits=tuple(('spade', 'heart', 'club', 'diamond'))
    ranks=tuple(('ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king'))

    def add(self, card):
        CardPile.add(self, card, False)
        return self

    def __init__(self, init_cards: tuple = None):
        cards = []
        if init_cards == None:
            for suit in Deck.suits:
                for rank in Deck.ranks:
                    cards.append(Card(suit, rank, True))
        else:
            if not isinstance(init_cards, (tuple, list)):
                raise TypeError('Deck() init_cards argument must be a tuple or a list, not a '+str(type(init_cards)))
            for card in init_cards:
                if not isinstance(card, (Card, tuple)):
                    raise TypeError('Deck() init_cards argument must contain only Card or tuple types, not '+str(type(card)))
                if isinstance(card, tuple):
                    cards.append(Card(card[0], card[1]))
                else:
                    cards.append(Card(card.suit, card.rank))
        CardPile.__init__(self, *cards)

    def shuffle(self):
        '''shuffles the order of the deck'''
        random.shuffle(self.cards)
        return self  

    def deal(self, num: int = 1):
        '''returns cardpile taken from deck'''
        if not isinstance(num, int):
            raise TypeError('Deck.deal() num argument must be an integer, not a '+str(type(num)))
        cards = CardPile()
        while num > 0:
            card = self.take()
            cards.add(card)
            num -= 1
        return cards

    def __eq__(self, deck) -> bool:
        return self.cards == deck.cards

    def __ne__(self, deck) -> bool:
        return not self == deck

    def __str__(self) -> str:
        if len(self) > 0:
            return '**'
        else:
            return '[]'

    def __repr__(self) -> str:
        result = 'Deck('
        for card in self.cards:
            result += repr(card) + ','
        result = result.rstrip(',') + ')'
        return result
        
assert Deck().cards == [Card('spade', 'ace'), Card('spade', 'two'), Card('spade', 'three'), Card('spade', 'four'), Card('spade', 'five'), Card('spade', 'six'),
                        Card('spade', 'seven'), Card('spade', 'eight'), Card('spade', 'nine'), Card('spade', 'ten'), Card('spade', 'jack'), Card('spade', 'queen'),
                        Card('spade', 'king'), Card('heart', 'ace'), Card('heart', 'two'), Card('heart', 'three'), Card('heart', 'four'), Card('heart', 'five'),
                        Card('heart', 'six'), Card('heart', 'seven'), Card('heart', 'eight'), Card('heart', 'nine'), Card('heart', 'ten'), Card('heart', 'jack'),
                        Card('heart', 'queen'), Card('heart', 'king'), Card('club', 'ace'), Card('club', 'two'), Card('club', 'three'), Card('club', 'four'),
                        Card('club', 'five'), Card('club', 'six'), Card('club', 'seven'), Card('club', 'eight'), Card('club', 'nine'), Card('club', 'ten'),
                        Card('club', 'jack'), Card('club', 'queen'), Card('club', 'king'), Card('diamond', 'ace'), Card('diamond', 'two'), Card('diamond', 'three'),
                        Card('diamond', 'four'), Card('diamond', 'five'), Card('diamond', 'six'), Card('diamond', 'seven'), Card('diamond', 'eight'),
                        Card('diamond', 'nine'), Card('diamond', 'ten'), Card('diamond', 'jack'), Card('diamond', 'queen'), Card('diamond', 'king')]
assert Deck().deal() == CardPile(('diamond', 'king'))
assert Deck().deal(3) == CardPile(('diamond', 'king'), ('diamond', 'queen'), ('diamond', 'jack'))
assert random_test.possibleShuffle(Deck().cards,Deck().shuffle().cards)
assert repr(Deck((('spade', 'ace'), ('heart', 'two')))) == 'Deck(Card(Suit(\'spade\'),Rank(\'ace\'),True),Card(Suit(\'heart\'),Rank(\'two\'),True))'
assert str(Deck()) == '**'
assert str(Deck([])) == '[]'
