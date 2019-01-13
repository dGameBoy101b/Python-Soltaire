import random
class Color():
    '''the two colors of a standard playing card deck as full string literals'''
    colors=('black','red')
    def __init__(self,value):
        if Color.colors.count(value)>0:
            self.value=value
        else:
            raise Exception('invalid color')
    def __eq__(self,color):
        return self.value==color.value
    def __ne__(self,value):
        return not self==color.value
    assert Color('black').value=='black'
    assert Color('red').value=='red'
    assert Color('black')==Color('black')
    assert Color('black')!=Color('red')
class Suit():
    '''the four suits of a standard playing card deck as full string literals'''
    suits=('spade','heart','club','diamond')
    def __init__(self,value):
        if Suit.suits.count(value)>0:
            self.value=value
        else:
            raise Exception('invalid suit')
    def __eq__(self,suit):
        return self.value==suit.value
    def __ne__(self,suit):
        return not self==suit
    def color(self):
        if self.value=='spade' or self.value=='club':
            return Color('black')
        else:
            return Color('red')
    assert Suit('spade').value=='spade'
    assert Suit('heart').value=='heart'
    assert Suit('club').value=='club'
    assert Suit('diamond').value=='diamond'
    assert Suit('spade').color()==Color('black')
    assert Suit('heart').color()==Color('red')
    assert Suit('club')==Suit('club')
    assert Suit('diamond')!=Suit('heart')
class Rank():
    '''the thirteen suits of a standard playing card deck (Ace-low) as short string literals'''
    ranks=('A','2','3','4','5','6','7','8','9','10','J','Q','K')
    def __init__(self,value):
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
    def __le__(self,value):
        return self<rank or self==rank
    assert Rank('A').value=='A'
    assert Rank('7').value=='7'
    assert Rank('K')>Rank('A')
    assert Rank('10')<Rank('J')
    assert Rank('3')==Rank('3')
    assert Rank('5')!=Rank('9')
    assert Rank('4')>=Rank('2')
    assert Rank('6')<=Rank('6')
class Card():
    '''a standard playing card'''
    def __init__(self,suit,rank,facedown=True,hidden=None):
        self.suit=Suit(suit)
        self.rank=Rank(suit)
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
        if self.faceup:
            self.faceup=False
        else:
            self.faceup=True
    assert Card(Suit('spade'),Rank('A')).suit==Suit('spade')
    assert Card(Suit('heart'),Rank('2')).rank==Rank('2')
    assert Card(Suit('diamond'),Rank('5')).facedown==True
    assert Card(Suit('club'),Rank('10'),False).facedown==False
    assert Card(Suit('spade'),Rank('Q')).hidden==True
    assert Card(Suit('heart'),Rank('8'),False).hidden==False
    assert Card(Suit('diamond'),Rank('6'),True,False).hidden==False
class CardPile():
    '''an ordered pile of standard playing cards'''
    def __init__(self,*cards): 
        for card in cards:
            if not isinstance(card,Card):
                raise Exception('invalid card')
        self.cards=list(cards)
    def height(self):
        return len(self.cards)
    def add(self,card,totop=True):
        if not isinstance(card,Card):
            raise Exception('invalid card')
        if not isinstance(totop,bool):
            raise Exception('invalid totop')
        if totop:
            self.cards.append(card)
        else:
            self.cards.insert(0,card)
    def take(self,fromtop=True):
        if not isinstance(fromtop,bool):
            raise Exception('invalid fromtop')
        if fromtop:
            card=self.cards.pop()
        else:
            card=self.cards.pop(0)
        return card
class Deck(CardPile):
    '''a standard deck of cards'''
    suits=('spade','heart','club','diamond')
    ranks=('A','2','3','4','5','6','7','8','9','10','J','Q','K')
    def __init__(self):
        cards=[]
        for suit in Deck.suits:
            for rank in Deck.ranks:
                cards.append(Card(suit,rank))
        CardPile.__init__(cards)
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self,num=1):
        if not isinstance(num,int):
            raise Exception('invalid num')
        cards=CardPile()
        while num>0:
            card=self.take()
            cards.add(card)
            num-=1
        return cards
class BuildingPile(CardPile):
    '''piles for building cards in decending order alternating in color'''
    def topCard(self):
        return self.cards[self.height()-1]
    def stack(self,card):
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
class EndPile(CardPile):
    def __init__(self,suit):
        if suit=='spade' or suit=='heart' or suit=='club' or suit=='diamond'
    def topCard(self):
        return self.cards[self.height()-1]
    def stack(self,card):
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
