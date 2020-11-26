# The configuration file for the entire project

from enum import Enum, auto


class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


class Constants:
    PLACE_ACTION_ARGUMENTS = 4
    CLOCKWISE = 1
    ANTI_CLOCKWISE = 0
    DELIMITER = ' '
    INPUT_FILE_PATH = 'input_data.txt'


class CommandType(Enum):
    MOVE = auto()
    REPORT = auto()
    LEFT = auto()
    RIGHT = auto()
    PLACE = auto()


DIRECTION_VECTORS = {
    Direction.NORTH.name: [0, 1],
    Direction.SOUTH.name: [0, -1],
    Direction.EAST.name: [1, 0],
    Direction.WEST.name: [-1, 0]
}
