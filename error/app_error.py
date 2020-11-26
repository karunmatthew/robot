

# base class for all application specific errors
# can be extended if a new type of error is encountered
class ApplicationError(Exception):
    pass


# handles all the command specific errors
class CommandError(ApplicationError):

    def __init__(self, command, error_message):
        self.command = command
        self.error_message = error_message

    def print_error_message(self, command_string):
        print('ERROR ::', command_string.strip(), '::', self.error_message,
              '::', self.command.strip())


# handles errors associated with passing in wrong
# arguments for executing a command
class CommandArgumentError(CommandError):

    def __init__(self, argument, error_message):
        CommandError.__init__(self, 'PLACE', error_message)
        self.argument = argument

    def print_error_message(self, command_string):
        print('ERROR ::', command_string.strip(), '::', self.argument,
              self.error_message)
