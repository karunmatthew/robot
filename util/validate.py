from error.app_error import CommandArgumentError
from util.constants import DIRECTION_VECTORS
import configparser


# validate the parameters associated with the 'PLACE' command
def validate_command_parameters(direction, x, y):

    config = configparser.ConfigParser()
    config.read('config.ini')

    max_columns = int(config['DEFAULT']['N'])
    max_rows = int(config['DEFAULT']['M'])

    validate_is_numeric(x, max_columns)
    validate_is_numeric(y, max_rows)
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
