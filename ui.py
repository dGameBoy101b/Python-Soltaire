import class_def
import sys
COMMANDS={'exit':('close this program',0,0),
          'commands':('display this list of commands',0,0),
          'rules':('display the rules of solitaire',0,0),
          'start':('start a new game of solitaire',0,0),
          'submit':('submit a free card to the correct endpile',1,1),
          'stack':('stack card(s) onto a build pile',1,2),
          'cycle':('deal out another 3 cards to the discard',0,0),
          'recycle':('return all cards from discard to deck',0,0)}
RULES=...
WELCOME=...
game=False
def exit():
    '''close the program'''
    raise SystemExit

def rules():
    '''display the rules of solitaire'''
    print(RULES)
    return

def commands():
    '''display the list of commands'''
    for key in COMMANDS:
        line=key+' : '+COMMANDS[key][0]
        print(line)
    return

def start():
    '''begin a new game of solitaire'''
    global deck, end_piles, build_piles, discard_pile, game
    deck=class_def.Deck()
    deck.shuffle()
    end_piles=list()
    for suit in class_def.Suit.suits:
        end_piles.append(class_def.EndPile(suit))
    build_piles=list()
    for i in range(7):
        build_piles.append(class_def.BuildingPile())
        for j in range(i):
            build_piles[i].add(deck.take())
        build_piles[i].add(deck.take().flip())
    discard_pile=class_def.DiscardPile()
    game=True
    return

def submit(card_str:str):
    '''attempt to submit given card to an end pile'''
    global end_piles, build_piles, discard_pile, game
    if not game:
        raise class_def.Unavailable('|command \'submit\' is not available yet')
    #refine user input
    suit=card_str[0]
    rank=card_str[1:3]
    card=class_def.Card(suit,rank,False)
    #find given card
    for pile in build_piles:
        if len(pile)>0 and pile.topCard()==card:
            src_pile=pile
            break
    else:
        if discard_pile.topCard()==card:
            src_pile=discard_pile
        else:
            raise class_def.IllegalMove('!\''+card_str+'\' card not found in valid position')
    print(repr(src_pile))
    #find correct end pile
    for pile in end_piles:
        if pile.suit==card.suit:
            dest_pile=pile
            break
    else:
        raise class_def.IllegalMove('!matching end pile for \''+card_str+'\' found')
    print(repr(dest_pile))
    #attempt action
    cards=src_pile.take()
    for card in cards:
        dest_pile.stack(card)
    return

def stack(card_from,card_to=''):
    '''move a card to a vaild build pile'''
    global build_piles, discard_pile, end_piles, game
    if not game:
        raise class_def.Unavailable('|command \'stack\' is not available yet')
    #refine user input
    card_from=class_def.Card(card_from[0],card_from[1:3],False)
    if not card_from.rank=='king':
        card_to=class_def.Card(card_to[0],card_to[1:3],False)
    #find from card
    for pile in build_piles:
        if card_from in pile:
            pile_from=pile
            break
    else:
        if card_from==discard_pile.topCard():
            pile_from=discard_pile
        else:
            for pile in end_piles:
                if card_from==pile.topCard():
                    pile_from=pile
            else:
                raise class_def.IllegalMove('!\''+card_from+'\' card cannot be found in valid position')
    #find to card
    if not card_from.rank=='king':
        for pile in build_piles:
            if len(pile)>0 and card_to==pile.topCard():
                pile_to=pile
                break
        else:
            raise class_def.IllegalMove('!\''+card_to+'\' card cannot be found in valid position')
    elif str(card_to)=='':
        for pile in build_piles:
            if len(pile)<1:
                pile_to=pile
                break
        else:
            raise class_def.IllegalMove('| empty build pile cannot be found for \''+card_from+'\'')
    else:
        raise class_def.IllegalMove('! \''+card_from+'\' must be stacked onto empty build pile')
    #attempt action
    cards=pile_from.take(len(pile_from)-pile_from.cards.index(card_from))
    for card in cards:
        pile_to.stack(card)
    return

def cycle():
    '''move 3 cards from deck to discard pile'''
    global deck, discard_pile, game
    if not game:
        raise class_def.Unavailable('|command \'cycle\' is not available yet')
    if len(deck)<1:
        raise class_def.IllegalMove('!no more cards in deck to cycle')
    elif len(deck)>=3:
        cards=deck.deal(3)
    else:
        cards=deck.deal(len(deck))
    for card in cards:
        discard_pile.stack(card)
    return

def recycle():
    '''mov all cards from discard pile to deck once deck is empty'''
    global deck, discard_pile, game
    if not game:
        raise class_def.Unavailable('|command \'recycle\' is not available yet')
    if len(discard_pile)<1:
        raise class_def.IllegalMove('!no cards in discard pile to recycle')
    elif len(deck)>0:
        raise class_def.IllegalMove('!deck must be empty to recycle')
    else:
        cards=discard_pile.reset()
        for card in cards:
            deck.add(card)
    return

def display():
    '''display current state of solitaire game'''
    if game:
        global deck, end_piles, build_piles, discard_pile
        line=''
        for pile in end_piles:
            line+=str(pile)+' '
        line.rstrip()
        print(line)
        print('-'*len(line))
        for pile in build_piles:
            print(str(pile))
        line=str(deck)+'\t'+str(discard_pile)
        line=line.expandtabs()
        print('-'*len(line))
        print(line)
    return

def command(com:str=''):
    global COMMANDS
    com=com.split()
    if com[0] in COMMANDS:
        min_arg=COMMANDS[com[0]][1]
        max_arg=COMMANDS[com[0]][2]
        try:
            if len(com)-1<min_arg or len(com)-1>max_arg:
                raise ValueError('!incorrect number of arguments: must be between '+str(min_arg)+' and '+str(max_arg)+' for \''+str(com[0])+'\' command')
            if len(com)>1:
                command=com[0]+'('
                for i in range(COMMANDS[com[0]][2]):
                    try:
                        command+='\''+com[i+1]+'\','
                    finally:
                        pass
                command=command[0:-1]+')'
            else:
                command=com[0]+'()'
            print('|executing '+repr(command)+'...')
            eval(command)
        except (class_def.IllegalMove, ValueError, class_def.Unavailable):
            print(sys.exc_info()[1])
            input('...> ')
        except:
            raise
    else:
        print('|command not recognised')
    print()
    return

print(WELCOME)
print()
commands()
print()
while True:
    command(input('command> '))
    display()
