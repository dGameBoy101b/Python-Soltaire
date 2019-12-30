from solitaire.console.command_base import Command, Unavailable, MoreArgsRequired
from solitaire.game.card import Card

class SubmitCommand(Command):
    keyword = 'submit'
    desc = 'submit a free card to the correct endpile'

    def run(com_args: [str], game_vars: dict) -> dict:
        if not game_vars['game']:
            raise Unavailable('|command \'submit\' is not available yet')
        #refine user input
        try:
            card_str = com_args[0]
        except IndexError:
            raise MoreArgsRequired('1 argument required to execute \''+SubmitCommand.keyword+'\'!')
        suit = card_str[0]
        rank = card_str[1:3]
        card = Card(suit, rank, False)
        #find given card
        for pile in game_vars['build_piles']:
            if len(pile) > 0 and pile.topCard() == card:
                src_pile = pile
                break
        else:
            if game_vars['discard_pile'].topCard() == card:
                src_pile = game_vars['discard_pile']
            else:
                raise IllegalMove('!\''+card_str+'\' card not found in valid position')
        #find correct end pile
        for pile in game_vars['end_piles']:
            if pile.suit == card.suit:
                dest_pile = pile
                break
        else:
            raise IllegalMove('!matching end pile for \''+card_str+'\' not found')
        #attempt action
        cards = src_pile.take()
        for card in cards:
            dest_pile.stack(card)
        return game_vars
