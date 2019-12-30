from solitaire.console.command_base import Command, Unavailable
from solitaire.game.card_pile import IllegalMove

class CycleCommand(Command):
    keyword = 'cycle'
    desc = 'deal out another 3 cards to the discard'

    def run(com_args: [str], game_vars: dict) -> dict:
        if not game_vars['game']:
            raise Unavailable('command \'cycle\' is not available yet')
        if len(game_vars['deck']) < 1:
            raise IllegalMove('no more cards in deck to cycle!')
        elif len(game_vars['deck']) >= 3:
            cards = game_vars['deck'].deal(3)
        else:
            cards = game_vars['deck'].deal(len(game_vars['deck']))
        for card in cards:
            game_vars['discard_pile'].stack(card)
        return game_vars
