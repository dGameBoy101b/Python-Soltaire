from solitaire.console.command_base import Command, Unavailable, MoreArgsRequired
from solitaire.game.card import Card
from solitaire.game.card_pile import IllegalMove

class StackCommand(Command):
    keyword = 'stack'
    desc = 'stack card(s) onto a build pile'

    def run(com_args: [str], game_vars: dict) -> dict:
        if not game_vars['game']:
            raise Unavailable('command \'stack\' is not available yet')
        #refine user input
        try:
            card_from = com_args[0]
        except IndexError:
            raise MoreArgsRequired('at least 1 argument required to execute \''+StackCommand.keyword+'\'!')
        card_from = Card(card_from[0], card_from[1:3], False)
        if not card_from.rank == 'king':
            try:
                card_to = com_args[1]
            except IndexError:
                raise MoreArgsRequired('2 arguments required to execute non-king \''+StackCommand.keyword+'\'!')
            card_to = Card(card_to[0], card_to[1:3], False)
        else:
            card_to = None
        #find from card
        for i in range(len(game_vars['build_piles'])):
            if card_from in game_vars['build_piles'][i]:
                pile_from = 'build_piles'
                pile_from_index = i
                break
        else:
            if card_from == game_vars['discard_pile'].topCard():
                pile_from = 'discard_pile'
            else:
                for i in range(len(game_vars['end_piles'])):
                    if card_from == game_vars['end_piles'][i].topCard():
                        pile_from = 'end_piles'
                        pile_from_index = i
                else:
                    raise IllegalMove('\''+card_from+'\' card cannot be found in valid position!')
        #find to card
        if not card_from.rank == 'king':
            for i in range(len(game_vars['build_piles'])):
                if len(game_vars['build_piles'][i]) > 0 and card_to == game_vars['build_piles'][i].topCard():
                    pile_to_index = i
                    break
            else:
                raise IllegalMove('\''+card_to+'\' card cannot be found in valid position!')
        else:
            for i in range(len(game_vars['build_piles'])):
                if len(game_vars['build_piles'][i]) < 1:
                    pile_to_index = i
                    break
            else:
                raise IllegalMove('empty build pile cannot be found for \''+str(card_from)+'\'!')
        #attempt action
        if pile_from == 'discard_pile':
            cards = game_vars['discard_pile'].take()
        else:
            cards = game_vars[pile_from][pile_from_index].take(len(game_vars[pile_from][pile_from_index]) - game_vars[pile_from][pile_from_index].cards.index(card_from))
        for card in cards:
            game_vars['build_piles'][pile_to_index].stack(card)
        return game_vars
