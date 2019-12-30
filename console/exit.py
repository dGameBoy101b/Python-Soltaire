from solitaire.console.command_base import Command

class ExitCommand(Command):
    FAREWELL = 'Thank you for playing Solitaire'
    
    keyword = 'exit'
    desc = 'close this program'

    def run(com_args: [str], game_vars: dict):
        print(ExitCommand.FAREWELL)
        raise SystemExit
