import random
class Color():
    '''the two colors of a standard playing card deck as full string literals'''
    colors=frozenset({'black','red'})
    def __init__(self,value:str):
        if value in Color.colors:
            self.value=value
        else:
            raise Exception('invalid color')
    def __eq__(self,color):
        return self.value==color.value
    def __ne__(self,color):
        return not self==color
    def display(self)->str:
        '''returns human-readable representation'''
        return str(self.value)
assert Color('black').value=='black'
assert Color('red').value=='red'
assert Color('black')==Color('black')
assert Color('black')!=Color('red')
assert Color('black').display()=='black'

class Suit():
    '''the four suits of a standard playing card deck as full string literals'''
    suits=frozenset({'spade','heart','club','diamond'})
    shorthand=dict({'spade':'s','heart':'h','club':'c','diamond':'d'})
    def __init__(self,value:str):
        if value in Suit.suits:
            self.value=value
        else:
            raise Exception('invalid suit')
    def __eq__(self,suit):
        return self.value==suit.value
    def __ne__(self,suit):
        return not self==suit
    def color(self):
        '''determines color of suit'''
        if self.value=='spade' or self.value=='club':
            return Color('black')
        else:
            return Color('red')
    def display(self,short=True):
        '''returns human-readable representation'''
        if short:
            return str(Suit.shorthand[self.value])
        else:
            return str(self.value)
assert Suit('spade').value=='spade'
assert Suit('heart').value=='heart'
assert Suit('club').value=='club'
assert Suit('diamond').value=='diamond'
assert Suit('spade').color()==Color('black')
assert Suit('heart').color()==Color('red')
assert Suit('club')==Suit('club')
assert Suit('diamond')!=Suit('heart')
assert Suit('spade').display()=='s'
assert Suit('heart').display(False)=='heart'

class Rank():
    '''the thirteen suits of a standard playing card deck (Ace-low) as short string literals'''
    ranks=tuple(('A','2','3','4','5','6','7','8','9','10','J','Q','K'))
    def __init__(self,value:str):
        if Rank.ranks.count(value)>0:
            self.value=value
        else:
            raise Exception('invalid rank')
    def __eq__(self,rank):
        return Rank.ranks.index(self.value)==Rank.ranks.index(rank.value)
    def __ne__(self,rank):
        return not self==rank
    def __gt__(self,rank):
        return Rank.ranks.index(self.value)>Rank.ranks.index(rank.value)
    def __lt__(self,rank):
        return Rank.ranks.index(self.value)<Rank.ranks.index(rank.value)
    def __ge__(self,rank):
        return self>rank or self==rank
    def __le__(self,rank):
        return self<rank or self==rank
    def display(self):
        '''returns human-readable representation'''
        return str(self.value)
assert Rank('A').value=='A'
assert Rank('7').value=='7'
assert Rank('K')>Rank('A')
assert Rank('10')<Rank('J')
assert Rank('3')==Rank('3')
assert Rank('5')!=Rank('9')
assert Rank('4')>=Rank('2')
assert Rank('6')<=Rank('6')
assert Rank('Q').display()=='Q'

class Card():
    '''a standard playing card'''
    def __init__(self,suit:str,rank:str,facedown:bool=True,hidden:bool=None):
        self.suit=Suit(suit)
        self.rank=Rank(rank)
        if isinstance(facedown,bool):
            self.facedown=facedown
        else:
            raise Exception('invalid faceup')
        if hidden==None:
            self.hidden=facedown
        elif isinstance(hidden,bool):
            self.hidden=hidden
        else:
            raise Exception('invalid hidden')
    def __eq__(self,card):
        return self.suit==card.suit and self.rank==card.rank
    def __ne__(self,card):
        return not self==card
    def flip(self):
        '''toggles between faceup and facedown'''
        self.facedown=not self.facedown
        if __debug__:
            return self
    def display(self,short:bool=True) -> str:
        '''returns human-readable representation'''
        if self.hidden:
            return '**'
        elif short:
            return str(str(self.suit.display())+str(self.rank.display()))
        else:
            return str('('+str(self.suit.display(False))+','+str(self.rank.display())+')')
assert Card('spade','A').suit==Suit('spade')
assert Card('heart','2').rank==Rank('2')
assert Card('diamond','5').facedown==True
assert Card('club','10',False).facedown==False
assert Card('spade','Q').hidden==True
assert Card('heart','8',False).hidden==False
assert Card('diamond','6',True,False).hidden==False
assert Card('club','3').flip()==Card('club','3',False)
assert Card('heart','K',False).flip()==Card('heart','K',True)
assert Card('spade','7').display()=='**'
assert Card('heart','3',False).display()=='h3'
assert Card('diamond','A',False).display(False)=='(diamond,A)'

class CardPile():
    '''an ordered pile of standard playing cards'''
    def __init__(self,*cards): 
        for card in cards:
            if not isinstance(card,(tuple,Card)):
                raise Exception(str(card)+' invalid card')
        self.cards=[]
        for card in cards:
            if isinstance(card, tuple):
                self.cards.append(Card(*card))
            else:
                self.cards.append(card)
    def height(self)->int:
        '''returns number of cards in pile'''
        return len(self.cards)
    def display(self,short:bool=True)->str:
        '''returns human-readable representation'''
        if short:
            display=''
            for card in self.cards:
                display+=card.display()+','
            return display[0:-1]
        else:
            display='('
            for card in self.cards:
                 display+=card.display(False)+','
            return display[0:-1]+')'
    def add(self,card,totop=True):
        '''adds card to pile'''
        if not isinstance(card,(tuple,Card)):
            raise Exception(str(card)+' invalid card')
        if isinstance(card,tuple):
            card=Card(*card)
        if not isinstance(totop,bool):
            raise Exception('invalid totop')
        if totop:
            self.cards.append(card)
        else:
            self.cards.insert(0,card)
        if __debug__:
            return self
    def take(self,fromtop=True):
        '''removes card from pile and returns it'''
        if not isinstance(fromtop,bool):
            raise Exception('invalid fromtop')
        if self.height()<1:
            raise Exception('no cards to take')
        if fromtop:
            card=self.cards.pop()
        else:
            card=self.cards.pop(0)
        if __debug__:
            return (card,self)
        else:
            return card
    def __eq__(self,cardpile)->bool:
        return self.cards==cardpile.cards
    def __ne__(self,cardpile)->bool:
        return not self==cardpile
assert CardPile().height()==0
assert CardPile(('spade','A')).height()==1
assert CardPile(('heart','4'),('diamond','7')).height()==2
assert CardPile(('diamond','2',False)).add(('club','10',False))==CardPile(('diamond','2',False),('club','10',False))
assert CardPile(('spade','Q')).add(('heart','7'),False)==CardPile(('heart','7'),('spade','Q'))
assert CardPile(('club','9')).take()[1].height()==0
assert CardPile(('spade','3'),('diamond','J')).take()[0]==Card('diamond','J')
assert CardPile(('heart','8'),('spade','7')).take(False)[0]==Card('heart','8')

class Deck(CardPile):
    '''a standard deck of cards: initializes unshuffled'''
    suits=tuple(('spade','heart','club','diamond'))
    ranks=tuple(('A','2','3','4','5','6','7','8','9','10','J','Q','K'))
    def __init__(self):
        cards=[]
        for suit in Deck.suits:
            for rank in Deck.ranks:
                cards.append(Card(Suit(suit),Rank(rank)))
        CardPile.__init__(cards)
    def shuffle(self):
        '''shuffles the order of the deck'''
        random.shuffle(self.cards)
        if __debug__:
            return self
    def deal(self,num:int=1):
        '''returns cardpile taken from deck'''
        if not isinstance(num,int):
            raise Exception('invalid num')
        cards=CardPile()
        while num>0:
            card=self.take()
            cards.add(card)
            num-=1
        if __debug__:
            return (cards,self)
        else:
            return cards
    def __eq__(self,deck):
        return self.cards==deck.cards
    def __ne__(self,deck):
        return not self==deck
assert Deck().cards==[Card('spade','A'),Card('spade','2'),Card('spade','3'),Card('spade','4'),Card('spade','5'),Card('spade','6'),Card('spade','7'),Card('spade','8'),Card('spade','9'),Card('spade','10'),Card('spade','J'),Card('spade','Q'),Card('spade','K'),
                      Card('heart','A'),Card('heart','2'),Card('heart','3'),Card('heart','4'),Card('heart','5'),Card('heart','6'),Card('heart','7'),Card('heart','8'),Card('heart','9'),Card('heart','10'),Card('heart','J'),Card('heart','Q'),Card('heart','K'),
                      Card('club','A'),Card('club','2'),Card('club','3'),Card('club','4'),Card('club','5'),Card('club','6'),Card('club','7'),Card('club','8'),Card('club','9'),Card('club','10'),Card('club','J'),Card('club','Q'),Card('club','K'),
                      Card('diamond','A'),Card('diamond','2'),Card('diamond','3'),Card('diamond','4'),Card('diamond','5'),Card('diamond','6'),Card('diamond','7'),Card('diamond','8'),Card('diamond','9'),Card('diamond','10'),Card('diamond','J'),Card('diamond','Q'),Card('diamond','K')]
assert Deck().deal()[0]==CardPile(('spade','A'))
assert Deck().deal(3)[0]==CardPile(('spade','A'),('spade','2'),('spade','3'))
assert Deck().deal(50)[1]==CardPile(('diamond','Q'),('diamond','K'))
assert Deck().shuffle()!=Deck()

class BuildingPile(CardPile):
    '''piles for building cards in decending order alternating in color'''
    def topCard(self):
        '''returns top card of pile'''
        return self.cards[self.height()-1]
    def stack(self,card):
        '''attempts to legally stack given card'''
        if not isinstance(card,Card):
            raise Exception('invalid card')
        color=self.topCard().color
        if color==card.color:
            raise Exception('invalid color')
        rank=self.topCard().rank
        if rank=='K' and card.rank=='Q':
            pass
        elif rank=='Q' and card.rank=='J':
            pass
        elif rank=='J' and card.rank=='10':
            pass
        elif rank=='10' and card.rank=='9':
            pass
        elif rank=='9' and card.rank=='8':
            pass
        elif rank=='8' and card.rank=='7':
            pass
        elif rank=='7' and card.rank=='6':
            pass
        elif rank=='6' and card.rank=='5':
            pass
        elif rank=='5' and card.rank=='4':
            pass
        elif rank=='4' and card.rank=='3':
            pass
        elif rank=='3' and card.rank=='2':
            pass
        elif rank=='2' and card.rank=='A':
            pass
        else:
            raise Exception('invalid rank')
        self.add(card)
        return self
assert BuildingPile(('spade','K',False)).stack(Card('heart','Q',False))==BuildingPile(('spade','K',False),('heart','Q',False))
assert BuildingPile(('diamond','6'),('heart','8'),('club','A')).topCard()==Card('club','A')

class EndPile(CardPile):
    def __init__(self,suit):
        self.suit=Suit(suit)
        CardPile.__init__()
    def topCard(self):
        '''returns top card of pile'''
        return self.cards[self.height()-1]
    def stack(self,card):
        '''attempts to legally stack given card'''
        if not isinstance(card,Card):
            raise Exception('invalid card')
        if self.suit!=card.suit:
            raise Exception('invalid suit')
        rank=self.topCard().rank
        if rank=='A' and card.rank=='2':
            pass
        elif rank=='2' and card.rank=='3':
            pass
        elif rank=='3' and card.rank=='4':
            pass
        elif rank=='4' and card.rank=='5':
            pass
        elif rank=='5' and card.rank=='6':
            pass
        elif rank=='6' and card.rank=='7':
            pass
        elif rank=='7' and card.rank=='8':
            pass
        elif rank=='8' and card.rank=='9':
            pass
        elif rank=='9' and card.rank=='10':
            pass
        elif rank=='10' and card.rank=='J':
            pass
        elif rank=='J' and card.rank=='Q':
            pass
        elif rank=='Q' and card.rank=='K':
            pass
        else:
            raise Exception('invalid rank')
        self.add(card)
        return self

class DiscardPile(CardPile):
    def topCard(self):
        return self.cards[self.height()-1]
    def reset(self):
        cards=self.cards
        self.cards=[]
        return cards
