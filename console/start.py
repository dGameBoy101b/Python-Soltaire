from solitaire.console.command_base import Command
from solitaire.game.deck import Deck
from solitaire.game.end_pile import EndPile
from solitaire.game.build_pile import BuildingPile
from solitaire.game.discard_pile import DiscardPile
from solitaire.game.suit import Suit

class StartCommand(Command):
    keyword = 'start'
    desc = 'start a new game of Solitaire'

    def run(com_args: [str], game_vars: dict):
        #initialise deck
        game_vars['deck'] = Deck()
        game_vars['deck'].shuffle()
        #initialise end piles
        game_vars['end_piles'] = []
        for suit in Suit.suits:
            game_vars['end_piles'].append(EndPile(suit))
        #initialise build piles
        game_vars['build_piles'] = []
        for i in range(7):
            game_vars['build_piles'].append(BuildingPile())
            for j in range(i):
                game_vars['build_piles'][i].add(game_vars['deck'].take())
            game_vars['build_piles'][i].add(game_vars['deck'].take().flip())
        #initialise discard pile
        game_vars['discard_pile'] = DiscardPile()
        #start game
        game_vars['game'] = True
        return game_vars
