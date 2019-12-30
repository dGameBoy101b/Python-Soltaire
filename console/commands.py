from solitaire.console.command_base import Command
from solitaire.console.exit import ExitCommand
from solitaire.console.rules import RulesCommand
from solitaire.console.start import StartCommand
from solitaire.console.submit import SubmitCommand
from solitaire.console.stack import StackCommand
from solitaire.console.cycle import CycleCommand
from solitaire.console.recycle import RecycleCommand

class CommandsCommand(Command):
    keyword = 'commands'
    desc = 'display this list of commands'

    COM_SEP = ' : '
    COMMANDS = (ExitCommand,
                RulesCommand,
                StartCommand,
                SubmitCommand,
                StackCommand,
                CycleCommand,
                RecycleCommand)

    def run(com_args: [str], game_vars: dict) -> dict:
        print(CommandsCommand.keyword + CommandsCommand.COM_SEP + CommandsCommand.desc)
        for com in CommandsCommand.COMMANDS:
            print(com.keyword + CommandsCommand.COM_SEP + com.desc)
        return game_vars
