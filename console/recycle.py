from solitaire.console.command_base import Command, Unavailable

class RecycleCommand(Command):
    keyword = 'recycle'
    desc = 'return all cards from discard to deck'

    def run(com_args: [str], game_vars: dict) -> dict:
        if not game_vars['game']:
            raise Unavailable('|command \'recycle\' is not available yet')
        if len(game_vars['discard_pile']) < 1:
            raise IllegalMove('!no cards in discard pile to recycle')
        elif len(game_vars['deck']) > 0:
            raise IllegalMove('!deck must be empty to recycle')
        else:
            cards = game_vars['discard_pile'].reset()
            for card in cards:
                game_vars['deck'].add(card)
        return game_vars
