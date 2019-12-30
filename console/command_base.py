class Unavailable(Exception):
    '''command cannot be executed in current context'''

class MoreArgsRequired(Exception):
    '''command requires more arguments to execute'''

class Command():
    '''the base class for game commands'''
    ARG_SEP = ' '
    desc = NotImplemented
    keyword = NotImplemented

    def run(com_args: [str], game_vars: dict):
        '''the method to called when the command is executed'''
        raise NotImplementedError('This method should be overridden by derivative classes!')
