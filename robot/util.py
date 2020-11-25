
# validate the parameters associated with the 'PLACE' command
from robot.app_error import CommandArgumentError
from robot.config import Config, DIRECTION_VECTORS


def validate_command_parameters(direction, x, y):
    if not x.isnumeric():
        raise CommandArgumentError(x, 'Command argument not an Integer')
    if int(x) < 0 or int(x) >= Config.N:
        raise CommandArgumentError(x, 'x value outside the board')
    if not y.isnumeric():
        raise CommandArgumentError(y, 'Command argument not an Integer')
    if int(y) < 0 or int(y) >= Config.M:
        raise CommandArgumentError(y, 'y value outside the board')
    if not direction.strip() in DIRECTION_VECTORS:
        raise CommandArgumentError(direction.strip(), 'Invalid direction value')