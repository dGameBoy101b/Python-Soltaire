from solitaire.console.commands import CommandsCommand
from solitaire.console.cycle import CycleCommand
from solitaire.console.exit import ExitCommand
from solitaire.console.recycle import RecycleCommand
from solitaire.console.rules import RulesCommand
from solitaire.console.stack import StackCommand
from solitaire.console.start import StartCommand
from solitaire.console.submit import SubmitCommand
from solitaire.console.command_base import Unavailable, MoreArgsRequired
from solitaire.game.card_pile import IllegalMove

class TextInterface():
    '''a command based interface for a game of solitaire'''

    WELCOME = '\n'
    COM_PROMPT = 'command> '
    ERR_PROMPT = 'error> '
    COMMANDS = frozenset({CommandsCommand,
                CycleCommand,
                ExitCommand,
                RecycleCommand,
                RulesCommand,
                StackCommand,
                StartCommand,
                SubmitCommand})

    game_vars = {'game': False,
                 'end_piles': [None] * 4,
                 'build_piles': [None] * 7,
                 'deck': None,
                 'discard_pile': None}

    def display():
        '''display current state of solitaire game'''
        if TextInterface.game_vars['game']:
            line = ''
            for pile in TextInterface.game_vars['end_piles']:
                line += str(pile) + ' '
            line.rstrip()
            print(line)
            print('-' * len(line))
            for pile in TextInterface.game_vars['build_piles']:
                print(str(pile))
            line = (str(TextInterface.game_vars['deck']) + '\t'
                    + str(TextInterface.game_vars['discard_pile']))
            line = line.expandtabs()
            print('-' * len(line))
            print(line)
        return

    def command(com: str):
        com_parts = com.split(' ')
        for i in range(len(com_parts)):
            com_parts[i] = com_parts[i].strip()
        while True:
            try:
                com_parts = com_parts.remove('')
            except ValueError:
                break
        com_args = com_parts[1:]
        keyword = com_parts[0]
        for command in TextInterface.COMMANDS:
            if keyword == command.keyword:
                try:
                    res = command.run(com_args, TextInterface.game_vars)
                except (IllegalMove, MoreArgsRequired, Unavailable) as e:
                    print(TextInterface.ERR_PROMPT + str(e))
                    return
                if res != None:
                    TextInterface.game_vars = res
                break
        return

    def main():
        print(TextInterface.WELCOME)
        CommandsCommand.run([], TextInterface.game_vars)
        while True:
            TextInterface.command(input(TextInterface.COM_PROMPT))
            TextInterface.display()

if __name__ == '__main__':
    TextInterface.main()
