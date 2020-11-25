
class ApplicationError(Exception):
    pass


class CommandError(ApplicationError):

    def __init__(self, command, error_message):
        self.command = command
        self.error_message = error_message

    def print_error_message(self, command_string):
        print(self.error_message, '::', self.command.strip(), 'in', command_string.strip())


class CommandArgumentError(CommandError):

    def __init__(self, argument, error_message):
        CommandError.__init__(self, 'PLACE', error_message)
        self.argument = argument

    def print_error_message(self, command_string):
        print(self.argument, self.error_message, 'in', command_string.strip())
