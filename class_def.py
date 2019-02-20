import random
from extended_debug import error_test,random_test
class IllegalMove(Exception):
    '''attempted action breaks the rules of solitaire'''

class Unavailable(Exception):
    '''command cannot be executed in current context'''
        
class Color():
    '''the two colors of a standard playing card deck as full string literals'''
    colors=frozenset({'black','red'})
    def __init__(self,value:str):
        if not isinstance(value,str):
            raise TypeError('Color() value argument must be a string, not a '+str(type(value)))
        if value in Color.colors:
            self.value=value
        else:
            raise ValueError(value+' cannot be a Color')
    def __eq__(self,color)->bool:
        if not isinstance(color,Color):
            raise TypeError('only a Color can be compared to a Color, not a '+str(type(value)))
        return self.value==color.value
    def __ne__(self,color)->bool:
        return not self==color
    def __str__(self)->str:
        return str(self.value)
    def __repr__(self)->str:
        return str('Color(\''+str(self.value)+'\')')
assert Color('black').value=='black'
assert Color('red').value=='red'
assert Color('black')==Color('black')
assert Color('black')!=Color('red')
assert str(Color('black'))=='black'
assert repr(Color('red'))=='Color(\'red\')'

class Suit():
    '''the four suits of a standard playing card deck as full string literals'''
    suits=frozenset({'spade','heart','club','diamond'})
    shorthand={'spade':'s','heart':'h','club':'c','diamond':'d'}
    longhand={'s':'spade','h':'heart','c':'club','d':'diamond'}
    def __init__(self,value:str):
        if not isinstance(value,str):
            raise TypeError('Suit() value argument must be a string, not a '+str(type(value)))
        if value in Suit.shorthand:
            self.value=value
        elif value in Suit.longhand:
            self.value=Suit.longhand[value]
        else:
            raise ValueError(value+' is not a Suit')
    def __hash__(self):
        return id(self)
    def __eq__(self,suit)->bool:
        if not isinstance(suit,Suit):
            raise TypeError('only a Suit can be compared to a Suit, not a '+str(type(value)))
        return self.value==suit.value
    def __ne__(self,suit)->bool:
        return not self==suit
    def color(self):
        '''determines color of suit'''
        if self.value=='spade' or self.value=='club':
            return Color('black')
        else:
            return Color('red')
    def __str__(self)->str:
        return str(Suit.shorthand[self.value])
    def __repr__(self)->str:
        return str('Suit(\''+str(self.value)+'\')')
assert Suit('spade').value=='spade'
assert Suit('heart').value=='heart'
assert Suit('club').value=='club'
assert Suit('diamond').value=='diamond'
assert Suit('spade').color()==Color('black')
assert Suit('heart').color()==Color('red')
assert Suit('club')==Suit('club')
assert Suit('diamond')!=Suit('heart')
assert str(Suit('spade'))=='s'
assert repr(Suit('heart'))=='Suit(\'heart\')'

class Rank():
    '''the thirteen suits of a standard playing card deck (Ace-low) as short string literals'''
    ranks=('ace','two','three','four','five','six','seven','eight','nine','ten','jack','queen','king')
    shorthand=dict({'ace':'A','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','ten':'10','jack':'J','queen':'Q','king':'K'})
    longhand=dict({'A':'ace','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','10':'ten','J':'jack','Q':'queen','K':'king'})
    def __init__(self,value:str):
        if not isinstance(value,str):
            raise TypeError('Rank() value argument must be a string, not a '+str(type(value)))
        if value in Rank.shorthand:
            self.value=value
        elif value in Rank.longhand:
            self.value=Rank.longhand[value]
        else:
            raise ValueError(value+' is not a Rank')
    def __eq__(self,rank)->bool:
        if not isinstance(rank,(Rank,str)):
            raise TypeError('only a Rank can be compared to a Rank, not a '+str(type(rank)))
        if isinstance(rank,str):
            rank=Rank(rank)
        return Rank.ranks.index(self.value)==Rank.ranks.index(rank.value)
    def __ne__(self,rank)->bool:
        return not self==rank
    def __gt__(self,rank)->bool:
        if not isinstance(rank,(Rank,str)):
            raise TypeError('only a Rank can be compared to a Rank, not a '+str(type(rank)))
        if isinstance(rank,str):
            rank=Rank(rank)
        return Rank.ranks.index(self.value)>Rank.ranks.index(rank.value)
    def __lt__(self,rank)->bool:
        if not isinstance(rank,(Rank,str)):
            raise TypeError('only a Rank can be compared to a Rank, not a '+str(type(rank)))
        if isinstance(rank,str):
            rank=Rank(rank)
        return Rank.ranks.index(self.value)<Rank.ranks.index(rank.value)
    def __ge__(self,rank)->bool:
        return self>rank or self==rank
    def __le__(self,rank)->bool:
        return self<rank or self==rank
    def __str__(self)->str:
        return str(Rank.shorthand[self.value])
    def __repr__(self)->str:
        return str('Rank(\''+str(self.value)+'\')')
assert Rank('ace').value=='ace'
assert Rank('seven').value=='seven'
assert Rank('king')>Rank('ace')
assert Rank('ten')<Rank('jack')
assert Rank('three')==Rank('three')
assert Rank('five')!=Rank('nine')
assert Rank('four')>=Rank('two')
assert Rank('six')<=Rank('six')
assert str(Rank('queen'))=='Q'
assert repr(Rank('two'))=='Rank(\'two\')'

class Card():
    '''a standard playing card'''
    def __init__(self,suit:str,rank:str,facedown:bool=True):
        if not isinstance(suit,(str,Suit)):
            raise TypeError('Card() suit argument must be a string or a Suit, not a '+str(type(suit)))
        if isinstance(suit,str):
            self.suit=Suit(suit)
        else:
            self.suit=suit
        if not isinstance(rank,(str,Rank)):
            raise TypeError('Card() rank argument must be a string or a Rank, not a '+str(type(rank)))
        if isinstance(rank,str):
            self.rank=Rank(rank)
        else:
            self.rank=rank
        if isinstance(facedown,bool):
            self.facedown=facedown
        else:
            raise TypeError('Card() facedown argument must be a boolean, not a '+str(type(facedown)))
    def __hash__(self):
        return id(self)
    def __eq__(self,card)->bool:
        return self.suit==card.suit and self.rank==card.rank and self.facedown==card.facedown
    def __ne__(self,card)->bool:
        return not self==card
    def flip(self,link:bool=False):
        '''toggles between faceup and facedown'''
        self.facedown=not self.facedown
        if link:
            self.hidden=self.facedown
        return self
    def __str__(self)->str:
        if self.facedown:
            return '**'
        else:
            return str(str(self.suit)+str(self.rank))
    def __repr__(self):
        return str('Card('+repr(self.suit)+','+repr(self.rank)+','+str(self.facedown)+')')
assert Card('spade','ace').suit==Suit('spade')
assert Card('heart','two').rank==Rank('two')
assert Card('diamond','five').facedown==True
assert Card('club','ten',False).facedown==False
assert Card('club','three').flip()==Card('club','three',False)
assert Card('heart','king',False).flip()==Card('heart','king',True)
assert str(Card('spade','seven'))=='**'
assert str(Card('heart','three',False))=='h3'
assert repr(Card('diamond','ace'))=='Card(Suit(\'diamond\'),Rank(\'ace\'),True)'
assert repr(Card('club','five',False))=='Card(Suit(\'club\'),Rank(\'five\'),False)'

class CardPile():
    '''an ordered pile of standard playing cards'''
    def __init__(self,*cards:tuple):
        for card in cards:
            if not isinstance(card,(tuple,Card)):
                raise TypeError('each item in CardPile() *cards argument must be a Card or tuple, not a '+str(type(card)))
        self.cards=[]
        for card in cards:
            if isinstance(card, tuple):
                self.cards.append(Card(*card))
            else:
                self.cards.append(card)
    def __len__(self)->int:
        return len(self.cards)
    def __repr__(self):
        display='CardPile('
        if len(self)>0:
            for card in self.cards:
                display+=repr(card)+','
            return display[0:-1]+')'
        else:
            return display+')'
    def __str__(self)->str:
        if len(self)>0:
            display=''
            for card in self.cards:
                display+=str(card)+','
            return display[0:-1]
        else:
            return '[]'
    def add(self,card,totop=True):
        '''adds card to pile'''
        if not isinstance(card,(tuple,Card)):
            raise TypeError('CardPile.add() card argument must be a Card or a tuple, not a '+str(type(card)))
        if isinstance(card,tuple):
            card=Card(*card)
        if not isinstance(totop,bool):
            raise TypeError('CardPile.add() card argument must be a boolean, not a '+str(type(totop)))
        if totop:
            self.cards.append(card)
        else:
            self.cards.insert(0,card)
        return self
    def take(self,fromtop=True)->Card:
        '''removes card from pile and returns it'''
        if not isinstance(fromtop,bool):
            raise TypeError('CardPile.take() fromtop argument must be a boolean, not a '+str(type(fromtop)))
        if len(self)<1:
            raise IllegalMove('CardPile must contain at least one Card to use .take()')
        if fromtop:
            card=self.cards.pop()
        else:
            card=self.cards.pop(0)
        return card
    def __eq__(self,cardpile)->bool:
        return self.cards==cardpile.cards
    def __ne__(self,cardpile)->bool:
        return not self==cardpile
    def __contains__(self,card:Card)->bool:
        return card in self.cards
    def __iter__(self):
        return iter(self.cards)
assert len(CardPile())==0
assert len(CardPile(('spade','ace')))==1
assert len(CardPile(('heart','four'),('diamond','seven')))==2
assert CardPile(('diamond','two',False)).add(('club','ten',False))==CardPile(('diamond','two',False),('club','ten',False))
assert CardPile(('spade','queen')).add(('heart','seven'),False)==CardPile(('heart','seven'),('spade','queen'))
assert CardPile(('spade','three'),('diamond','jack')).take()==Card('diamond','jack')
assert CardPile(('heart','eight'),('spade','seven')).take(False)==Card('heart','eight')
assert repr(CardPile())=='CardPile()'
assert repr(CardPile(('spade','ace'),('heart','two')))=='CardPile(Card(Suit(\'spade\'),Rank(\'ace\'),True),Card(Suit(\'heart\'),Rank(\'two\'),True))'
assert str(CardPile())=='[]'
assert str(CardPile(('heart','four')))=='**'
assert str(CardPile(('diamond','king',False),('club','seven',False)))=='dK,c7'

class Deck(CardPile):
    '''a standard deck of cards: initializes unshuffled'''
    suits=tuple(('spade','heart','club','diamond'))
    ranks=tuple(('ace','two','three','four','five','six','seven','eight','nine','ten','jack','queen','king'))
    def add(self,card):
        CardPile.add(self,card,False)
        return self
    def __init__(self,init_cards:tuple=None):
        cards=[]
        if init_cards==None:
            for suit in Deck.suits:
                for rank in Deck.ranks:
                    cards.append(Card(suit,rank,True))
        else:
            if not isinstance(init_cards,(tuple,list)):
                raise TypeError('Deck() init_cards argument must be a tuple or a list, not a '+str(type(init_cards)))
            for card in init_cards:
                if not isinstance(card,(Card,tuple)):
                    raise TypeError('Deck() init_cards argument must contain only Card or tuple types, not '+str(type(card)))
                if isinstance(card,tuple):
                    cards.append(Card(card[0],card[1]))
                else:
                    cards.append(Card(card.suit,card.rank))
        CardPile.__init__(self,*cards)
    def shuffle(self):
        '''shuffles the order of the deck'''
        random.shuffle(self.cards)
        return self  
    def deal(self,num:int=1):
        '''returns cardpile taken from deck'''
        if not isinstance(num,int):
            raise TypeError('Deck.deal() num argument must be an integer, not a '+str(type(num)))
        cards=CardPile()
        while num>0:
            card=self.take()
            cards.add(card)
            num-=1
        return cards
    def __eq__(self,deck)->bool:
        return self.cards==deck.cards
    def __ne__(self,deck)->bool:
        return not self==deck
    def __str__(self)->str:
        if len(self)>0:
            return '**'
        else:
            return '[]'
    def __repr__(self)->str:
        result='Deck('
        for card in self.cards:
            result+=repr(card)+','
        result=result.rstrip(',')+')'
        return result
        
assert Deck().cards==[Card('spade','ace'),Card('spade','two'),Card('spade','three'),Card('spade','four'),Card('spade','five'),Card('spade','six'),Card('spade','seven'),Card('spade','eight'),Card('spade','nine'),Card('spade','ten'),Card('spade','jack'),Card('spade','queen'),Card('spade','king'),Card('heart','ace'),Card('heart','two'),Card('heart','three'),Card('heart','four'),Card('heart','five'),Card('heart','six'),Card('heart','seven'),Card('heart','eight'),Card('heart','nine'),Card('heart','ten'),Card('heart','jack'),Card('heart','queen'),Card('heart','king'),Card('club','ace'),Card('club','two'),Card('club','three'),Card('club','four'),Card('club','five'),Card('club','six'),Card('club','seven'),Card('club','eight'),Card('club','nine'),Card('club','ten'),Card('club','jack'),Card('club','queen'),Card('club','king'),Card('diamond','ace'),Card('diamond','two'),Card('diamond','three'),Card('diamond','four'),Card('diamond','five'),Card('diamond','six'),Card('diamond','seven'),Card('diamond','eight'),Card('diamond','nine'),Card('diamond','ten'),Card('diamond','jack'),Card('diamond','queen'),Card('diamond','king')]
assert Deck().deal()==CardPile(('diamond','king'))
assert Deck().deal(3)==CardPile(('diamond','king'),('diamond','queen'),('diamond','jack'))
assert random_test.possibleShuffle(Deck().cards,Deck().shuffle().cards)
assert repr(Deck((('spade','ace'),('heart','two'))))=='Deck(Card(Suit(\'spade\'),Rank(\'ace\'),True),Card(Suit(\'heart\'),Rank(\'two\'),True))'
assert str(Deck())=='**'
assert str(Deck([]))=='[]'

class BuildingPile(CardPile):
    '''piles for building cards in decending order, alternating in color'''
    def topCard(self)->Card:
        '''returns top card of pile'''
        if len(self)>0:
            return self.cards[len(self)-1]
        else:
            return None
    def take(self,n:int=1):
        if not isinstance(n,int):
            raise TypeError('BulidingPile.take() n argument must be an integer, not a '+str(type(n)))
        if len(self)<1:
            raise IllegalMove('an empty build pile cannot be taken from')
        num=0
        for card in self:
            if not card.facedown:
                num+=1
        if n>num:
            raise IllegalMove('only faceup cards may be taken from a build pile')
        cards=CardPile()
        for i in range(n):
            cards.add(self.topCard(),False)
            self.cards.pop()
        if len(self)>0 and self.topCard().facedown:
            self.topCard().flip()
        return cards        
    def stack(self,card:Card):
        '''attempts to legally stack given card'''
        if not isinstance(card,Card):
            raise TypeError('BuildingPile.stack() card argument must be a Card, not a '+str(type(card)))
        color=self.topCard().suit.color()
        if color==card.suit.color():
            raise IllegalMove('building piles must stack cards in alternating colors')
        rank=self.topCard().rank.value
        if rank=='king' and card.rank.value=='queen':
            pass
        elif rank=='queen' and card.rank.value=='jack':
            pass
        elif rank=='jack' and card.rank.value=='ten':
            pass
        elif rank=='ten' and card.rank.value=='nine':
            pass
        elif rank=='nine' and card.rank.value=='eight':
            pass
        elif rank=='eight' and card.rank.value=='seven':
            pass
        elif rank=='seven' and card.rank.value=='six':
            pass
        elif rank=='six' and card.rank.value=='five':
            pass
        elif rank=='five' and card.rank.value=='four':
            pass
        elif rank=='four' and card.rank.value=='three':
            pass
        elif rank=='three' and card.rank.value=='two':
            pass
        elif rank=='two' and card.rank.value=='ace':
            pass
        else:
            raise IllegalMove('euilding piles must stack cards in decending ranks')
        self.add(card)
        return self
assert BuildingPile(('spade','king',False)).stack(Card('heart','queen',False))==BuildingPile(('spade','king',False),('heart','queen',False))
assert BuildingPile(('diamond','six'),('heart','eight'),('club','ace')).topCard()==Card('club','ace')
assert error_test.expect('BuildingPile(("heart","king",False)).stack(Card("diamond","queen",False))',IllegalMove,global_variables={'IllegalMove':IllegalMove,'BuildingPile':BuildingPile,'CardPile':CardPile,'Card':Card,'Rank':Rank,'Suit':Suit,'Color':Color})
assert error_test.expect('BuildingPile(("spade","king",False)).stack(Card("diamond","three",False))',IllegalMove,global_variables={'IllegalMove':IllegalMove,'BuildingPile':BuildingPile,'CardPile':CardPile,'Card':Card,'Rank':Rank,'Suit':Suit,'Color':Color})
assert BuildingPile(('spade','three'),('spade','king',False),('heart','queen',False)).take(2)==CardPile(('spade','king',False),('heart','queen',False))
assert error_test.expect("BuildingPile(('diamond','four'),('club','ace'),('club','ten',False)).take(2)",IllegalMove,global_variables={'IllegalMove':IllegalMove,'BuildingPile':BuildingPile,'CardPile':CardPile,'Card':Card,'Rank':Rank,'Suit':Suit,'Color':Color})
assert error_test.expect("BuildingPile().take()",IllegalMove,global_variables={'BuildingPile':BuildingPile,'CardPile':CardPile,'Card':Card,'Rank':Rank,'Suit':Suit,'Color':Color})

class EndPile(CardPile):
    '''piles for submitting cards of the same suit, in ascending order'''
    def __init__(self,suit,*cards):
        self.suit=Suit(suit)
        CardPile.__init__(self,*cards)
    def topCard(self)->Card:
        '''returns top card of pile'''
        return self.cards[len(self)-1]
    def stack(self,card:Card):
        '''attempts to legally stack given card'''
        if not isinstance(card,(tuple,Card)):
            raise TypeError('EndPile.stack() card argument must be a Card or tuple, not a '+str(type(card)))
        if isinstance(card,tuple):
            card=Card(*card)
        if self.suit!=card.suit:
            raise IllegalMove('end piles must stack cards of the same suit')
        if len(self)>0:
            rank=self.topCard().rank.value
            if rank=='ace' and card.rank.value=='two':
                pass
            elif rank=='two' and card.rank.value=='three':
                pass
            elif rank=='three' and card.rank.value=='four':
                pass
            elif rank=='four' and card.rank.value=='five':
                pass
            elif rank=='five' and card.rank.value=='six':
                pass
            elif rank=='six' and card.rank.value=='seven':
                pass
            elif rank=='seven' and card.rank.value=='eight':
                pass
            elif rank=='eight' and card.rank.value=='nine':
                pass
            elif rank=='nine' and card.rank.value=='ten':
                pass
            elif rank=='ten' and card.rank.value=='jack':
                pass
            elif rank=='jack' and card.rank.value=='queen':
                pass
            elif rank=='queen' and card.rank.value=='king':
                pass
            else:
                raise IllegalMove('end piles must stack cards in ascending rank')
        elif card.rank.value=='ace':
            pass
        else:
            raise IllegalMove('end piles must stack \'ace\' ranked cards first')
        self.add(Card(card.suit,card.rank,False))
        return self
    def __repr__(self):
        display='EndPile('+repr(self.suit)+','
        for card in self.cards:
            display+=repr(card)+','
        return display[0:-1]+')'
    def __str__(self):
        if len(self)>0:
            return str(self.topCard())
        else:
            return '[]'
assert len(EndPile('spade'))==0
assert len(EndPile('heart').stack(('heart','ace')))==1
assert error_test.expect('EndPile("diamond").stack(("club","ace"))',IllegalMove,global_variables={'IllegalMove':IllegalMove,'EndPile':EndPile,'CardPile':CardPile,'Card':Card,'Rank':Rank,'Suit':Suit,'Color':Color})
assert error_test.expect('EndPile("spade").stack(("spade","six"))',IllegalMove,global_variables={'IllegalMove':IllegalMove,'EndPile':EndPile,'CardPile':CardPile,'Card':Card,'Rank':Rank,'Suit':Suit,'Color':Color})
assert error_test.expect('EndPile("heart").stack(("heart","ace")).stack(("heart","three"))',IllegalMove,global_variables={'IllegalMove':IllegalMove,'EndPile':EndPile,'CardPile':CardPile,'Card':Card,'Rank':Rank,'Suit':Suit,'Color':Color})
assert repr(EndPile('diamond'))=="EndPile(Suit('diamond'))"
assert repr(EndPile('club',('club','A',False),('club','two',False)))=="EndPile(Suit('club'),Card(Suit('club'),Rank('ace'),False),Card(Suit('club'),Rank('two'),False))"
assert str(EndPile('spade'))=='[]'
assert str(EndPile('heart',('heart','ace',False),('heart','two',False)))=='h2'

class DiscardPile(CardPile):
    '''piles where discarded cards go and can be recycled back into the deck'''
    def __init__(self,*init_cards:tuple):
        self.cards=[]
        for card in init_cards:
            if not isinstance(card,(tuple,Card)):
                raise TypeError('DiscardPile() *init_cards argument must contain only tuple or Card types, not '+str(type(card)))
            if isinstance(card,tuple):
                self.cards.append(Card(card[0],card[1],False))
            else:
                self.cards.append(Card(card.suit,card.rank,False))
    def topCard(self):
        return self.cards[len(self)-1]
    def take(n:int=1):
        if not isinstance(n,int):
            raise TypeError('DiscardPile.take() n argument must be an integer, not a '+str(type(n)))
        if n>len(self):
            raise IndexError('Can only .take() up to '+str(len(self))+' cards, not '+str(n))
        cards=CardPile()
        for i in range(n):
            cards.add(self.topCard())
            self.cards.pop()
        return cards
    def reset(self):
        if len(self)<1:
            raise IllegalMove('DiscardPile() must have at least 1 Card to use .reset()')
        cards=self.cards
        self.cards=[]
        return CardPile(*cards)
    def stack(self,*cards:tuple):
        if not isinstance(cards,(tuple,CardPile)):
            raise TypeError('DiscardPile.stack() *cards argument must be a tuple or a CardPile, not a '+str(type(cards)))
        if len(cards)<1:
            raise IndexError('DiscardPile.stack() *cards argument must contain at least 1 Card, not '+str(len(cards)))
        for card in cards:
            if not isinstance(card,(Card,tuple)):
                raise TypeError('DiscardPile.stack() *cards argument must contain only Card types or tuple types, not '+str(type(card))+' types')
            if isinstance(card,tuple):
                self.add(Card(card[0],card[1],False))
            else:
                self.add(Card(card.suit,card.rank,False))
        return self
    def __str__(self):
        if len(self)>0:
            return str(self.topCard())
        else:
            return '[]'
    def __repr__(self):
        display='DiscardPile('
        if len(self)>0:
            for card in self.cards:
                display+=repr(card)+','
            return display[0:-1]+')'
        else:
            return display+')'
assert len(DiscardPile())==0
assert len(DiscardPile(('spade','ace')))==1
assert DiscardPile(('diamond','eight'),('club','jack')).topCard()==Card('club','jack',False)
assert DiscardPile(('spade','three'),('heart','king')).reset()==CardPile(('spade','three',False),('heart','king',False))
assert str(DiscardPile())=='[]'
assert repr(DiscardPile())=='DiscardPile()'
assert str(DiscardPile(('diamond','six'),('club','ace')))=='cA'
assert repr(DiscardPile(('spade','two'),('spade','queen')))=='DiscardPile(Card(Suit(\'spade\'),Rank(\'two\'),False),Card(Suit(\'spade\'),Rank(\'queen\'),False))'
assert DiscardPile().stack(('diamond','four'),('heart','jack'))==DiscardPile(('diamond','four'),('heart','jack'))
assert error_test.expect('DiscardPile().reset()',IllegalMove,global_variables={'IllegalMove':IllegalMove,'DiscardPile':DiscardPile,'CardPile':CardPile,'Card':Card,'Rank':Rank,'Suit':Suit,'Color':Color})
assert error_test.expect('DiscardPile().stack()',IndexError,global_variables={'DiscardPile':DiscardPile,'CardPile':CardPile,'Card':Card,'Rank':Rank,'Suit':Suit,'Color':Color})
