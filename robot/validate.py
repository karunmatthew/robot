from error.app_error import CommandArgumentError
from robot.config import Config, DIRECTION_VECTORS


# validate the parameters associated with the 'PLACE' command
def validate_command_parameters(direction, x, y):
    validate_is_numeric(x, Config.N)
    validate_is_numeric(y, Config.M)
    if not direction.strip() in DIRECTION_VECTORS:
        raise CommandArgumentError(direction.strip(),
                                   'Unsupported direction value')


# validate if the argument to the command is a non-negative integer
# within the bounds of the board
def validate_is_numeric(value, max_limit):
    if not value.isnumeric():
        raise CommandArgumentError(value, 'Expected a non-negative integer')
    if int(value) < 0 or int(value) >= max_limit:
        raise CommandArgumentError(value, 'Expected value within range [0,' +
                                   str(max_limit - 1) + ']')
