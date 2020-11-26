from enum import Enum, auto


class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


class Config:
    # no of columns
    N = 8
    # no of rows
    M = 10
    # default start position of agent
    DEFAULT_START_X = 0
    DEFAULT_START_Y = 0
    # default facing direction of the agent
    DEFAULT_FACING_DIRECTION = Direction.NORTH.name

    CLOCKWISE = 1
    ANTI_CLOCKWISE = 0

    # path to the commands file
    INPUT_FILE_PATH = 'input_data.txt'

    DELIMITER = ' '


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
