from solitaire.console.command_base import Command

class RulesCommand(Command):
    RULES = '\n'
    keyword = 'rules'
    desc = 'display the rules of Solitaire'

    def run(com_args: [str], game_vars: dict):
        print(RulesCommand.RULES)
        return
